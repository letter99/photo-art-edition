# Photo → Art Edition Skill V2

Turn one photograph into a coherent editorial image edition:

- `A_poster.png` — orientation-aware editorial poster
- `B_color_sticker.png` — transparent color art sticker
- `C_monochrome_sticker.png` — transparent single-color art sticker

The workflow emphasizes whole-scene understanding, a locked Master Illustration,
short selective prompts, derivative-first production, and file-level QA for
transparent sticker PNGs. Poster geometry adapts to portrait, landscape and
panoramic source images. Stickers are selected, abstracted and recomposed from
meaningful scene motifs rather than cropped from the complete illustration.
The preferred visual direction is a quiet remembered editorial watercolor
image: a modest subject, abundant breathing room, low-saturation source-derived
color, tactile paper and restrained hand-made reduction. References guide the
level of quietness and abstraction; they do not force a botanical subject,
specific composition, or object checklist.

The C asset keeps the historical filename `C_monochrome_sticker.png` for
compatibility, but its treatment is single-color rather than necessarily
black-and-white. Black is the default; ask for an ink hue or hex color when a
different tone better suits the source.

## Usage

Load `SKILL.md` as the skill instructions, then provide one source photograph.
The workflow is designed to use `gpt-image-2` when an image-generation tool is
available. If the host does not expose image generation, do not claim that the
model was used; use deterministic image editing only as an explicitly labeled
fallback.

See `SKILL.md` for the complete workflow and `references/` for stage-specific
rules. Validate sticker outputs with:

```bash
python scripts/asset-validation/validate_stickers.py B_color_sticker.png C_monochrome_sticker.png
```
