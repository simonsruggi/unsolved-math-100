# 1. Riemann Hypothesis

> **Field:** Analytic Number Theory · **Status:** Open (as of 2026) · **Prize:** Clay Millennium ($1,000,000)

## Statement

The Riemann zeta function is defined for `Re(s) > 1` by
`ζ(s) = Σ 1/nˢ` and extended by analytic continuation to the whole complex plane (except a simple pole at `s = 1`).

It has "trivial" zeros at the negative even integers `−2, −4, −6, …`. The **Riemann Hypothesis (RH)** asserts:

> Every *non-trivial* zero of ζ(s) has real part exactly **½**.

Equivalently, all non-trivial zeros lie on the "critical line" `Re(s) = ½`.

## Why it matters

RH is the deepest known statement about the distribution of prime numbers. It is equivalent to a sharp error bound in the Prime Number Theorem:
`π(x) = Li(x) + O(√x · log x)`. Hundreds of theorems in number theory are proved *conditionally on RH*; a proof would instantly upgrade all of them. Its generalizations (GRH, Grand RH) underpin vast areas of arithmetic.

## History

- **1859** — Bernhard Riemann states the hypothesis in his only paper on number theory.
- **1900** — Featured as part of Hilbert's 8th problem.
- **2000** — Named a Clay Millennium Prize Problem.

## State of the art

- **Proven:** infinitely many zeros lie *on* the critical line (Hardy, 1914). More than 40% of non-trivial zeros are known to lie on the line (Conrey and successors).
- **Computational:** the first several trillion non-trivial zeros have all been verified to lie exactly on the critical line. (Verification of cases proves nothing in general — infinitely many remain.)
- **Zero-free regions:** classical results give zero-free regions near `Re(s) = 1`, enough for the Prime Number Theorem, but far from the critical line.
- The analogue of RH for varieties over finite fields (the Weil conjectures) **is** proven (Deligne, 1974) — but the original RH is not.

## Common pitfalls for "solvers"

- Numerical verification of many zeros does **not** prove RH.
- Elementary "proofs" almost always mishandle the analytic continuation or the functional equation.

## References

- B. Riemann, *Über die Anzahl der Primzahlen unter einer gegebenen Größe* (1859).
- Clay Mathematics Institute, [Official problem description](https://www.claymath.org/millennium/riemann-hypothesis/).
- H. M. Edwards, *Riemann's Zeta Function* (1974).

## Approaches in this repo

*None yet — be the first (responsibly!). See [CONTRIBUTING.md](../CONTRIBUTING.md).*
