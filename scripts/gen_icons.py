"""Генерирует плейсхолдер-иконки для Android из простого текста.
Заменить на реальный логотип, когда он будет — просто перезаписать
android/app/src/main/res/mipmap-*/ic_launcher*.png и drawable/splash.png."""
import os

from PIL import Image, ImageDraw, ImageFont

BG = (15, 23, 42)       # #0f172a — тёмный фон в цвет сайта
FG = (37, 99, 235)      # #2563eb — акцентный синий
TEXT = (255, 255, 255)

BASE = os.path.join(os.path.dirname(__file__), "..", "android", "app", "src", "main", "res")

SIZES = {
    "mipmap-mdpi": 48, "mipmap-hdpi": 72, "mipmap-xhdpi": 96,
    "mipmap-xxhdpi": 144, "mipmap-xxxhdpi": 192,
}


def make_icon(size):
    img = Image.new("RGBA", (size, size), BG)
    draw = ImageDraw.Draw(img)
    pad = int(size * 0.12)
    draw.rounded_rectangle([pad, pad, size - pad, size - pad], radius=int(size * 0.18), fill=FG)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(size * 0.34))
    except OSError:
        font = ImageFont.load_default()
    text = "B2B"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((size - tw) / 2 - bbox[0], (size - th) / 2 - bbox[1]), text, font=font, fill=TEXT)
    return img


for folder, size in SIZES.items():
    out_dir = os.path.join(BASE, folder)
    os.makedirs(out_dir, exist_ok=True)
    icon = make_icon(size)
    icon.save(os.path.join(out_dir, "ic_launcher.png"))
    icon.save(os.path.join(out_dir, "ic_launcher_round.png"))
    icon.save(os.path.join(out_dir, "ic_launcher_foreground.png"))

# splash-экран (фон + логотип по центру)
splash = Image.new("RGBA", (1200, 1200), BG)
draw = ImageDraw.Draw(splash)
logo = make_icon(400)
splash.paste(logo, (400, 400), logo)
for density in ["drawable", "drawable-land-mdpi", "drawable-land-hdpi", "drawable-land-xhdpi",
                "drawable-land-xxhdpi", "drawable-land-xxxhdpi", "drawable-port-mdpi",
                "drawable-port-hdpi", "drawable-port-xhdpi", "drawable-port-xxhdpi", "drawable-port-xxxhdpi"]:
    out_dir = os.path.join(BASE, density)
    os.makedirs(out_dir, exist_ok=True)
    splash.save(os.path.join(out_dir, "splash.png"))

print("Иконки и splash-экран сгенерированы (плейсхолдер).")
