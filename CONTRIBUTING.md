# Contributing

Thank you for wanting to contribute! This project only works if contributions are **rigorous and honest**. Please read this fully.

## The golden rules

1. **Separate proven from conjectured.** Every claim must be clearly labeled: *proven* (with a reference or a complete argument), *conjectured*, *heuristic*, or *computational evidence*.
2. **Cite your sources.** Papers, preprints (arXiv), textbooks, OEIS entries, Wikipedia — link them.
3. **Be humble about "solutions."** See below.
4. **Be kind.** See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Ways to contribute

### 1. Improve a problem page (easiest, most valuable)
Add or expand a file in `problems/`, named `NNN-slug.md` (e.g. `004-collatz-conjecture.md`), using [`problems/_TEMPLATE.md`](problems/_TEMPLATE.md). Include statement, history, known partial results, and references. Open a PR.

### 2. Report a solved / disproven problem
If a listed problem has been resolved, open a PR that:
- updates the entry in `README.md` and its `problems/` page,
- cites a **peer-reviewed publication** or a preprint that has gained broad expert acceptance.

### 3. Propose an approach
Add a file under `approaches/NNN-problem-slug/your-idea.md`, or open an issue using the "New approach" template. An approach can be:
- a reformulation or reduction to another problem,
- a heuristic or probabilistic argument,
- computational experiments (share code/data),
- a partial result under extra hypotheses,
- a promising angle with a clear explanation of where it gets stuck.

## About submitting a "full solution"

We love ambition. We also love mathematics too much to pretend a GitHub merge validates a proof.

**Please understand:** a genuine solution to any problem on this list would be one of the most significant mathematical events of the decade. The correct venue for it is a peer-reviewed journal and the scrutiny of domain experts — not a pull request. History is full of sincere, confident, and *wrong* proofs of these exact problems; even brilliant mathematicians have published flawed attempts.

So, if you believe you have a solution:

- **First, try to break it yourself.** Where is the weakest step? Have you checked small cases computationally?
- **State every assumption explicitly.** A single unjustified "clearly" is usually where these arguments fail.
- **Submit it as an *approach*, not a "solution."** Frame it as "here is an argument; here is what I can and cannot justify." That is honest, useful, and respected.
- Consider posting to arXiv (needs endorsement) or forums like MathOverflow for expert eyes.

Pull requests claiming a complete proof will be treated as **approaches** and reviewed on their mathematical content. Low-effort or unfalsifiable "I solved it" submissions will be closed politely.

## Style

- Use LaTeX-style math in backticks or `$...$` where GitHub renders it; keep statements precise.
- Keep prose accessible: a motivated undergraduate should grasp the *statement* even if not the frontier.
- One problem/approach per PR when possible.

## Review

Maintainers and community reviewers check for: correct labeling (proven vs. conjectured), valid references, mathematical soundness of claims, and tone. We may ask questions before merging — that's normal and collaborative, not a rejection.
