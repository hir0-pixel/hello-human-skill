# Hello Human

![Hello Human mascot](assets/mascot.png)

Your AI drafts read like AI drafts. You can tell. So can everyone else.

Hello Human is an agent skill that teaches Cursor, Claude Code, and other compatible agents to write the way a real person would — with a point of view, uneven rhythm, and specifics that aren't pulled from a template.

Not another synonym spinner. Those swap "delve" for "explore" and call it a day. This fixes the stuff underneath: stiff structure, recycled tropes, filler transitions, and that polished nothing voice every model defaults to.

## Why use it

**You sound like yourself, not the model.** The skill pushes for stance, detail, and rhythm that matches the format — a Slack message shouldn't read like a white paper.

**It catches what humans notice.** The tells aren't just buzzwords. It's the rule-of-three lists, the neat conclusions, the "not X but Y" contrasts, the participial openers, the paragraphs that all do the same job. Hello Human runs a full pass over substance, structure, tropes, syntax, and genre before handing you a draft.

**It works across formats.** Email, blog posts, LinkedIn, marketing copy, essays, casual texts — each has different rules, and the skill knows the difference.

**It's built on actual research.** Wikipedia's AI writing signs, StoryScope narrative shape work, tropes.fyi, and peer-reviewed detection papers — not a blog post someone wrote in twenty minutes.

## Install

```bash
npx skills@latest add hir0-pixel/hello-human-skill --global
```

Works with Cursor, Claude Code, Codex, and other agents that support the open Agent Skills format.

## Use it

Attach the skill or just say what you need:

```
Use Hello Human for this email. I want it direct, not corporate.
```

```
Rewrite this blog post so it doesn't sound like ChatGPT wrote it.
```

```
Help me draft a LinkedIn post about our billing refactor — honest, not inspirational-poster tone.
```

The agent walks through a multi-pass workflow: fix the substance first, break the robotic shape, kill trope clusters, tighten syntax, add voice, match the genre, then revise until the draft holds up.

## What it won't do

- Spin synonyms and call it "humanized"
- Add fake typos or randomness to trick detectors
- Invent facts or citations to fill gaps

Write something worth reading first. Polish second.

## License

MIT
