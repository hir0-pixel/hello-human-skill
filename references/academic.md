# Academic Research — Writing Rules

Sources: Juzek & Ward ([arXiv 2412.11385](https://arxiv.org/abs/2412.11385)), Kobak et al. ([Science Advances 2025](https://doi.org/10.1126/sciadv.adt3813)), Reinhart et al. ([PNAS 2025](https://doi.org/10.1073/pnas.2422455122)), Liang et al. ([Patterns 2023](https://doi.org/10.1016/j.patter.2023.100779)), [How LLMs Distort Language](https://arxiv.org/abs/2603.18161) (2026).

## 21 focal words (Juzek & Ward)

Inflections count separately. Kobak et al. identified 900 excess words broadly; this is the core focal set.

| Focal word | Plain replacement |
|------------|-------------------|
| advancements | advances, improvements |
| aligns | matches, agrees with |
| boasts | has, includes |
| comprehending | understanding |
| delve | examine, study |
| delved | examined, studied |
| delves | examines, studies |
| delving | examining, studying |
| emphasizing | showing, stressing |
| garnered | received, gained |
| groundbreaking | new; state the actual novelty |
| intricate | complex, detailed |
| intricacies | details, complexities |
| realm | field, area |
| showcases | shows |
| showcasing | showing |
| surpasses | exceeds, performs better than |
| surpassing | exceeding, performing better than |
| underscore | show, stress |
| underscores | shows, stresses |
| underscoring | showing, stressing |

**Rule:** Do not ban mechanically. Replace when they add prestige without information. Prefer the exact action, comparison, or result.

**Excess spikes (Kobak 2025):** delves (r=28), underscores (r=13.8), showcasing (r=10.7) — style words, not content words.

---

## Syntax rules (PNAS 2025 / Biber)

Instruction-tuned models favor informationally dense, noun-heavy prose.

| AI overuse | Fix |
|------------|-----|
| Present-participial clauses (2–5×) | "We used the survey and found gaps" not "Using the survey, revealing several gaps…" |
| Nominalizations (1.5–2×) | "we evaluated" not "we conducted an evaluation" |
| Abstract *that*-clause subjects (2.6× GPT-4o) | "The policy's failure shows…" not "That the policy failed demonstrates…" |
| Phrasal coordination stacks (1.9×) | Split "design, implementation, evaluation, and optimization of…" into named actions |
| Agentless passive underuse | Name actor when known — but **passive is not inherently AI** when actor is unknown |

Also:
- **Match genre** — conversation, reporting, fiction, scholarship should not share one polished house style
- **Vary structure naturally** — don't manufacture short-long alternation; let evidence drive rhythm
- **Protect meaning during edits** — grammar-only AI edits can shift stance (arXiv 2603.18161). Record author's position first; verify every revised claim

---

## Root cause

Strongest account: **alignment-induced predictability**, not unusual depth.

Base models predict likely continuations. Instruction tuning and RLHF reward responses evaluators read as polished, helpful, complete, or scholarly. Words like *intricate*, *underscore*, *groundbreaking* become cheap quality signals. Repeated preference creates a narrow stylistic basin: safe vocabulary, dense noun phrases, balanced lists, neutral conclusions.

Juzek & Ward found no clear evidence architecture/algorithms/pretraining alone caused focal-word overuse. Llama base/chat comparison consistent with fine-tuning/RLHF contributing — but human-preference experiment was mixed.

**RLHF is the leading supported mechanism, not a proven sole cause.**

Also: register leveling (one voice all genres), homogenization toward statistical mean, local maximum of predictability (DetectGPT).

---

## Detection reality

**More likely to read as human:**
- Concrete names, dates, measurements, places, sensory details
- Clear stance including genuine uncertainty or disagreement
- Genre-appropriate syntax and uneven but purposeful rhythm
- Claims/examples that could belong only to this writer
- Revisions that preserve original meaning and voice

**More likely to be flagged:**
- Low-perplexity safe continuations
- Uniform sentence/paragraph structure
- Dense focal vocabulary, ornamental metaphors, promotional adjectives
- Forced tricolons, "not X but Y," tidy summary endings
- Neutralization of author position; abstractions replacing examples

| Study | Finding |
|-------|---------|
| Liang et al. 2023 | 61.2% avg FP on TOEFL essays; 97.8% flagged by ≥1 detector |
| Paraphrase evasion | Detectors drop sharply; synonym swap ≠ human voice |
| Style fine-tune | Some detectors 97% → 3% — surface fix fragile |
| StoryScope 2026 | ~93% from structure after style edits — shape fix durable |

Scores = screening signals, not authorship evidence. Never infer misconduct from score alone.

---

## Clustering rule

One tell is ordinary. Humans use em dashes, participial clauses, *delve*, parallel triples, summary phrases.

AI style is a **density problem**. Threshold: **3+ independent tells within a few hundred words:**

1. Focal vocabulary cluster
2. Formulaic contrast ("not X but Y")
3. Uniform rhythm
4. Promotional abstraction
5. Generic conclusions
6. Missing specifics
7. Excessive structural tidiness

A cluster justifies closer reading — not a verdict.

**Operational (Hello Human):** 0–1 categories in 200w = OK. 2 = revise. 3+ = rewrite from bullet notes.

**Useful question:** "How many predictable defaults replaced specific thought?"
