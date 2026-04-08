from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = [
    ROOT / "assets" / "social-preview" / "github-social-preview.png",
    ROOT / "docs" / "assets" / "social-preview" / "github-social-preview.png",
]


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = []
    if bold:
        candidates.extend(
            [
                "C:/Windows/Fonts/segoeuib.ttf",
                "C:/Windows/Fonts/arialbd.ttf",
                "C:/Windows/Fonts/calibrib.ttf",
            ]
        )
    else:
        candidates.extend(
            [
                "C:/Windows/Fonts/segoeui.ttf",
                "C:/Windows/Fonts/arial.ttf",
                "C:/Windows/Fonts/calibri.ttf",
            ]
        )
    candidates.extend(
        [
            "C:/Windows/Fonts/DejaVuSans-Bold.ttf" if bold else "C:/Windows/Fonts/DejaVuSans.ttf",
        ]
    )

    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size=size)
    return ImageFont.load_default()


def rounded_box(draw: ImageDraw.ImageDraw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def chip(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, font, fill: str, text_fill: str):
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    width = (right - left) + 40
    height = (bottom - top) + 22
    rounded_box(draw, (x, y, x + width, y + height), radius=18, fill=fill)
    draw.text((x + 20, y + 8), text, font=font, fill=text_fill)
    return width, height


def main():
    image = Image.new("RGB", (1280, 640), "#f3f6fb")
    draw = ImageDraw.Draw(image)

    rounded_box(draw, (72, 68, 1236, 598), radius=28, fill="#dbe3ef")
    rounded_box(draw, (58, 54, 1222, 584), radius=28, fill="#ffffff", outline="#d6deea", width=2)

    title_font = load_font(74, bold=True)
    subtitle_font = load_font(38)
    url_font = load_font(24)
    badge_font = load_font(28, bold=True)
    chip_font = load_font(24, bold=True)

    repo_url = "JavaInterview on GitHub"
    url_box = draw.textbbox((0, 0), repo_url, font=url_font)
    url_width = url_box[2] - url_box[0]
    draw.text((1188 - url_width, 104), repo_url, font=url_font, fill="#445573")

    draw.text((120, 148), "500+ Java Interview", font=title_font, fill="#18233f")
    draw.text((120, 222), "Questions and Answers", font=title_font, fill="#18233f")
    draw.text(
        (120, 304),
        "Structured by topic for Junior, Middle, and Senior developers",
        font=subtitle_font,
        fill="#4a5a77",
    )

    badges = [
        ("Junior", "#19a84f"),
        ("Middle", "#e48a00"),
        ("Senior", "#e62b24"),
    ]
    x = 112
    for label, fill in badges:
        width, _ = chip(draw, x, 356, label, badge_font, fill, "#ffffff")
        x += width + 16

    chip_rows = [
        ["Spring Boot", "Hibernate / JPA", "SQL / PostgreSQL", "Kafka"],
        ["Docker / Kubernetes", "Collections", "Concurrency", "REST / HTTP"],
    ]

    y = 452
    for row in chip_rows:
        x = 112
        for label in row:
            width, height = chip(draw, x, y, label, chip_font, "#eef3fb", "#2b63d9")
            x += width + 14
        y += height + 16

    for output in OUTPUTS:
        output.parent.mkdir(parents=True, exist_ok=True)
        image.save(output)
        print(output)


if __name__ == "__main__":
    main()
