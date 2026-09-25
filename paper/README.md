# Mutual linearity from classical Markov response theory

Short PRE manuscript by **Timur Aslyamov and Massimiliano Esposito**.
The REVTeX preamble, fonts, author order, emails, and affiliation come from
`AdaptationLimit/paper/main.tex`; the journal option is changed to `pre`.

- `main.tex`: self-contained manuscript.
- `references.bib`: twelve references with verified publication or preprint metadata.
- `main.pdf`: compiled review copy.
- `verify_derivation.py`: reproducible numerical verification, requiring NumPy.
- `research/source_notes.md`: literature provenance, earlier discussions, and scope.
- `build/`: ignored compilation, rendering, and numerical-check output.

## Build

From this directory, with a TeX distribution providing REVTeX 4.2,
Libertine, newtxmath, and latexmk:

```sh
make
```

Equivalently:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
cp build/main.pdf main.pdf
```

For Overleaf, upload `main.tex` and `references.bib` and select pdfLaTeX.
No cross-paper labels, figures, or external research repository are required.

The current version uses the matrix entries `W_ij` and `W_ji` directly.
Four numbered sections cover the introduction, exact stationary response,
mutual linearity, and discussion and conclusions. The introduction states
the goal of deriving the known relations from classical finite-response theory.
It has ten equations and no boxed formulas. The discussion extends
the argument to nonsingular linear systems when one coefficient is varied,
explicitly eliminating the common factor between components `n` and `m`.
A separate paragraph states the fixed-direction generalization needed for
the Laplace-domain application. The text distinguishes the dependence of `h_n` on the starting
rates from the rate-independent ratios and cites the dynamical response-kernel
ratio in the authors' DFRR paper. A compact application with `A = s I - W`
derives Laplace-domain mutual linearity for a fixed initial distribution,
including the current relations and the distinction from instantaneous
mutual linearity in time. The broader rank-r, multiple-edge, and
uniformization discussions remain outside the short note.

## Verification

```sh
make verify
```

Override `PYTHON` if NumPy is installed in a separate environment.
The script obtains stationary distributions from normalized balance equations
and first-passage times from killed backward generators, independently of the
response formulas. It checks arbitrary finite perturbations, uniformization,
the normalized Moore-Penrose formula, simultaneous variation of both input rates,
current slopes and their reference invariance, first-passage identities,
multiple input currents, and the fixed-range dimension bound. Separate examples
cover bridge inputs, positive but insensitive state probabilities, and changing
traffic at fixed stationary probabilities.

The current run used seed `19681980` and passed 29,206 assertions in 38 groups.
The maximum scaled error was approximately `1.24e-13` for algebraic identities
and `6.69e-11` including finite-difference derivative checks. Detailed results
are written to `build/verification.json`. These checks complement the analytical
proofs; the manuscript does not rely on numerical evidence. The verification
script retains checks of the broader identities considered in the first draft;
those extensions are no longer part of the short manuscript. The rewritten
component formulas were additionally checked on 30 random models, including
the current coefficient and first-passage signs (maximum absolute residual
approximately `5e-16`).

The Laplace-domain extension adds 2,160 checks at real and complex frequencies,
solving both transformed master equations for the same initial distribution.
These check finite changes of probabilities and currents, including invariance
of their slopes under changes of the starting rates. The maximum scaled error
in these checks was approximately `1.23e-13`.

The PDF was rendered and inspected on every page. The final build has no
overfull boxes or unresolved citations/references. An informational Libertine
warning and the stock REVTeX bibliography-style warning can remain.
