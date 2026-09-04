#!/usr/bin/env python3
"""Basic file-level validation for B/C sticker assets.

Usage:
    python validate_stickers.py B.png C.png

Checks that files are PNGs, are strict RGBA, and contain actual transparent
pixels outside the sticker.
This does not perform visual QA; it only validates the output contract.
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow is required: pip install pillow")
    raise SystemExit(2)


def validate(path: Path) -> bool:
    try:
        with Image.open(path) as img:
            ok_type = img.format == "PNG"
            ok_rgba = img.mode == "RGBA"
            has_transparent = False
            if ok_rgba:
                alpha = img.getchannel("A")
                # Require transparency at the exterior, not merely somewhere
                # inside the image. Corners are a conservative check that
                # catches accidental rectangular backgrounds.
                corners = (
                    alpha.getpixel((0, 0)),
                    alpha.getpixel((img.width - 1, 0)),
                    alpha.getpixel((0, img.height - 1)),
                    alpha.getpixel((img.width - 1, img.height - 1)),
                )
                has_transparent = min(corners) == 0
            print(
                f"{path}: format={img.format}, mode={img.mode}, "
                f"rgba={ok_rgba}, transparent_pixels={has_transparent}"
            )
            return ok_type and ok_rgba and has_transparent
    except Exception as exc:
        print(f"{path}: ERROR: {exc}")
        return False


def main() -> int:
    if len(sys.argv) < 2:
        print("Provide one or more sticker PNG paths.")
        return 2
    results = [validate(Path(arg)) for arg in sys.argv[1:]]
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
