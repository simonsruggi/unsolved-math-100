# 3. Twin Prime Conjecture

> **Field:** Number Theory · **Status:** Open (as of 2026) · **Prize:** none

## Statement

> There are infinitely many primes `p` such that `p + 2` is also prime.

Examples of twin primes: (3, 5), (5, 7), (11, 13), (17, 19), (29, 31), …

## Why it matters

A special case of Polignac's conjecture (#18) and the Hardy–Littlewood k-tuple conjecture (#31). The recent breakthroughs on it revolutionized analytic number theory and sieve methods.

## History

- Implicit since antiquity; named and studied systematically from the 19th–20th centuries (de Polignac, Hardy–Littlewood).

## State of the art — a dramatic decade

- **Zhang (2013):** proved there exists a *finite* gap `H` such that infinitely many prime pairs differ by at most `H` — the first bound of its kind (Zhang's original `H` was about 70,000,000). This was a landmark: it proved *bounded gaps between primes* exist.
- **Polymath8 + Maynard (2013–2014):** independent methods (Maynard's "multidimensional sieve") lowered the bound dramatically to **246**: infinitely many prime pairs differ by at most 246.
- Under the Elliott–Halberstam conjecture (#29), the bound improves to **6**.
- The full conjecture (gap exactly **2**, infinitely often) remains **open** — the parity barrier blocks current sieves from reaching 2.

## Common pitfalls for "solvers"

- The bound-246 result is *not* the twin prime conjecture; closing 246 → 2 is the hard, open part.
- Heuristic densities (Hardy–Littlewood predict ~`C·x/(log x)²` twin primes up to x) match data beautifully but are not proofs.

## References

- Y. Zhang, *Bounded gaps between primes*, Annals of Mathematics (2014).
- J. Maynard, *Small gaps between primes*, Annals of Mathematics (2015), [arXiv:1311.4600](https://arxiv.org/abs/1311.4600).

## Approaches in this repo

*None yet. See [CONTRIBUTING.md](../CONTRIBUTING.md).*
