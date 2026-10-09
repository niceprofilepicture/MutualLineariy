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
are not retained in the current manuscript. Twenty-four of the twenty-five bibliography
entries are cited in the current version.

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

The chemical-network addition (9 October 2026) cites
[Harunari, Fiusa, and Polettini, arXiv:2610.11970v1](https://arxiv.org/html/2610.11970v1).
Their zero-deficiency, bidirectionality, and single-linkage-class assumptions
supply complex balance, `K psi = 0`, for positive stationary activities.
The manuscript assumes complex balance directly and now follows the same
finite-response derivation as for Markov jump processes. Applying `G = K^D`
to `K Delta psi = -Delta K psi'` gives
`Delta psi = (psi / S) Delta S + h alpha`, with `S = sum(psi)`,
`h = -G (e_i - e_j)`, and `alpha = Delta r_+ psi_j' - Delta r_- psi_i'`.
Thus `psi' = S' pi + h alpha`, where `pi = psi / S`.
Eliminating the two amplitudes recovers the homogeneous relation in their
Eq. (5), using coefficients `C_ab = pi_a h_b - pi_b h_a` evaluated in
the reference system and independent of the rate changes. This formulation
does not remove the controlled reaction and needs no nonbridge assumption.
If all three minors vanish for a selected triple,
its activities are mutually proportional; the displayed relation remains valid.
The manuscript includes this central stationary relation, without adding
activity-ratio bounds or stochastic claims. The fourth section is now
"Further applications," with parallel subsections for Laplace-transformed
dynamics and chemical reaction networks. The abstract and introduction reflect
both applications. For the earlier edge-removal formulation, an independent
in-memory check of the activity decomposition, the homogeneous relation,
and scalar current formula covered 900 rate pairs
on 60 random networks, with maximum residual approximately `6.88e-15`.
The finite-response formulation was checked on 400 rate changes in 40
mass-action networks of the form `2 A_i <-> 2 A_j`, with fixed total species
concentration, including 20 chains and 20 cycles. The activity-response,
homogeneous-relation, and probability-limit checks had numerical errors
below `5.22e-15`.

The closing literature paragraph in "Exact stationary response" distinguishes
the use of the Drazin inverse for response derivatives from its use for finite
changes. It briefly cites
[Baiesi, Maes, and Netocny, J. Stat. Phys. 135, 57-75 (2009)](https://doi.org/10.1007/s10955-009-9723-3)
for current-cumulant calculations: their Eqs. (16)-(17) express covariances
using the Drazin inverse, and higher cumulants follow from their perturbation
expansion. This attribution does not identify their counting-field calculation
with the physical-response factorization in the later FRRs.
[Mandal and Jarzynski, J. Stat. Mech. 2016, 063204](https://doi.org/10.1088/1742-5468/2016/06/063204)
is cited for expansions under slow driving; their Eqs. (11)-(13) define the
same generalized inverse and give the leading lag `p - pi = G dot(pi)`.
The paragraph also cites the two fluctuation-response papers by Ptaszynski, Aslyamov,
and Esposito: [state observables, PRE 113, 024130 (2026)](https://doi.org/10.1103/r1qk-76gc)
and [state-current correlations, PRE 113, 024131 (2026)](https://doi.org/10.1103/4htr-dfc5).
Their Drazin response identities appear in
[Eq. (11)](https://arxiv.org/html/2412.10233) and
[Eq. (16)](https://arxiv.org/html/2506.08877), respectively.
The requested Ising-model reference is
[Ptaszynski and Esposito, PRE 111, 034125 (2025)](https://doi.org/10.1103/PhysRevE.111.034125):
[Section III.2, Eq. (35)](https://arxiv.org/html/2411.19643v3) derives response
derivatives recursively using the Drazin inverse. For finite changes,
[Bao and Liang, arXiv:2412.19602v6](https://arxiv.org/html/2412.19602v6),
Supplemental Material I, Eq. (S5), explicitly gives the same finite-response
identity as this note. The bibliography uses their revised 2026 title,
"Nonlinear Response Identities and Bounds for Nonequilibrium Steady States."
The first version appeared in 2024 under a different title.
The inline connection to mean first-passage times uses the column-generator
convention: `tau_(j->i) = (G_ij - G_ii) / pi_i`, with zero passage time when
starting at the target. This is Bao and Liang's Eq. (S2); their Eqs. (S5)--(S9)
convert the Drazin finite-response identity to its passage-time form.
At the user's request, the MFPT sentence also cites
[Cho and Meyer, LAA 316, 21-28 (2000)](https://doi.org/10.1016/S0024-3795(99)00263-3),
"Markov chain sensitivity measured by mean first passage times."
Publication metadata and the scope of its sensitivity bounds were verified
on the publisher's page. The manuscript now says "response formulas and
bounds" to reflect that scope.
The paragraph also cites Harvey et al., Eq. (44), for linear response in
passage times, and Khodabandehlou, Maes, and Netocny, Eq. (III.1), for finite
changes. It does not attribute the finite-change formula to Harvey et al.
The alternative formulations are
[Aslyamov and Esposito, PRL 132, 037101 (2024)](https://doi.org/10.1103/PhysRevLett.132.037101)
and [PRL 133, 107103 (2024)](https://doi.org/10.1103/PhysRevLett.133.107103).
They incorporate normalization to obtain invertible matrices from the rate
matrix; the second paper's matrix approach and Supplemental Material A give
the reduced and row-replacement constructions. "Invertible" is the intended
algebraic property here; "reversible" would refer to a different property of
the Markov dynamics.

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
  integrate to a global affine relation. The added chemical-network application
  concerns complex activities under complex balance, rather than a general
  affine relation between species concentrations.

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

- [Polettini, Harunari, Dal Cengio, and Lecomte, Lett. Math. Phys. 116, 1 (2026)](https://doi.org/10.1007/s11005-025-02026-8),
  "Coplanarity of rooted spanning-tree vectors," is included in the existing
  mutual-linearity citation groups. The publisher's abstract identifies an
  alternative spanning-tree derivation of stationary current mutual linearity
  and an extension to two pairs of edges. The bibliography follows the
  journal's 2026 volume year, although the online publication date was
  5 December 2025. No additional tree identities are claimed in the note.
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
  bibliography metadata checked on APS. Equation (44) gives linear response
  in terms of mean first-passage times. The manuscript cites it alongside
  the finite-response formulations of Khodabandehlou et al. and Bao and Liang,
  without making a priority claim.

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
