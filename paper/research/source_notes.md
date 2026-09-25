# Sources and scope of the draft

Prepared on 25 September 2026. These are working notes, not manuscript text.

The manuscript was subsequently shortened at the user's request to a direct
component derivation using `W_ij` and `W_ji`, with no boxes. A subsequent
brief remark adds the ninth equation: for a nonsingular linear system with
fixed right-hand side, varying one coefficient or one row gives the same
common-factor response. Arbitrary perturbations of a linear system need not
have this property; the perturbation source must have a fixed direction.
The source record below describes the initial broader investigation. The
rank-r and multiple-edge extensions and uniformization
are not retained in the current manuscript. Nine of the twelve bibliography
entries are cited in the short version.

The annotated revision clarifies that `h_n` depends on the rates at the chosen
starting point, while its ratios are invariant under changes of the selected
edge. Explicitly, `h'_n = h_n / (1 - Delta W_ij h_j + Delta W_ji h_i)`;
the numerical verification already checks this rescaling and current-slope
invariance. The manuscript explains it through the common straight line.
The bridge example and concluding detailed-balance sentence were removed at
the user's request; the nonzero-denominator condition remains.

The DFRR citation was checked against `DFRR/paper/main.tex`, equation label
`eq:mutual-linearity`, and the public
[arXiv version 3](https://arxiv.org/html/2604.24626v3) of
[Aslyamov and Esposito, arXiv:2604.24626](https://arxiv.org/abs/2604.24626).
The forward/backward rate-response ratio applies to responses to impulsive
perturbations at the same time, including state observables and currents
with antisymmetric jump weights. It does not in general assert the analogous
ratio for responses to finite or time-integrated changes of the rates.

The frequency-domain addition follows directly from the nonsingular linear
system argument with `A = s I - W` and fixed right-hand side `p(0)`.
It compares time-independent generators at a fixed Laplace frequency with
positive real part, keeping the initial distribution unchanged. The finite
response direction is `(s I - W)^(-1) (e_i - e_j)`; as `s` tends to zero,
the stationary projector cancels and this tends to `-W^D (e_i - e_j)`.
The ratio of two direction components gives the probability relation, while
the existing current calculation includes the explicit rate change on the
perturbed edge. Frequency dependence gives a convolution relation in time.
Primary texts checked:

- [Harunari et al., arXiv:2402.13193](https://arxiv.org/html/2402.13193):
  frequency-domain current-current relations.
- [Zheng and Lu, arXiv:2604.06162](https://arxiv.org/html/2604.06162):
  Section V, nonstationary relaxation with a fixed initial distribution;
  state and counting observables excluding the varied transition count.
- [Voits and Schwarz, arXiv:2605.00135](https://arxiv.org/html/2605.00135):
  Section 3, Laplace-domain occupation-probability relations and their
  time-domain convolution interpretation. The manuscript does not reproduce
  the graph expansions, short-time asymptotics, or hitting-time results.

## Previous discussions consulted

- **Clarify MJP steady-state linearity**, task
  `01a0536f-0561-77c1-ab6c-8fe89f6e400c`, 30 August 2026.
  The user explicitly proposed subtracting the two stationary equations and
  applying the Drazin inverse. The discussion developed the fixed response
  direction, the direct contribution to the changed input-current functional,
  a deleted-edge representation, and the fixed-range rank-r generalization.
  It recommended treating the note as a unification of classical perturbation
  theory and recent physical results, rather than asserting a new finite-update
  identity or an unverified priority claim.
- **Explain mutual current linearity**, task
  `01a05376-1ece-73c0-9833-985a7fb60eec`, 30 August 2026.
  This distinguishes exact affine/unimolecular stationarity from nonlinear
  chemical kinetics, where a local derivative ratio generally does not
  integrate to a global affine relation. The present draft stays with finite
  Markov jump processes.

## Classical foundation

- [Schweitzer, J. Appl. Probab. 5, 401-413 (1968)](https://doi.org/10.2307/3212261):
  title and metadata verified on Cambridge Core. Its abstract explicitly
  describes perturbations of both stationary distributions and fundamental
  matrices. The publisher also has identifier `10.1017/S0021900200110083`;
  the bibliography uses the DOI displayed on the article page.
- [Meyer, SIAM Rev. 17, 443-464 (1975)](https://doi.org/10.1137/1017044):
  included for the group-inverse formulation and its relation to passage times.
- [Meyer, SIAM J. Algebraic Discrete Methods 1, 273-283 (1980)](https://doi.org/10.1137/0601031):
  publisher title, volume, issue, page range, and DOI checked. Its online
  publication date is 2006; the correct original publication year is 1980.
- [Hunter, Linear Algebra Appl. 82, 201-214 (1986)](https://doi.org/10.1016/0024-3795(86)90152-7):
  publisher abstract explicitly concerns rank-one stationary-distribution
  updates. Included because of the earlier discussion.

Historical metadata and abstracts were checked; the draft does not claim a
page-by-page examination of all the original paywalled papers. The central
finite-response identity is proved directly in the manuscript, with its sign,
column convention, normalization, and uniformization stated explicitly.

## Recent results

- [Harunari et al., PRL 133, 047401 (2024)](https://doi.org/10.1103/PhysRevLett.133.047401),
  [preprint](https://arxiv.org/abs/2402.13193): stationary current-current
  affinity under changes of the two input rates. The draft recovers the
  stationary relation, including the changing input-current functional.
  The later frequency-domain paragraph also recovers the basic transformed
  current relations. Graphical coefficients and open-network extensions
  remain outside the short note.
- [Khodabandehlou, Maes, and Netočný, J. Phys. A 58, 155002 (2025)](https://doi.org/10.1088/1751-8121/adc8ea),
  [preprint](https://arxiv.org/abs/2412.05019): Section III already starts
  from an exact difference of stationary distributions and expresses it in
  first-passage times. Its footnote at Eq. (III.1) identifies Eq. (44) of
  Harvey et al. as an antecedent and thanks Timur Aslyamov for pointing it out.
  This is why the manuscript explicitly acknowledges that equivalent route.
  The IOP page could not be retrieved; the article text was checked through
  the authors' PDF and arXiv, with publication data corroborated by the PRL
  bibliography and the supplied DOI.
- [Bebon and Speck, PRL 136, 137401 (2026)](https://doi.org/10.1103/jcm3-57d8),
  [preprint](https://arxiv.org/abs/2602.20321): probability-affinity and
  the ratio of forward/backward rate responses are recovered. Its general
  counting-observable definition excludes the input edge. The draft retains
  this restriction and separately handles the input current. It does not
  claim to recover all spanning-tree bounds or application results.
- [Dal Cengio et al., SciPost Phys. 19, 111 (2025)](https://doi.org/10.21468/SciPostPhys.19.4.111),
  [preprint](https://arxiv.org/abs/2502.04298): the admissible set of input
  edges leaves a connected remaining network. The draft gives the stationary
  affine relation for the corresponding irreducible remaining generator.
  The coefficients depend on the whole input set. Their transient/resolvent
  and fluctuation results are outside the scope of the note.
- [Harvey, Lahiri, and Ganguli, PRE 108, 014403 (2023)](https://doi.org/10.1103/PhysRevE.108.014403):
  bibliography metadata checked on APS. The manuscript attributes the
  Eq. (44) connection specifically to Khodabandehlou et al.; it does not
  present this as a newly discovered historical link.

Reference PDFs and extracted text are cached here locally and ignored by Git.

## Mathematical and editorial choices

1. Use the Drazin/group inverse, rather than silently substituting the
   Moore-Penrose inverse; the latter needs the normalization projector.
2. Start with the finite-change identity, as requested, and identify the
   fixed one-dimensional range before introducing observables.
3. State affinity using a cross-multiplied probability relation so that
   insensitive reference states are handled correctly. Positive stationary
   probability does not imply a nonzero response.
4. For current parametrization distinguish original irreducibility from
   irreducibility after deleting the input. An undirected nonbridge condition
   suffices when every remaining edge has positive rates in both directions;
   it is not a replacement for directed connectivity in general.
5. The rank-r statement needs a fixed containing range for the whole family.
   A bound on the rank of each perturbation separately is insufficient.
6. Frame the contribution as a short common derivation and geometric
   interpretation. No claim is made that the classical identity, all
   first-passage connections, or the recent current theorems are new here.

Numerical verification and build instructions are in `../README.md`.
