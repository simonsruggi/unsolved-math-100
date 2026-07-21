# 95. P versus NP

> **Field:** Theoretical Computer Science · **Status:** Open (as of 2026) · **Prize:** Clay Millennium ($1,000,000)

## Statement

- **P** is the class of decision problems solvable by a deterministic algorithm in polynomial time.
- **NP** is the class of decision problems whose "yes" answers can be *verified* in polynomial time given a certificate.

Clearly `P ⊆ NP`. The question:

> Does **P = NP**? I.e., is every problem whose solution can be efficiently *checked* also efficiently *solvable*?

The overwhelming consensus conjecture is **P ≠ NP**, but there is no proof.

## Why it matters

If `P = NP`, thousands of important problems (routing, scheduling, protein folding heuristics, theorem proving, and — alarmingly — breaking much of modern cryptography) would have efficient algorithms. If `P ≠ NP` (as believed), it certifies that some problems are inherently hard. Either way it reshapes computer science, mathematics, and cryptography.

## History

- Formulated by **Stephen Cook** (1971) and independently **Leonid Levin**; Cook proved SAT is NP-complete.
- **Richard Karp** (1972) showed 21 natural problems are NP-complete.
- Named a Clay Millennium Problem in 2000.

## State of the art

- **NP-completeness:** thousands of problems are known NP-complete; solving *any one* in polynomial time would collapse `P = NP`.
- **Barriers (why it's hard to prove):**
  - *Relativization* (Baker–Gill–Solovay, 1975): the question has different answers relative to different oracles, so oracle-based diagonalization can't settle it.
  - *Natural proofs* (Razborov–Rudich, 1994): a broad class of circuit-lower-bound techniques cannot work if strong one-way functions exist.
  - *Algebrization* (Aaronson–Wigderson, 2008): extends the relativization barrier to algebraic techniques.
- Circuit lower bounds strong enough to separate P from NP remain out of reach.

## Common pitfalls for "solvers"

- Any proof must **overcome the three barriers above** — a purported proof that doesn't even address them is almost certainly flawed.
- "I found a fast algorithm for [NP-complete problem]" claims must survive adversarial testing; historically all have failed on some instance.

## References

- S. Cook, *The complexity of theorem-proving procedures* (1971).
- Clay Mathematics Institute, [Official problem description](https://www.claymath.org/millennium/p-vs-np/).
- Aaronson, *P =? NP* survey (2017), [ECCC / arXiv](https://www.scottaaronson.com/papers/pnp.pdf).

## Approaches in this repo

*None yet. See [CONTRIBUTING.md](../CONTRIBUTING.md) — and please address the known barriers.*
