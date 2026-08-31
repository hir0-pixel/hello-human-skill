# Tropes.fyi — Complete Trope Checklist

Source: [tropes.fyi](https://tropes.fyi) (49 tropes + 10 behaviours, Ossama Chaib). One trope alone ≠ AI. **Density** is the tell.

## Anti-humanizer (read first)

Do **not** run synonym spinners (Quillbot-class tools). They keep low perplexity and read worse. arXiv 2026: >96% of "humanized" rewrites still game some detectors.

Do **not:** add typos, swap em-dashes for parentheses, pad word count, prompt "make undetectable."

**Do:** fix skeleton — burstiness, specifics, stance, shape. Re-prompt + manual edit beats spinners.

## Density caps (hard limits)

| Pattern | Cap per piece |
|---------|---------------|
| Negative parallelism | ≤1 |
| Tricolon / rule of three | ≤1 |
| Em dashes | ≤2 per 500 words |
| Signpost fillers (Additionally, Furthermore…) | ≤1 per 500 words |

**Audit:** 0–1 tropes in 500w = fine. 2–3 = tighten. 4+ = rewrite from notes.

---

## Sentence structure

| Trope | Fix |
|-------|-----|
| **Negative parallelism** ("It's not X — it's Y") | State Y. Highest-weight tell. |
| **"Not X. Not Y. Just Z."** | One affirmative sentence. |
| **Rule of three / tricolon** | Natural count. Never stacked tricolons. |
| **Anaphora** (same opener ×3+) | Vary subject; don't chant. |
| **"The X? A Y."** | Don't self-Q&A. Write the fact. |
| **False ranges** ("from X to Y") | Only if real scale. Else list. |
| **Comma-clipped tail** | Finish verb in same clause. |
| **"It's worth noting / Importantly / Notably"** | Delete wrapper; keep clause. |
| **Superficial -ing tails** | Cut tacked significance. |
| **Short punchy fragments** as own grafs | Merge; fragments only if you'd say them aloud. |
| **Excessive enumeration** ("The first… The second…") | Real list or real prose, not both. |
| **"Despite its challenges…"** | Name real problem or skip. Don't bounce to thrive. |

## Composition

| Trope | Fix |
|-------|-----|
| **Preamble** (announce-then-answer) | Lead with answer. Never restate prompt. |
| **Reasoning leak** | No voiceover of deciding/planning. Output only. |
| **Premise stacking** | Point first, evidence after. |
| **Fractal summaries** | No intro/mid/end recap at every heading. |
| **The Tie-Back** ("So, to answer your question…") | Stop when answer is done. |
| **Signposted conclusion** | No "In conclusion." Land and quit. |
| **Never-ending conclusion** | One closing beat. |
| **One-point dilution** | Say once with best example. |
| **Content duplication** | Delete repeated grafs. |
| **Belaboring the unnecessary** | Don't pre-defend uncontroversial claims. |
| **Self-echo** | Don't "pay off" your own earlier phrase. |
| **Rapid-fire historical analogies** | Drop Apple/Facebook/cloud litany. |
| **Listicle in a trench coat** | If it's a list, format as one. |

## Tone

| Trope | Fix |
|-------|-----|
| **Grandiose stakes** | Keep actual scale (API pricing ≠ civilization). |
| **False vulnerability** | Specific cost or skip. |
| **Quotable one-liners** | If it doesn't inform, cut. No slide bait. |
| **"Here's the kicker / thing / catch"** | No manufactured reveal. |
| **"Imagine a world where…"** | Start in the present. |
| **"Think of it as…"** | Analogy only if asked. |
| **Forced figurative language** | Cut similes that don't clarify. |
| **Vague attributions** | Name person/paper or drop claim. |
| **Appeal to familiarity** ("famously") | Prove it or don't claim consensus. |
| **Promotional language** | Describe; don't sell unless genre is ad. |
| **Invented concept labels** ("X paradox/trap") | Describe the thing plainly. |

## Formatting

| Trope | Fix |
|-------|-----|
| **Em-dash addiction** | Period/comma. Cap ~2/500w. No paren dodge. |
| **Bold-first bullets** | Prose, or bold only if rest is new info. |
| **Title case headings** | Sentence case. |
| **"Where / What / Why" headers** | Name section in nouns. |
| **Unicode decoration** | Straight quotes, `->` not `→`. No heading emoji. |
| **Colon as mid-sentence pivot** | Two sentences. Colon only before list. |

## Word choice

| Trope | Fix |
|-------|-----|
| **Delve family** | Ban: delve, leverage (v), harness, robust, utilize, streamline, certainly → *use / is / help* |
| **Quietly + magic adverbs** | Cut quietly, deeply, fundamentally, remarkably, arguably. |
| **Tapestry / landscape / ecosystem / paradigm** | Plain noun: field, set, setup. |
| **"Serves as / stands as / marks"** | is / has / was |
| **"Where it actually lives"** | Name the source. |
| **Synonym cycling** | One noun, repeat it. |
| **Kill-list extras** | additionally, furthermore, moreover, pivotal, foster, underscore, seamless, unlock, navigate, realm, "in today's fast-paced" |

## Behaviors

| Trope | Fix |
|-------|-----|
| **Compulsive counting** | Don't announce "five things." Just write them. |
| **Collaborative "we"** | Match author. Personal = I. Fake company we = tell. |
| **Pedagogical voice** | No "Let's break this down / unpack / dive in." |
| **Appease / over-expand** | Match ask's size. Don't manage feelings. |
| **Verify nobody asked** | Don't pull extra threads unprompted. |
| **Changelog-as-docs** | Docs aren't a diary of your process. |

## Burstiness (cross-cutting)

- After 20+ word sentence → one under 8 words
- Mix 3-word and 25+ word sentences
- Never three similar lengths in a row
- Plain copulas; verbs over nominalizations
- Kill participial openers ("Leveraging X, we…")

---

## Genre fixes

**Email:** Subject = ask. First line = why. One specific detail. Uneven grafs, contractions. Kill: "I hope this finds you well," "don't hesitate," symmetrical paragraphs, "Additionally," chatbot closer.

**Blog:** Open on claim, not "In today's world." One number or anecdote. Opinion someone can reject. End without recap. Kill: "Let's dive in," meta "this post will," tricolon subheads, "In conclusion."

**LinkedIn:** One concrete win or miss. Line breaks for rhythm. A stance. Kill: "thrilled to announce," "humbled and honored," emoji bullets, hashtag stacks.

**Marketing:** Outcome with number. Customer words. One CTA. Kill: revolutionize/game-changer/seamless, bold-label feature lists, stakes inflation. Proof or cut.

**Essay:** No thesis announcement. One side thread. Named source. Withhold moral in closing.

**Text/DM:** Fragments OK. No corporate vocabulary.
