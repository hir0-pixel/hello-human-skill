# Wikipedia AISIGNS — Complete Reference

Source: [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) and [WikiProject AI Cleanup Guide](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup/Guide_and_resources)

## Fix philosophy (read this first)

Wikipedia's cleanup model is **not** synonym-swapping to pass detectors.

1. **Patterns are symptoms, not the disease.** Fixing em dashes while leaving fabricated substance is worse than not fixing.
2. **Root cause:** LLMs regress to the mean — specific facts become generic, positive, important-sounding language. Less specific *and* more exaggerated simultaneously.
3. **Rewrite from scratch** when AI draft is the substrate. Salvage verified facts only.
4. **Verify every claim** against sources. AI slop often has citations that look real but aren't.
5. **Detectors are unreliable alone.** GPTZero/Pangram have non-trivial error rates; paraphrasing defeats them. Pattern density + substance check beats a score.
6. **Do not mask tells to evade detection** — makes forensic cleanup harder without fixing quality.
7. **Probability compounds.** One sign proves nothing. Three independent signs in one passage → treat as AI until rewritten.
8. **Don't over-correct ineffective indicators** (see below) — stripping human traits makes writing worse.

Heavy LLM users detect AI ~90% of the time; casual humans score near chance. Assume ~10% false-positive risk on detectors.

---

## Content tells

| Pattern | Words to watch | Fix |
|---------|----------------|-----|
| Undue significance/legacy | stands/serves as, testament/reminder, pivotal/vital/key role, underscores importance, evolving landscape, indelible mark, setting the stage for | State what happened |
| Canned notability | independent coverage, media outlets, cited/featured/profiled in, leading expert, active social media presence | Name one outlet or cut |
| Superficial -ing tails | highlighting…, ensuring…, reflecting…, fostering…, valuable insights, align/resonate with | End at the fact |
| Promotional tone | boasts a, vibrant, nestled, in the heart of, groundbreaking, renowned, diverse array | Neutral description |
| Vague attribution | Industry reports, Experts argue, several sources (citing one) | Name source or delete |
| Outline close | Despite its…faces challenges, Despite these challenges, Future Outlook | Cut formula |
| Other | "X refers to…" for non-proper nouns; "Awards and recognition" headings; generic "debates" framing | Direct prose |

---

## Language and grammar

### AI vocabulary (strongest tell when clustered)
Additionally, align with, boasts, bolstered, crucial, deep dive, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adj), landscape (abstract), meticulous, pivotal, robust, showcase, tapestry, testament, underscore (verb), valuable, vibrant.

**Take literally:** synonyms are NOT implicated. One word = coincidence; cluster = tell.

**Eras:** GPT-4 (2023–mid-2024): delve, tapestry, testament, intricate, meticulous, boasts, garner. GPT-4o (mid-2024–mid-2025): align with, fostering, enhance, showcasing, vibrant. GPT-5+ (mid-2025+): emphasizing, showcasing + notability boilerplate.

### Copula avoidance (>10% drop in is/are post-2023)
serves as, stands as, functions as, represents, marks, boasts/features/offers [noun], refers to → **is / has / was**

### Vague connection
in connection with, associated with → **of / for / by / who**

### Negative parallelisms
not only X but Y; not X but Y; no X no Y just Z; X rather than Y (Grok-heavy)

### Rule of three
adjective-adjective-adjective; three parallel phrases making thin analysis look comprehensive

---

## Style tells

- Article-title heading above content
- Title case headings → sentence case
- Headings containing only sub-headings
- Mechanical boldface (every keyword bolded)
- Inline-header lists (`**Header:** restates line`)
- Em dashes formulaic and *spaced* (note: GPT-5.1+ uses fewer; Claude uses more than pros per 2026 study)
- Emoji as heading/bullet decoration
- Needless tables that should be prose
- Curly/smart quotes (weak alone — Word/macOS also produce these)
- Skipped heading levels; overuse of level-1 headings
- `----` thematic breaks between every section

---

## Communication artifacts (never in final copy)

**Chatbot:** I hope this helps, Certainly!, Would you like…, let me know, here is a…

**Disclaimers:** as of my last training update, while specific details are limited, not widely documented, in the provided sources, based on available information

**Placeholders:** [Specific Topic], [Your Name], PASTE_URL_HERE, access-date=2025-XX-XX

**AI identity:** as an AI language model, as a large language model

**Edit-summary tells (if reviewing drafts):** ensured neutrality, complies with Manual of Style, preserved/retained/avoided, emphasis on "sourced" over substance, itemizing template names

---

## Markup & citation tells

- Markdown where plain text belongs (`#`, `**`, `---`)
- Broken wikitext / template garbling
- Hallucinated categories, templates, red-link refs
- Dead links, invalid ISBNs, wrong DOIs
- `utm_source=chatgpt.com`, `referrer=grok.com`
- Model leakage — see LLM-specific below

---

## Historical (Nov 2022 – 2024)

Didactic disclaimers (it's important to note, worth noting); In summary/In conclusion/Overall closers; prompt refusals; abrupt cut-offs; forced elegant variation (synonym cycling from repetition penalty)

---

## Signs of HUMAN writing — what to ADD

LLMs *avoid* these common human constructions. Add back:

- Simple **is/has/was:** there is a, it has a, was a
- Plain verbs: wrote, moved, used, tried, died (not authored, relocated, utilized, attempted, passed away)
- **Superlatives with evidence:** one of the best, is the only, was the first
- **Hedges/intensifiers:** very, perhaps, tends to, maybe, I think
- **Wordy human phrases:** as a result of, in order to, all of the, the fact that (AI underuses these)
- Ability to explain *why* a specific choice was made
- Style consistency with author's earlier writing

---

## Ineffective indicators (don't over-correct)

- Perfect grammar alone
- Mixed casual/formal register
- "Bland" or "robotic" prose
- "Fancy"/academic/formal prose alone
- Single transition word alone
- Unsourced content alone
- Bizarre wikitext errors
- Correct wikitext/formatting

---

## LLM-specific differences

| Model | Tells | Markup leakage |
|-------|-------|----------------|
| **ChatGPT/GPT** | Broadest-context puffery; era vocab above; curly quotes | `:contentReference[oaicite:N]`, `turn0search0`, `oai_citation` |
| **Grok** | causal, empirical, correlate; underscore; "X rather than Y"; very long output | `grok_card`, `grok_render_citation_card_json`, `referrer=grok.com` |
| **Claude** | Concise; markdown-by-default; **more em dashes than pros** (2026) | Markdown habits |
| **Gemini** | Concise; less puffery | `[cite: 1]`, `[span_1](start_span)` |
| **DeepSeek** | Curly quotes | `【85†L261-269】` lenticular citations |
| **Perplexity** | — | `[attached_file:1]`, `[web:1]`, `ppl-ai-file-upload` |

**Caveat (Aug 2026):** Wikipedia flags its own AISIGNS page partly outdated for newest models. Human writing is measurably converging on LLM style. Treat vocab lists as era-stamped.

---

## Clustering rule

One em dash ≠ AI. One "delve" ≠ AI. **Co-occurrence** across categories in 200 words → rewrite. Target: ≤1 hit per category per 500 words.
