# 81. Jacobian Conjecture

> **Field:** Algebraic Geometry / Commutative Algebra · **Status:** ⚡ **DISPROVEN for n > 2 (July 2026)** — open for n = 2 · **Prize:** none (Smale's Problem #16)

## Statement

Let `F : ℂⁿ → ℂⁿ` be a polynomial map (each coordinate is a polynomial). The **Jacobian Conjecture (Keller, 1939)** asserts:

> If the Jacobian determinant `det(JF)` is a **nonzero constant**, then `F` is invertible and its inverse is also polynomial.

The constant-nonzero-Jacobian condition is *necessary* (it holds for any polynomial automorphism). The conjecture claimed it was also *sufficient*.

## Why it matters

Deceptively elementary to state, it resisted proof for 87 years and connects algebraic geometry, dynamical systems, and even quantum field theory / operator algebras (it is equivalent to the Dixmier Conjecture, #82, in a suitable sense). It is **Problem #16 on Stephen Smale's list** of problems for the 21st century. Famously, it accumulated **at least five published but incorrect proofs** — a textbook cautionary tale.

## History

- **1939** — Ott-Heinrich Keller poses the conjecture (for `n = 2`, ℤ-coefficients).
- **Decades of attempts** — many false proofs; reductions show it suffices to treat maps of the form `x + (degree-3 homogeneous)` in all dimensions (Bass–Connell–Wright, Yagzhev).
- **2016** — Tao demonstrated finite-time blow-up for an *averaged* Navier–Stokes, unrelated but a reminder that "supercritical"-feeling problems resist energy methods.
- **19–20 July 2026** — ⚡ **Levent Alpöge** (mathematician, Anthropic) announces an explicit **counterexample in ℂ³**, found with the assistance of **Claude Fable 5**. The strategy: don't prove it — *construct a counterexample*.

## The counterexample (n = 3)

Define `F = (a, b, c) : ℂ³ → ℂ³` by:

```
a = (1 + xy)³·z + y²(1 + xy)(4 + 3xy)
b = y + 3x(1 + xy)²·z + 3xy²(4 + 3xy)
c = 2x − 3x²y − x³z
```

**Properties:**
- `det(JF) = −2` — a nonzero constant, so `F` satisfies the conjecture's hypothesis.
- `F` is **not injective**: the three *distinct* points
  `(0, 0, −1/4)`, `(1, −3/2, 13/2)`, `(−1, 3/2, 13/2)`
  all map to the single point `(−1/4, 0, 0)`.

A map with a polynomial inverse would be a bijection, so non-injectivity is fatal. Hence the conjecture is **false for n = 3**, and by padding with identity coordinates (`x₄ ↦ x₄`, …) it is **false for every n ≥ 3**.

**The n = 2 case remains open.** (Padding lowers dimension the wrong way; it cannot produce a 2-D counterexample.)

## Verify it yourself

You don't have to trust the announcement — or the AI. The counterexample is a finite algebraic object. Run:

```bash
python3 scripts/verify_081_jacobian.py
```

(Script included in this repo.) It symbolically computes `det(JF) = −2` and confirms the three points collapse to `(−1/4, 0, 0)`. You can also paste the map into Wolfram Alpha / SageMath.

## Why "counterexample, not proof" matters

This is the model behavior this whole repo advocates: a *disproof by explicit construction* is **cheaply and independently checkable**, unlike a 100-page proof. The result stands or falls on arithmetic anyone can redo — which is why it was verified within hours of the announcement.

## Caveat on status

As of writing, this is a widely-verified **announcement / preprint**, not yet a formally refereed journal publication. Given that the object is fully explicit and machine-checkable, confidence is high — but if you have an updated citation (journal acceptance, formalization in Lean/Coq), please open a PR.

## References

- O.-H. Keller, *Ganze Cremona-Transformationen* (1939).
- H. Bass, E. Connell, D. Wright, *The Jacobian conjecture: reduction of degree and formal expansion of the inverse* (1982).
- L. Alpöge, announcement thread (July 2026) and verification preprint.
- [Jacobian conjecture — Wikipedia](https://en.wikipedia.org/wiki/Jacobian_conjecture)
- [Secret Blogging Seminar — The new counterexample to the Jacobian conjecture (2026)](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/)
- [Wolfram MathWorld — Jacobian Conjecture](https://mathworld.wolfram.com/JacobianConjecture.html)

## Approaches in this repo

Resolved for n ≥ 3. **The n = 2 case is still open** — approaches for two variables are welcome under `approaches/081-jacobian-conjecture/`.
