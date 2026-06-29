#!/usr/bin/env python3
"""Generate 4x4 contact sheets from a folder of images."""

import os
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

SRC = Path("/Volumes/noixzy T5 EVO SSD/ASSET LIBRARY/______newDemo Renders")
DST = SRC / "contact_sheets"

COLS = 4
ROWS = 4
PER_SHEET = COLS * ROWS
CELL_W = 400
CELL_H = 400
LABEL_H = 22
PADDING = 6
BG = (255, 255, 255)
LABEL_COLOR = (0, 0, 0)
FONT_SIZE = 11

SHEET_W = COLS * CELL_W + (COLS + 1) * PADDING
SHEET_H = ROWS * (CELL_H + LABEL_H) + (ROWS + 1) * PADDING

EXTS = {".png", ".jpg", ".jpeg", ".exr"}


def collect_images(root: Path) -> list[Path]:
    files = []
    for entry in root.rglob("*"):
        if entry.is_file() and entry.suffix.lower() in EXTS:
            # skip anything inside the output folder
            if "contact_sheets" in entry.parts:
                continue
            files.append(entry)
    return sorted(files)


def fit_center_crop(img: Image.Image, w: int, h: int) -> Image.Image:
    """Scale image to fill w×h then center-crop."""
    src_w, src_h = img.size
    scale = max(w / src_w, h / src_h)
    new_w = int(src_w * scale)
    new_h = int(src_h * scale)
    img = img.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - w) // 2
    top = (new_h - h) // 2
    return img.crop((left, top, left + w, top + h))


def truncate_label(draw: ImageDraw.ImageDraw, text: str, font, max_w: int) -> str:
    if draw.textlength(text, font=font) <= max_w:
        return text
    while text and draw.textlength(text + "…", font=font) > max_w:
        text = text[:-1]
    return text + "…"


def load_image(path: Path) -> Image.Image | None:
    try:
        if path.suffix.lower() == ".exr":
            # Pillow needs OpenEXR plugin; fall back to a grey placeholder if missing
            img = Image.open(path)
        else:
            img = Image.open(path)
        img.load()
        return img.convert("RGB")
    except Exception as e:
        print(f"  SKIP {path.name}: {e}", file=sys.stderr)
        return None


def make_placeholder(w: int, h: int) -> Image.Image:
    img = Image.new("RGB", (w, h), (200, 200, 200))
    d = ImageDraw.Draw(img)
    d.line([(0, 0), (w, h)], fill=(160, 160, 160), width=2)
    d.line([(w, 0), (0, h)], fill=(160, 160, 160), width=2)
    return img


def get_font(size: int):
    candidates = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSText.ttf",
        "/System/Library/Fonts/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()


def build_sheet(images: list[tuple[Path, Image.Image | None]], font) -> Image.Image:
    sheet = Image.new("RGB", (SHEET_W, SHEET_H), BG)
    draw = ImageDraw.Draw(sheet)

    for idx, (path, img) in enumerate(images):
        row = idx // COLS
        col = idx % COLS
        x = PADDING + col * (CELL_W + PADDING)
        y = PADDING + row * (CELL_H + LABEL_H + PADDING)

        if img is not None:
            cell = fit_center_crop(img, CELL_W, CELL_H)
        else:
            cell = make_placeholder(CELL_W, CELL_H)

        sheet.paste(cell, (x, y))

        label = truncate_label(draw, path.name, font, CELL_W)
        lx = x
        ly = y + CELL_H + 3
        draw.text((lx, ly), label, fill=LABEL_COLOR, font=font)

    return sheet


def main():
    DST.mkdir(parents=True, exist_ok=True)

    print(f"Scanning {SRC} …")
    files = collect_images(SRC)
    print(f"Found {len(files)} images → {-(-len(files) // PER_SHEET)} sheets")

    font = get_font(FONT_SIZE)

    sheet_num = 0
    for i in range(0, len(files), PER_SHEET):
        batch = files[i : i + PER_SHEET]
        sheet_num += 1
        out_path = DST / f"contact_sheet_{sheet_num:03d}.png"
        print(f"  Sheet {sheet_num:03d}  ({i+1}–{i+len(batch)} of {len(files)}) → {out_path.name}")

        loaded = [(p, load_image(p)) for p in batch]
        sheet = build_sheet(loaded, font)
        sheet.save(out_path, "PNG", optimize=False)

        # close images to free memory
        for _, img in loaded:
            if img:
                img.close()

    print(f"\nDone. {sheet_num} contact sheet(s) written to:\n  {DST}")


if __name__ == "__main__":
    main()
