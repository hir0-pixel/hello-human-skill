# AI Writing Patterns — Master Quick Reference

Consolidated index. Deep catalogs live in sibling files:

- [wikipedia-aisigns.md](wikipedia-aisigns.md) — full Wikipedia catalog + fix philosophy
- [storyscope.md](storyscope.md) — shape / narrative geometry
- [tropes.md](tropes.md) — 49 tropes.fyi patterns
- [academic.md](academic.md) — 21 focal words, PNAS syntax, detection science

## Three layers of AI writing

| Layer | What detectors catch | Fix |
|-------|---------------------|-----|
| **Surface** | Kill-list words, em dashes, transitions | Purge + tropes pass |
| **Syntax** | Participial openers, nominalizations, uniform length | Academic pass |
| **Shape** | Tidy arc, explicit theme, linear time, neat closure | StoryScope pass |

Fix order: **substance → shape → tropes → syntax → burstiness → detector.**

## Clustering rule

One tell ≠ AI. **Density across categories** in 200 words = signal. See SKILL.md Pass 6.

## Kill-list vocabulary

Ban or replace on sight:

```
additionally, align with, boasts, bolstered, comprehensive, crucial, delve,
delve into, ecosystem, elevate, emphasizing, enduring, enhance, facilitate,
foster, fostering, furthermore, garner, harness, highlight (verb), interplay,
intricate, intricacies, landscape (abstract), leverage, meticulous, moreover,
navigate (metaphor), nuanced, optimize, pivotal, realm, robust, seamless,
showcase, streamline, tapestry (abstract), testament, underscore (verb),
unlock, utilize, vibrant, delve, game-changer, revolutionary, cutting-edge,
transformative, unparalleled, invaluable, shed light on, it's important to note,
it's worth noting, in today's fast-paced, at the end of the day
```

**Grok-specific add-ons:** causal, empirical, correlate (when used as faux-scientific filler), figurative "underscore", "X rather than Y" abstractions.

**Grok/X-native profile** (Copyleaks, Wikipedia, Grokipedia):
- Conversational bluntness masks low burstiness — wit ≠ human rhythm
- Edgy word choices still cluster at high statistical probability
- AI phrasing concentrated throughout (not just intro/conclusion like ChatGPT)
- Overuses superficially scientific register: *causal*, *empirical*, *correlate*
- Figurative "underscore" persists in Grok output through 2026
- "X rather than Y" reversed parallelisms common in Grokipedia-style prose
- Formal mode (essays, reports) falls into same low-perplexity traps as other LLMs
- Paste artifacts: `grok_card`, `grok_render_citation_card_json`, `referrer=grok.com` URLs
- Manufactured edginess at uniform energy — let one paragraph be flat or bored

**Claude-specific:** substrate, wedge, vector (abstract), harness (metaphor), paradigm, flywheel, north star.

Replace with plain words: use, help, show, is, has, many, important, change, work.

## Structural tells

| Tell | Fix |
|------|-----|
| Rule of three everywhere | Use the natural number of items |
| "Not just X, but Y" | State Y directly |
| "It's not X, it's Y" | Cut the negation frame |
| Symmetrical bullet lists | Convert to prose or uneven lists |
| Bold-label: restates line | Prose paragraphs |
| Title case headings | Sentence case |
| Intro + 3 sections + conclusion | End without summary when possible |
| Meta openers ("In this article…") | Start with the point |
| "In conclusion / Ultimately" | Delete; stop earlier |

## Punctuation & formatting

- **Em dashes:** avoid. Default zero; max one per piece when rephrasing would actually break the meaning. Never for rhythm or AI-polish.
- **Colons mid-sentence:** Rare. Rewrite as two sentences.
- **Boldface:** Proper nouns only, not every keyword.
- **Emoji in headings:** Remove unless brand requires.
- **Curly quotes:** Straight quotes in plain text.

## Syntax tells

| AI habit | Human habit |
|----------|-------------|
| "serves as / stands as / marks" | is / was / has |
| "features / offers / boasts [noun]" | has |
| "associated with / in connection with" | of / for / by / who |
| Passive stacks | Named actor + active verb |
| Even 15–20 word sentences | 3-word and 30-word mixed |
| No contractions | Contractions in casual register |
| No questions | Occasional real questions |
| Hedging chains ("may potentially") | "may" or a direct claim |
| Synonym cycling (protagonist → hero → central figure) | Pick one term, repeat |
| Participial openers ("Leveraging X, we…") | Subject-verb: "We used X to…" |
| Nominalization chains ("conducted an evaluation") | Verbs: "we evaluated" |
| Register shifts mid-piece | One dominant register throughout |
| Fake casual hedges ("to be honest", "it's worth noting") | Genuine stance ("maybe", "I think") |

## Content tells

- Puffery without evidence ("pivotal moment", "testament to", "indelible mark")
- Vague attributions ("experts say", "studies show") without naming source
- Formulaic challenges ("Despite challenges… continues to thrive")
- Positive-only sentiment with no friction
- Outline-style "future prospects" closers
- Canned significance inflation

## What detectors measure (academic consensus)

Modern classifiers (GPTZero 2023+, Originality, Turnitin) use deep-learning ensembles — not raw perplexity/burstiness alone. But the features they learn overlap heavily with:

1. **Perplexity / token predictability** — AI text = lower surprise (DetectGPT, ICML 2023).
2. **Burstiness** — variance in sentence complexity. AI = flat; human = spiky.
3. **Slop density + syntax** — participial openers, nominalizations, transition ratio, uniform length.
4. **Stylometric drift** — model-specific word clusters (LUAR embeddings).

Fix burstiness, slop density, and nominalizations first. Word substitution alone drops some detectors but reads hollow (Krishna et al., NeurIPS 2023: paraphrase evasion ≠ human voice).

**False positives:** Detectors often measure linguistic sophistication, not authorship (Liang et al., Patterns 2023: 61% FP on non-native English). Simple clear prose can score AI. Treat scores as screening, not proof.

## Signs of genuine human writing

- Simple is/has constructions
- Plain verbs (wrote, died, used) over stiff synonyms (authored, passed away, utilized)
- Occasional hedges and intensifiers ("very", "maybe", "probably", "I think") — epistemic markers are a human signal (Herbold et al., Scientific Reports 2023)
- Specific superlatives tied to evidence ("our worst quarter since 2019")
- Imperfect structure — one short graf, one long
- Opinion someone could disagree with
- Verifiable specifics or honest placeholders

## Ineffective tells (don't over-correct)

- Perfect grammar alone ≠ AI (skilled humans exist)
- Formal prose alone ≠ AI
- Single transition word ≠ AI
- Bland ≠ AI (AI is often *too* polished and positive)
