"""Build assets/svg/vendor-dark.svg and vendor-light.svg: one row of logo tiles in the skillicons.dev style.

用法（在仓库根目录运行）：python tools/vendor_logos.py
增删 logo：改下面的 LOGOS（文件放在 assets/logos/ 里），然后重新运行。
"""
import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOGOS = [  # (文件名, 鼠标悬停提示, 内边距: 越大 logo 越小; "full" = 铺满整块)
    ("altium-designer.svg", "Altium Designer", 30),
    ("cadence-pcb-editor-clean.png", "Cadence Allegro", "full"),
    ("easyeda.svg", "EasyEDA", 44),
    ("keil-studio.png", "Arm Keil MDK", 30),
    ("stmicroelectronics-blue-white.svg", "STMicroelectronics", "full"),
    ("texas-instruments-symbol-transparent.png", "Texas Instruments", 46),
    ("espressif.png", "Espressif", 24),
    ("solidworks-user-drawn-transparent.png", "SOLIDWORKS", 36),
]
TILE = {"dark": "#242938", "light": "#F4F2ED"}
MIME = {".svg": "image/svg+xml", ".png": "image/png"}


def data_uri(path):
    return f"data:{MIME[path.suffix]};base64," + base64.b64encode(path.read_bytes()).decode()


def build(theme):
    n = len(LOGOS)
    w = n * 300 - 44
    tiles = []
    for i, (fn, title, pad) in enumerate(LOGOS):
        x = i * 300
        uri = data_uri(ROOT / "assets" / "logos" / fn)
        if pad == "full":
            img = (f'<image href="{uri}" x="0" y="0" width="256" height="256" preserveAspectRatio="xMidYMid slice" '
                   f'clip-path="url(#tile)"/>')
        else:
            img = f'<image href="{uri}" x="{pad}" y="{pad}" width="{256 - 2 * pad}" height="{256 - 2 * pad}" preserveAspectRatio="xMidYMid meet"/>'
        tiles.append(f'<g transform="translate({x} 0)"><title>{title}</title>'
                     f'<rect width="256" height="256" rx="60" fill="{TILE[theme]}"/>{img}</g>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w * 48 / 256:.2f}" height="48" viewBox="0 0 {w} 256" role="img">'
           f'<title>{", ".join(t for _, t, _ in LOGOS)}</title>'
           f'<defs><clipPath id="tile"><rect width="256" height="256" rx="60"/></clipPath></defs>'
           + "".join(tiles) + "</svg>\n")
    (ROOT / "assets" / "svg" / f"vendor-{theme}.svg").write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    for t in TILE:
        build(t)
    print("ok")
