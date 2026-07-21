# 88. Navier–Stokes Existence and Smoothness

> **Field:** Partial Differential Equations / Fluid Dynamics · **Status:** Open (as of 2026) · **Prize:** Clay Millennium ($1,000,000)

## Statement

The incompressible Navier–Stokes equations describe the motion of a viscous fluid. For 3D flow with smooth, rapidly decaying initial data, the Millennium Problem asks to prove **one** of:

- **(Existence & smoothness)** smooth solutions exist for all time and remain smooth and finite-energy; **or**
- **(Breakdown)** there exist smooth initial data whose solution develops a singularity ("blow-up") in finite time.

In other words: do the 3D equations always have well-behaved solutions, or can a fluid spontaneously form a singularity?

## Why it matters

Turbulence, weather, aerodynamics — all governed by these equations. We *use* them constantly yet cannot prove their solutions behave well. It is the flagship open problem of nonlinear PDE.

## History

- Equations formulated by Navier (1822) and Stokes (1845).
- **Leray (1934):** constructed global *weak* solutions and introduced key concepts, but weak solutions are not known to be unique or smooth.
- Named a Clay Millennium Problem in 2000 (official statement by Charles Fefferman).

## State of the art

- **2D:** existence and smoothness are **known** (proven). The difficulty is genuinely 3D.
- **3D local existence:** smooth solutions exist for a *short* time; the open question is whether they can be continued globally.
- **Partial regularity (Caffarelli–Kohn–Nirenberg, 1982):** the singular set of a suitable weak solution has parabolic Hausdorff measure zero.
- **Conditional regularity:** many criteria (e.g. Ladyzhenskaya–Prodi–Serrin) guarantee smoothness *if* certain norms stay bounded — but boundedness itself is unproven.
- **Tao (2016):** demonstrated finite-time blow-up for an *averaged* / modified Navier–Stokes system, suggesting purely energy-based methods cannot rule out blow-up ("supercriticality barrier").

## Common pitfalls for "solvers"

- Energy estimates are *supercritical* in 3D — the scaling means naive a priori bounds don't close. Any solution must confront this.
- A construction must respect incompressibility and finite energy; many attempted blow-up examples secretly violate these.

## References

- C. Fefferman, [Official problem statement](https://www.claymath.org/millennium/navier-stokes-equation/) (Clay Mathematics Institute).
- L. Caffarelli, R. Kohn, L. Nirenberg, *Partial regularity of suitable weak solutions* (1982).
- T. Tao, *Finite time blowup for an averaged three-dimensional Navier–Stokes equation* (2016), [arXiv:1402.0290](https://arxiv.org/abs/1402.0290).

## Approaches in this repo

*None yet. See [CONTRIBUTING.md](../CONTRIBUTING.md).*
