"""Independent numerical checks of the manuscript (Python 3 + NumPy).

Stationary probabilities are solved from normalized balance equations;
first-passage times from killed backward generators. No manuscript
response formula is used to obtain either quantity.
"""
from collections import defaultdict
import json
from pathlib import Path

import numpy as np


RNG = np.random.default_rng(19681980)
ERRORS = defaultdict(float)
COUNTS = defaultdict(int)


def check(name, actual, expected, tolerance=2e-10):
    actual, expected = np.asarray(actual), np.asarray(expected)
    error = float(np.max(np.abs(actual - expected)))
    scale = max(1.0, float(np.max(np.abs(expected))))
    ERRORS[name] = max(ERRORS[name], error / scale)
    COUNTS[name] += 1
    assert error <= tolerance * scale, (name, error, scale)


def generator(rates):
    w = rates.copy()
    np.fill_diagonal(w, 0.0)
    w -= np.diag(w.sum(axis=0))
    return w


def stationary(w):
    a = w.copy()
    a[-1] = 1.0
    rhs = np.zeros(len(w))
    rhs[-1] = 1.0
    return np.linalg.solve(a, rhs)


def group_inverse(w, p):
    projector = np.outer(p, np.ones(len(w)))
    nu = max(-np.diag(w))
    return np.linalg.inv(w + nu * projector) - projector / nu


def first_passage(w, target):
    keep = np.arange(len(w)) != target
    tau = np.zeros(len(w))
    tau[keep] = np.linalg.solve(w.T[np.ix_(keep, keep)], -np.ones(keep.sum()))
    return tau


def edge_vectors(w, a, b):
    basis = np.eye(len(w))
    return basis[b] - basis[a], w[b, a] * basis[a] - w[a, b] * basis[b]


def generic_checks():
    for n in range(3, 10):
        for _ in range(12):
            rates = np.exp(RNG.uniform(-2, 2, (n, n)))
            w = generator(rates)
            p = stationary(w)
            g = group_inverse(w, p)
            projector = np.outer(p, np.ones(n))
            check('group inverse', w @ g, np.eye(n) - projector)
            check('group inverse commutation', g @ w, w @ g)
            check('group inverse normalization', np.ones(n) @ g, np.zeros(n))

            wp = generator(np.exp(RNG.uniform(-3, 3, (n, n))))
            pp = stationary(wp)
            dw = wp - w
            check('arbitrary finite perturbation', pp - p, -g @ dw @ pp)
            check('normalized Moore-Penrose', pp - p,
                  -(np.eye(n) - projector) @ np.linalg.pinv(w) @ dw @ pp)
            nu = 1.1 * max(max(-w.diagonal()), max(-wp.diagonal()))
            t, tp = np.eye(n) + w / nu, np.eye(n) + wp / nu
            z = np.linalg.inv(np.eye(n) - t + projector)
            check('fundamental matrix', z, projector - nu * g)
            check('fundamental finite response', pp - p, z @ (tp - t) @ pp)

            a, b = 0, 1
            d, c = edge_vectors(w, a, b)
            h = -g @ d
            kappa = 1 + c @ h
            w0 = w - np.outer(d, c)
            p0 = stationary(w0)
            g0 = group_inverse(w0, p0)
            check('deleted-edge direction', h / kappa, -g0 @ d)
            for target in range(n):
                tau = first_passage(w, target)
                check('first-passage representation', tau,
                      (g[target] - g[target, target]) / p[target])
                check('first-passage response direction', h[target],
                      p[target] * (tau[a] - tau[b]))

            perturbations = []
            for _ in range(8):
                rp = rates.copy()
                rp[b, a], rp[a, b] = np.exp(RNG.uniform(-4, 4, 2))
                wp = generator(rp)
                pp = stationary(wp)
                gp = group_inverse(wp, pp)
                _, cp = edge_vectors(wp, a, b)
                v = cp - c
                alpha = v @ pp
                check('one-edge affine line', pp - p, alpha * h)
                check('finite scalar amplitude', alpha, (v @ p) / (1 - v @ h))
                check('physical input current', cp @ pp - c @ p, alpha * kappa)
                check('deleted-network stationary state', pp, p0 - g0 @ d * (cp @ pp))
                check('reference direction rescaling', -gp @ d, h / (1 - v @ h))
                for x in range(n):
                    for y in range(x + 1, n):
                        if (x, y) == (a, b):
                            continue
                        _, ce = edge_vectors(w, x, y)
                        slope = (ce @ h) / kappa
                        check('current-current law', ce @ (pp - p),
                              slope * (cp @ pp - c @ p))
                        hp = -gp @ d
                        check('slope reference invariance', slope,
                              (ce @ hp) / (1 + cp @ hp))
                perturbations.append(pp - p)
            singular_values = np.linalg.svd(np.array(perturbations), compute_uv=False)
            check('probability response dimension one', singular_values[1:],
                  np.zeros_like(singular_values[1:]))

            # Central differences use fresh, independently solved stationary states.
            for source, target, expected in [(a, b, h * p[a]), (b, a, -h * p[b])]:
                eps = 1e-5 * rates[target, source]
                rp, rm = rates.copy(), rates.copy()
                rp[target, source] += eps
                rm[target, source] -= eps
                derivative = (stationary(generator(rp)) - stationary(generator(rm))) / (2 * eps)
                check('differential rate response', derivative, expected, tolerance=2e-8)


def multiple_edge_checks():
    n = 6
    rates = np.exp(RNG.uniform(-1, 1, (n, n)))
    w = generator(rates)
    p = stationary(w)
    g = group_inverse(w, p)
    inputs = [(0, 1), (1, 2), (2, 0)]  # Three edges, incidence rank two.
    bmat = np.column_stack([edge_vectors(w, *edge)[0] for edge in inputs])
    cmat = np.column_stack([edge_vectors(w, *edge)[1] for edge in inputs])
    w0 = w - bmat @ cmat.T
    p0 = stationary(w0)
    g0 = group_inverse(w0, p0)
    samples = []
    for _ in range(80):
        rp = rates.copy()
        for a, b in inputs:
            rp[b, a], rp[a, b] = np.exp(RNG.uniform(-3, 3, 2))
        wp = generator(rp)
        pp = stationary(wp)
        cp = np.column_stack([edge_vectors(wp, *edge)[1] for edge in inputs])
        currents = cp.T @ pp
        check('multiple-input stationary state', pp, p0 - g0 @ bmat @ currents)
        check('fixed-range finite response', pp - p, -g @ bmat @ (cp - cmat).T @ pp)
        _, output = edge_vectors(w, 3, 4)
        check('multiple-input output current', output @ pp,
              output @ p0 - output @ g0 @ bmat @ currents)
        samples.append(pp - p)
    check('incidence rank', np.linalg.matrix_rank(bmat), 2)
    singular_values = np.linalg.svd(np.array(samples), compute_uv=False)
    check('probability response dimension two', singular_values[2:],
          np.zeros_like(singular_values[2:]))
    assert singular_values[1] > 1e-3


def degeneracy_checks():
    rates = np.zeros((6, 6))
    for a, b in [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3), (2, 3)]:
        rates[b, a], rates[a, b] = np.exp(RNG.uniform(-1, 1, 2))
    w = generator(rates)
    p = stationary(w)
    g = group_inverse(w, p)
    d, c = edge_vectors(w, 2, 3)
    h = -g @ d
    check('bridge denominator', 1 + c @ h, 0)
    check('bridge current', c @ p, 0)
    rp = rates.copy()
    rp[3, 2] *= 7
    wp = generator(rp)
    pp = stationary(wp)
    _, cp = edge_vectors(wp, 2, 3)
    check('changed bridge current', cp @ pp, 0)
    check('bridge probability response', pp - p, h * ((cp - c) @ pp))
    assert np.linalg.norm(pp - p) > 0.05

    rates = np.ones((3, 3))
    w = generator(rates)
    p = stationary(w)
    d, _ = edge_vectors(w, 0, 1)
    h = -group_inverse(w, p) @ d
    check('positive probability with zero response', h[2], 0)
    rates[1, 0], rates[0, 1] = 13, 0.2
    pp = stationary(generator(rates))
    check('insensitive probability remains fixed', pp[2], p[2])
    assert abs(pp[0] - p[0]) > 0.05

    rates = np.array([[0., 3.], [2., 0.]])
    p = stationary(generator(rates))
    pp = stationary(generator(5 * rates))
    check('traffic counterexample fixed probabilities', pp, p)
    traffic = rates[1, 0] * p[0] + rates[0, 1] * p[1]
    traffic_prime = 5 * (rates[1, 0] * pp[0] + rates[0, 1] * pp[1])
    check('traffic counterexample changing traffic', traffic_prime / traffic, 5)


def laplace_checks():
    """Solve both transformed master equations at real and complex frequencies."""
    for n in (3, 5, 8):
        for _ in range(6):
            rates = np.exp(RNG.uniform(-2, 2, (n, n)))
            w = generator(rates)
            p_initial = RNG.dirichlet(np.ones(n))
            d, c = edge_vectors(w, 0, 1)
            _, c_output = edge_vectors(w, 1, 2)
            for s in (0.1, 2.0, 0.2 + 1.3j, 1.0 + 7.0j):
                a = s * np.eye(n) - w
                transformed = np.linalg.solve(a, p_initial)
                h = np.linalg.solve(a, d)
                m = int(np.argmax(np.abs(h)))
                slope = (c_output @ h) / (1 + c @ h)
                for _ in range(5):
                    changed_rates = rates.copy()
                    changed_rates[1, 0], changed_rates[0, 1] = np.exp(
                        RNG.uniform(-3, 3, 2))
                    wp = generator(changed_rates)
                    ap = s * np.eye(n) - wp
                    changed = np.linalg.solve(ap, p_initial)
                    hp = np.linalg.solve(ap, d)
                    _, cp = edge_vectors(wp, 0, 1)
                    alpha = (cp - c) @ changed
                    delta = changed - transformed
                    check('Laplace finite probability response', delta, h * alpha)
                    check('Laplace mutual probability linearity', delta,
                          h / h[m] * delta[m])
                    check('Laplace probability slope invariance', hp / hp[m],
                          h / h[m])
                    check('Laplace input current response',
                          cp @ changed - c @ transformed, (1 + c @ h) * alpha)
                    check('Laplace mutual current linearity', c_output @ delta,
                          slope * (cp @ changed - c @ transformed))
                    check('Laplace current slope invariance', slope,
                          (c_output @ hp) / (1 + cp @ hp))


if __name__ == '__main__':
    generic_checks()
    multiple_edge_checks()
    degeneracy_checks()
    laplace_checks()
    report = {
        'seed': 19681980,
        'assertions': sum(COUNTS.values()),
        'max_scaled_error': max(ERRORS.values()),
        'checks': {name: {'count': COUNTS[name], 'max_scaled_error': ERRORS[name]}
                   for name in sorted(COUNTS)},
    }
    output = Path(__file__).parent / 'build' / 'verification.json'
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + '\n')
    print(f"PASS: {report['assertions']} assertions in {len(COUNTS)} groups")
    print(f"Maximum scaled error: {report['max_scaled_error']:.3g}")
    print(f"Report: {output}")
