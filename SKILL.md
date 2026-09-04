---
name: photo-art-edition
description: >
  Transform one uploaded photograph into three separate, coherent editorial
  image assets: a 3:4 poster, a transparent color art sticker, and a
  transparent monochrome art sticker. Use when the user wants to extract the
  emotional memory and atmosphere of a photograph into a restrained
  illustration while preserving subject identity, core spatial relationships,
  and the visual anchor. Understand deeply, prompt lightly, and never turn the
  whole scene analysis into a checklist.
---

# Photo Art Edition

## Purpose

Turn one source photograph into a memory-led illustration edition:

- A — Editorial art poster
- B — Transparent color art sticker
- C — Transparent monochrome art sticker

The illustration is not a literal redraw. It should preserve the photograph's
emotional direction, atmosphere, subject identity, core spatial relationships,
and visual anchor while allowing photographic detail to fade.

## Output contract

- Return three separate final PNG files.
- Use the fixed names `A_poster.png`, `B_color_sticker.png`, and
  `C_monochrome_sticker.png`.
- A is a vertical 3:4 poster, default 2048×2731 or an equivalent 3:4 size.
- B and C are RGBA PNGs with real transparent pixels outside the sticker.
- Never use a combined showcase image as a substitute for A/B/C.
- Never silently change the final format to JPG, WebP, or another format.
- A non-deliverable contact sheet may be created only as an optional preview.

## Core principles

1. Understand the photograph deeply, including its emotional memory and
   atmosphere, not only its objects and geometry.
2. Keep hard anchors: subject identity, core relationships, spatial hierarchy,
   visual anchor, and emotional direction.
3. Allow soft freedoms: exact detail, minor-object count, local texture,
   precise color, and degree of abstraction.
4. Analyze in detail internally, but pass only a small selective brief to the
   image model. Do not serialize the complete analysis into a checklist.
5. After the Master Illustration is selected, derive A/B/C from it and do not
   reinterpret the source photograph downstream.

## Workflow

```text
PHOTO
→ MEMORY EXTRACTION
→ SCENE ANCHORS
→ SPARSE MASTER BRIEF
→ MASTER ILLUSTRATION
→ AUTO-LOCK
→ A/B/C DERIVATION
→ VISUAL + FILE QA
→ OUTPUT
```

### 1. Memory extraction and scene anchors

Read the whole photograph before stylizing it. Identify the primary subject,
defining relationships, foreground/midground/background, depth, hierarchy,
visual anchor, first-impression rhythm, emotional core, and the concrete visual
evidence that creates it.

Create a factual Scene Map and a compact Memory Thesis. Keep these as internal
working material or intermediate artifacts; do not automatically paste them
into the generation prompt.

Read [scene-understanding.md](references/scene-understanding.md) and
[memory-extraction.md](references/memory-extraction.md).

### 2. Sparse Master Illustration

Compress the analysis into a short master brief containing only the subject,
one key relationship, emotional memory, atmosphere, and restrained visual
language. Do not list every visible object or ask the model to recreate the
full photograph. Prefer the economy and open space of a remembered drawing.

Read [prompt-discipline.md](references/prompt-discipline.md) and
[illustration-direction.md](references/illustration-direction.md).

### 3. Automatic Master selection and lock

When image generation is available, generate up to three Master candidates and
automatically select the strongest candidate whose factual anchors, emotional
direction, atmosphere, sparse quality, and drawing language are usable for
derivatives. If no candidate passes, regenerate within the environment's safe
retry limit. Do not move to A/B/C with a failed Master.

Record the selected Master and its invariants. Downstream work may not change
those invariants.

Read [master-lock.md](references/master-lock.md) and
[consistency.md](references/consistency.md).

### 4. Produce A, B and C

- A: combine the original photograph and locked Master into a vertical 3:4
  poster. Keep the photograph realistic and lightly graded. Prefer direct
  asset placement or programmatic composition over regenerating the scene.
- B: derive a color sticker from the locked Master by isolation, crop,
  composition, die-cut border and transparent export. Remove poster-only text
  and page space.
- C: derive a monochrome sticker from B or the locked Master by changing
  primarily the color expression. Preserve the sticker silhouette and layout.

Use image editing or deterministic pixel operations when available. Call an
image model for a derivative only when the environment cannot perform the
required operation directly, and always provide the locked Master as reference.

Read [edition-poster.md](references/edition-poster.md) for A,
[edition-sticker.md](references/edition-sticker.md) for B, and
[monochrome.md](references/monochrome.md) for C.

### 5. Model selection

- In Codex, use `gpt-image-2` when available. In ChatGPT/Codex UI, use the
  built-in image-generation tool when it is exposed; do not claim model use
  when that tool is unavailable.
- If the user explicitly names a model, use that model.
- Otherwise use the host environment's default image-generation model.
- If the required image-generation or editing capability is unavailable, state
  that clearly instead of pretending the files were produced.

### 6. QA and delivery

Check visual identity and file properties. B/C must be strict RGBA PNGs with
actual transparent exterior pixels, not merely an alpha metadata flag. Reject
any asset that changes subject identity, core relationship, emotional direction,
or the required file contract.

Read [quality-control.md](references/quality-control.md) and run the validator
in `scripts/asset-validation/` when the files are available.
