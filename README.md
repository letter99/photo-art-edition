# Photo → Art Edition Skill V2

Turn one photograph into a coherent editorial image edition:

- `A_poster.png` — vertical 3:4 editorial poster
- `B_color_sticker.png` — transparent color art sticker
- `C_monochrome_sticker.png` — transparent monochrome art sticker

The workflow emphasizes whole-scene understanding, a locked Master Illustration,
short selective prompts, derivative-first production, and file-level QA for
transparent sticker PNGs.

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
