# 4. Collatz Conjecture (3n+1 Problem)

> **Field:** Number Theory / Dynamical Systems · **Status:** Open (as of 2026) · **Prize:** none (though various informal bounties exist)

## Statement

Define a function on positive integers:
- if `n` is even, `n → n/2`;
- if `n` is odd, `n → 3n + 1`.

**Conjecture:** starting from *any* positive integer and iterating, you always eventually reach **1** (entering the cycle 4 → 2 → 1).

## Why it matters

It is the most famous "anyone can understand it, nobody can solve it" problem. Paul Erdős reportedly said: *"Mathematics may not be ready for such problems."* It sits at the crossroads of number theory, ergodic theory, and computability, and resists every standard technique.

## History

- Attributed to **Lothar Collatz**, c. 1937. Also known as the 3n+1 problem, Ulam conjecture, Kakutani's problem, Syracuse problem.

## State of the art

- **Computational:** verified for all starting values up to roughly 2⁶⁸ (all reach 1).
- **Terras (1976):** almost all integers (density 1) eventually drop below their starting value.
- **Tao (2019):** proved that *almost all* Collatz orbits attain *almost bounded* values — the strongest general result to date. It is a striking near-miss, but does **not** prove the full conjecture (it allows a density-zero set of possible exceptions).
- No non-trivial cycle is known, and none exists below very large bounds, but the general statement is unproven.

## Common pitfalls for "solvers"

- Verifying huge ranges of `n` proves nothing about *all* `n`.
- "Statistical" heuristics (each odd step multiplies by ~3/2, each even step halves, net shrink) *suggest* the conjecture but are **not** a proof — they ignore correlations between steps.
- Generalizations of Collatz are known to be **undecidable** (Conway), a strong warning that elementary arguments are unlikely to suffice.

## References

- J. C. Lagarias (ed.), *The Ultimate Challenge: The 3x+1 Problem* (AMS, 2010).
- T. Tao, *Almost all orbits of the Collatz map attain almost bounded values* (2019), [arXiv:1909.03562](https://arxiv.org/abs/1909.03562).

## Approaches in this repo

*None yet. Note: this problem attracts more flawed "proofs" than any other on the list — please read [CONTRIBUTING.md](../CONTRIBUTING.md) before submitting.*
