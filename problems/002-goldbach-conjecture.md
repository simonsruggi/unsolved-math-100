# 2. Goldbach's Conjecture

> **Field:** Number Theory · **Status:** Open (as of 2026) · **Prize:** none

## Statement

**Strong Goldbach Conjecture:** every even integer greater than 2 can be written as the sum of two primes (e.g. 4 = 2+2, 100 = 3+97).

The related **weak (ternary) Goldbach conjecture** — every odd number greater than 5 is a sum of three primes — was **proven by Harald Helfgott in 2013**. The *strong* (binary) form remains open.

## Why it matters

One of the oldest unsolved problems in mathematics, and a benchmark for additive prime number theory. Progress on it has driven the development of the circle method and sieve theory.

## History

- **1742** — Christian Goldbach, in a letter to Euler.
- **2013** — Helfgott proves the weak form (building on Vinogradov's 1937 result for large odd numbers).

## State of the art

- **Computational:** verified for all even numbers up to about 4 × 10¹⁸.
- **Chen's theorem (1973):** every sufficiently large even number is the sum of a prime and a *semiprime* (a product of at most two primes) — the closest structural result.
- **Vinogradov (1937):** every sufficiently large odd number is a sum of three primes (the seed of the weak-form proof).
- **Estermann / others:** almost all even numbers are sums of two primes (density-1 result).

## Common pitfalls for "solvers"

- The weak form being proven does **not** imply the strong form.
- Sieve methods have a known "parity problem" barrier that blocks naive routes to the exact statement.

## References

- Goldbach–Euler correspondence (1742).
- H. Helfgott, *The ternary Goldbach conjecture is true* (2013), [arXiv:1312.7748](https://arxiv.org/abs/1312.7748).

## Approaches in this repo

*None yet. See [CONTRIBUTING.md](../CONTRIBUTING.md).*
