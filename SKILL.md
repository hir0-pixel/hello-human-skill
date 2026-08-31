---
name: hello-human
description: Write human-like prose that avoids AI tells at surface, syntax, and structural levels. Use when the user asks for human-sounding writing, anti-AI copy, natural emails, blogs, essays, texts, or marketing copy. Triggers include "Hello Human", "write like a human", "humanize", "don't sound like ChatGPT/Grok/Claude", or passing AI detectors authentically. Built from Wikipedia AISIGNS, StoryScope, tropes.fyi, and academic detection research.
---

# Hello Human

Write like a specific person with something at stake — not like a model clearing RLHF.

**Install:** `~/.cursor/skills/`, `~/.claude/skills/`, or `~/.agents/skills/`

**Council sources:** Wikipedia AISIGNS, StoryScope (shape of AI writing), tropes.fyi (49 tropes), Kobak/PNAS/Stanford papers, community consensus.

## Five-pass workflow

```
- [ ] 0. Substance — real facts, no invented stats; rewrite don't mask (Wikipedia fix model)
- [ ] 1. Shape — narrative geometry, not just words (StoryScope pass)
- [ ] 2. Tropes — 49-pattern density audit (tropes.fyi pass)
- [ ] 3. Syntax — nominalizations, participial openers, copulatives (academic pass)
- [ ] 4. Soul — burstiness, stance, specifics, human markers
- [ ] 5. Genre — email/blog/copy/essay rules
- [ ] 6. Cluster audit — 3+ tell categories in 200 words → rewrite
- [ ] 7. Detector — scripts/score.py, target ≤0.40, min 300 words
- [ ] 8. Revise from flags; max 3 loops
```

## Pass 0 — Substance (Wikipedia)

Before polishing prose:

1. **Rewrite from notes**, not from AI draft (masking tells hides problems).
2. **Verify claims.** Use `[ADD SOURCE]` if unsure.
3. **Fix meaning first** — puffery, hallucinated citations, promotional tone are the disease; em dashes are symptoms.

See [references/wikipedia-aisigns.md](references/wikipedia-aisigns.md) § Fix philosophy.

## Pass 1 — Shape (StoryScope)

AI writing has **geometry**: tidy single-track arguments, explicit themes, linear time, neat closure. Style edits fool weak detectors; structure edits don't.

**Break the shape:** withhold the moral, inject a tangent, name something specific, cut signposts, leave one open loop, end without summary.

Full checklist: [references/storyscope.md](references/storyscope.md) § Practical checklist.

## Pass 2 — Tropes (tropes.fyi)

Run tell-density audit on [references/tropes.md](references/tropes.md).

**Hard caps:** ≤1 negative parallelism per piece; ≤1 tricolon; ≤2 em-dashes per 500 words.

Priority kills: negative parallelism, fractal summaries, reasoning leak, preamble, delve family, grandiose stakes, compulsive counting.

**Rule:** 4+ tropes in 500 words → rewrite from notes, not AI draft. No synonym spinners.

## Pass 3 — Syntax (academic)

- Verbs over nominalizations ("we evaluated" not "conducted an evaluation")
- Kill participial openers ("Leveraging X, we…")
- Split stacked noun phrases; name the actor
- Passive is fine when the actor is unknown — don't force active voice everywhere
- Plain copulatives: is/has/was
- Add genuine epistemic markers: maybe, I think, probably
- One register, committed
- Record the author's stance before editing; check every revised claim against it

See [references/academic.md](references/academic.md) for 21 focal words.

## Pass 4 — Soul + burstiness

- Mix 3-word and 30+ word sentences
- Specific numbers, names, dates — or honest placeholders
- Opinion someone could disagree with
- Contractions in casual register
- One flat/bored paragraph (especially after Grok edgy mode)
- No chatbot closers

## Pass 5 — Genre

[references/genres.md](references/genres.md)

## Pass 6 — Cluster audit

Count tell **categories** hit in any 200-word block (not individual words):

| Category | Examples |
|----------|----------|
| Kill-list vocab | delve, landscape, pivotal, underscore |
| Parallelism | not X but Y, not X not Y just Z |
| Signpost filler | additionally, furthermore, it's worth noting |
| Copulative dodge | serves as, stands as, boasts |
| Meta/summary | in conclusion, let's dive in, fractal recap |
| Shape | explicit theme, no side thread, all paragraphs same job |

**3+ categories → rewrite block.**

## Pass 7 — Detector

```bash
pip install lmscan
python scripts/score.py --file draft.txt
python tests/run_tests.py
```

Threshold: `ai_probability ≤ 0.40`. ≥300 words for reliable scores. Uses [lmscan](https://github.com/stef41/lmscan) — a free offline Python heuristic (burstiness, slop-word density, LLM vocab fingerprints). Not GPTZero/Turnitin; scores screen drafts in the revise loop, they don't prove authorship. Optional: Sapling/GPTZero API for a second opinion.

## Pass 8 — Revise order

1. Shape (structure)
2. Trope cluster
3. Kill-list + syntax (focal words when ornamental, not by default)
4. Burstiness
5. Re-score

Do not synonym-swap. Max 3 loops. Cluster = 3+ independent tell categories in ~200 words, not one isolated tell.

## Model tells

| Model | Shape + surface + leakage |
|-------|---------------------------|
| ChatGPT/GPT | Additionally, delve, rule-of-three, era vocab; `:contentReference`, `turn0search0` |
| Claude | Markdown default, reasoning leak, bold-first bullets; more em dashes than pros |
| Grok | causal/empirical/correlate, "X rather than Y"; `grok_card`, `referrer=grok.com` |
| Gemini | facilitate, comprehensive; `[cite: 1]` markers |
| DeepSeek | Curly quotes; lenticular citation brackets |
| Perplexity | `[attached_file:1]`, `ppl-ai-file-upload` URLs |

Strip paste artifacts before publishing. See [wikipedia-aisigns.md](references/wikipedia-aisigns.md) § LLM-specific.

## Never do

- Humanizer spinners (synonym swap)
- Mask tells without fixing substance
- Typos as fake voice
- Parentheses to dodge em dashes
- "Make this undetectable" prompting

## References

| File | Content |
|------|---------|
| [wikipedia-aisigns.md](references/wikipedia-aisigns.md) | Full Wikipedia pattern catalog + fix philosophy |
| [storyscope.md](references/storyscope.md) | Shape of AI writing / narrative geometry |
| [tropes.md](references/tropes.md) | 49 tropes from tropes.fyi |
| [academic.md](references/academic.md) | 21 focal words, PNAS syntax, detection science |
| [patterns.md](references/patterns.md) | Master quick-reference |
| [genres.md](references/genres.md) | Genre guides |
| [sources.md](references/sources.md) | Full bibliography |

## Validated samples

16 genre pairs (email, blog, essay, LinkedIn, marketing, casual text, Grok-style, academic). AI samples score ~0.69–0.85; humanized samples ~0.14–0.24 (lmscan, threshold ≤0.40). Run `python tests/run_tests.py` after changes. Regenerate fixtures with `tests/_write_samples.py` if you edit sample text.
