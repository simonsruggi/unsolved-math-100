#!/usr/bin/env python3
"""
Verify the July 2026 counterexample to the Jacobian Conjecture (problem #81).

The conjecture (Keller, 1939): a polynomial map F: C^n -> C^n with constant
nonzero Jacobian determinant is invertible (hence bijective).

This script checks Alpoge's C^3 counterexample (found with Claude Fable 5):
  1. det(JF) is the nonzero constant -2  -> hypothesis satisfied.
  2. Three DISTINCT points map to the same image -> F is not injective
     -> F cannot be a bijection -> the conjecture is FALSE for n >= 3.

Requires: sympy  (pip install sympy)
"""
import sympy as sp


def main():
    x, y, z = sp.symbols("x y z")

    a = (1 + x * y) ** 3 * z + y ** 2 * (1 + x * y) * (4 + 3 * x * y)
    b = y + 3 * x * (1 + x * y) ** 2 * z + 3 * x * y ** 2 * (4 + 3 * x * y)
    c = 2 * x - 3 * x ** 2 * y - x ** 3 * z
    F = sp.Matrix([a, b, c])

    det = sp.expand(F.jacobian([x, y, z]).det())
    print(f"Jacobian determinant: {det}")
    assert det == -2, "expected constant Jacobian determinant -2"

    points = [
        (sp.Integer(0), sp.Integer(0), sp.Rational(-1, 4)),
        (sp.Integer(1), sp.Rational(-3, 2), sp.Rational(13, 2)),
        (sp.Integer(-1), sp.Rational(3, 2), sp.Rational(13, 2)),
    ]
    images = []
    for p in points:
        sub = {x: p[0], y: p[1], z: p[2]}
        img = tuple(sp.simplify(comp.subs(sub)) for comp in (a, b, c))
        images.append(img)
        print(f"F{p} = {img}")

    assert len(set(points)) == 3, "points must be distinct"
    assert all(img == images[0] for img in images), "images must coincide"

    print("\nOK: constant nonzero Jacobian (-2) but 3 distinct points share one image.")
    print("=> F is not injective => Jacobian Conjecture is FALSE for n >= 3.")
    print("   (The n = 2 case remains open.)")


if __name__ == "__main__":
    main()
