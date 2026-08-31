# The Shape of AI Writing — StoryScope Layer

Source: Russell et al., [StoryScope: Investigating idiosyncrasies in AI fiction](https://arxiv.org/abs/2604.03136) (2026). Applies beyond fiction to essays, blogs, emails, and long copy.

## Core idea

AI text isn't just predictable **words** — it has predictable **shape**. Models cluster in a narrow region of narrative space. Human writing is more dispersed and statistically rarer (mean rarity percentile ~0.71 human vs ~0.49 AI).

Style edits (swap synonyms, fix em dashes) drop some detectors to ~3% accuracy. **Structure edits** still score ~93% AI. Hello Human must fix shape, not just surface.

---

## AI shape (what to break)

| Signal | AI tendency | Non-fiction example |
|--------|-------------|---------------------|
| Thematic explicitness | Narrator explains the moral (77% vs 52% human) | "This demonstrates the importance of innovation in today's world" |
| Single-track structure | 79% no subplots vs 57% human | One thesis, three supporting points, neat bow — no detours |
| Protagonist-driven resolution | Internal acceptance endings (47% vs 27%) | "We learned that resilience matters" |
| Linear time | Few jumps, flashbacks, or chronological breaks | Chronological case study with no side thread |
| Moralizing dialogue | Philosophy debate in dialogue (59% vs 34%) | Quoted experts all agree on the lesson |
| Vague allusion | Generic "many leaders" vs named references | "Industry experts" not "Marc Andreessen, 2024" |
| Embodied-emotion formula | Throat tightens, weather mirrors mood (81% vs 38%) | Cliché physical metaphors for feelings |
| Tidy causality | Every scene serves one arc | No loose end, no unrelated anecdote |
| Symmetrical pacing | Equal word count per sub-point | Three sections of identical length |
| Hyper-resolved endings | No loose ends or tension | Every thread answered in final graf |
| Abstract universality | Broad categories over specifics | "Industry trends" not "Stripe's 2024 API change" |
| Omniscient neutrality | Detached authority even in personal pieces | No "I" in an essay that should have one |
| Constant signposting | First/Moreover/Consequently every paragraph | Reader never has to connect dots |
| Harmonious contradiction | Counterargument raised then instantly neutralized | "Some disagree, but clearly…" |
| Emotion as label | Names emotion without embodied detail | "I was frustrated" with no scene |

---

## Human shape (what to add)

Apply to blogs, essays, emails 300+ words:

1. **Withhold the lesson.** Make the reader infer one conclusion. Don't state the theme in the last paragraph.
2. **Side thread / tangent.** One aside, parenthetical, or micro-obsession that slightly derails before returning.
3. **Moral ambiguity.** Two valid sides; pick one but acknowledge what you're giving up.
4. **Named specifics.** Real tools, dates, people, places — not "a leading provider."
5. **Temporal jump.** Start mid-thought; flash back later. Or "Six months earlier…"
6. **Uneven resolution.** Don't tie every thread. One open question is human.
7. **Embodiment over labeling.** Show the exact quote, action, or detail — not "I felt frustrated."
8. **Asymmetrical weighting.** 80% on one fascinating detail; gloss the rest in one sentence.
9. **Direct address (sparingly).** "You probably do this too" in blogs; skip in formal reports.

---

## Practical checklist (non-fiction)

Run after surface purge:

- [ ] **In conclusion test** — delete the final summary paragraph. Does it end sharper?
- [ ] **Tangent injection** — at least one aside or hyper-specific detail that briefly derails
- [ ] **Signpost eradication** — cut ~70% of However/Therefore/Moreover; logic carries transitions
- [ ] **Specificity pass** — swap 3+ abstract nouns for concrete, lived-in ones
- [ ] **Imbalance check** — sections uneven; human thought obsesses unevenly
- [ ] **Open loop** — one minor point left unresolved
- [ ] Theme stated explicitly **fewer than once per 500 words**
- [ ] One moment of genuine uncertainty ("I'm not sure yet whether…")

---

## Why humanizers fail

Commercial humanizers swap words → evade weak detectors → leave AI **plot geometry** intact. StoryScope: after style-only edits, narrative detection stays **93.9%**.

**Fix order:** substance → structure → syntax → vocabulary → detector score.

---

## Model fingerprints (structure)

Even at narrative level, models converge but differ slightly:
- **Claude:** flatter event escalation
- **GPT:** gossip/social framing as plot mechanism
- **Gemini:** external character description default

All still cluster away from human dispersion. Shape pass applies to all.
