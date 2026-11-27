"""Build the Tech stack section: one small SVG per icon (dark + light) and the README block that shows them.

用法（在仓库根目录运行）：python tools/tech_stack.py

- 增删图标、改鼠标悬停时浮出的说明文字：只改下面的 ROWS，然后运行上面这条命令。
- 脚本会生成 assets/svg/stack/ 里的图标，并自动重写 README.md 里
  <!-- tech-stack:start --> 和 <!-- tech-stack:end --> 之间的内容，不用手改 README。
- skillicons.dev 的图标第一次用到时会下载到 assets/icons/skill/，以后直接用本地文件。

Each icon is its own <img> so it can carry its own title= tooltip. The tiles keep skillicons' 48 px size
and 56.25 px pitch, so the rows look the same as a single skillicons strip.
"""
import base64
import html
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "assets" / "icons" / "skill"
LOGO_DIR = ROOT / "assets" / "logos"
OUT_DIR = ROOT / "assets" / "svg" / "stack"
README = ROOT / "README.md"
START, END = "<!-- tech-stack:start", "<!-- tech-stack:end -->"

# ✏️ 三行技术栈。每一项二选一：
#   ("skill", skillicons 图标名, 悬停说明)                       图标名见 https://skillicons.dev
#   ("logo", assets/logos 里的文件名, 悬停说明, 内边距, 底色)      文件名里的 {theme} 会换成 dark / light；
#                                                                内边距越大 logo 越小，"full" = 铺满；底色 None = 跟随深浅主题
ROWS = [
    [  # languages
        ("skill", "c", "C — systems programming language"),
        ("skill", "cpp", "C++ — systems programming language"),
        ("skill", "python", "Python — scripting and data processing"),
        ("skill", "rust", "Rust — memory-safe systems language"),
        ("skill", "verilog", "Verilog — hardware description language"),
        ("skill", "matlab", "MATLAB — numerical computing and simulation"),
        ("skill", "cmake", "CMake — cross-platform C/C++ build system"),
        ("skill", "bash", "Bash — Unix shell scripting"),
        ("skill", "powershell", "PowerShell — Windows shell scripting"),
        ("skill", "latex", "LaTeX — technical document typesetting"),
        ("skill", "md", "Markdown — lightweight markup language"),
    ],
    [  # embedded & hardware
        ("logo", "stmicroelectronics-blue-white.svg", "STMicroelectronics — STM32 microcontrollers", "full", None),
        ("logo", "texas-instruments-symbol-transparent.png", "Texas Instruments — MSPM0 microcontrollers", 46, None),
        ("logo", "adi.svg", "Analog Devices — analog, mixed-signal and RF ICs", 56, None),
        ("logo", "espressif-symbol.png", "Espressif — ESP32 Wi-Fi / Bluetooth SoCs", 52, None),
        ("logo", "artery-wordmark.png", "Artery — AT32 microcontrollers", 12, "#1B2232"),
        ("logo", "arduino.png", "Arduino — open-source microcontroller platform", 34, None),
        ("logo", "keil-uvision.png", "Keil µVision — embedded C IDE for MCUs", "full", None),
        ("logo", "lvgl-{theme}.svg", "LVGL — embedded graphics library", 52, None),
        ("logo", "altium-designer.svg", "Altium Designer — schematic and PCB design", 40, None),
        ("logo", "cadence-pcb-editor-clean.png", "Cadence Allegro — PCB design", "full", None),
        ("logo", "kicad-logo.png", "KiCad — open-source schematic and PCB design", 26, "#F4F6FB"),
        ("logo", "easyeda.svg", "EasyEDA — online schematic and PCB design", 44, None),
        ("logo", "solidworks-user-drawn-transparent.png", "SOLIDWORKS — 3D mechanical CAD", 36, None),
    ],
    [  # software & tools
        ("skill", "ts", "TypeScript — typed JavaScript"),
        ("skill", "js", "JavaScript — language of the web"),
        ("skill", "html", "HTML — web page markup"),
        ("skill", "css", "CSS — web page styling"),
        ("skill", "react", "React — UI library"),
        ("skill", "tauri", "Tauri — Rust-based desktop app framework"),
        ("skill", "nodejs", "Node.js — JavaScript runtime"),
        ("skill", "vite", "Vite — front-end build tool"),
        ("skill", "sqlite", "SQLite — embedded database"),
        ("skill", "qt", "Qt — cross-platform C++ UI framework"),
        ("skill", "linux", "Linux — open-source operating system"),
        ("skill", "git", "Git — version control"),
    ],
]

THEMES = ("dark", "light")
TILE = {"dark": "#242938", "light": "#F4F2ED"}  # skillicons' own neutral tile colours
MIME = {".svg": "image/svg+xml", ".png": "image/png"}
# 256-unit tile plus 22 units either side = skillicons' 300-unit pitch, drawn 48 px tall
FRAME = 'width="56.25" height="48" viewBox="-22 0 300 256"'


def skill_svg(name, theme):
    cached = SKILL_DIR / f"{name}-{theme}.svg"
    if not cached.exists():
        SKILL_DIR.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(f"https://skillicons.dev/icons?i={name}&theme={theme}",
                                     headers={"User-Agent": "profile-readme-build"})
        data = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")
        if "<svg" not in data or "undefined" in data:
            raise SystemExit(f"skillicons has no icon called {name!r}")
        cached.write_text(data.strip() + "\n", encoding="utf-8", newline="\n")
    svg = cached.read_text(encoding="utf-8")
    old = 'width="48" height="48" viewBox="0 0 256 256"'
    if old not in svg:
        raise SystemExit(f"unexpected skillicons format for {name}")
    return svg.replace(old, FRAME, 1)


def data_uri(path):
    data = path.read_bytes()
    if path.suffix == ".svg":  # same bytes on every checkout, whatever git does to line endings
        data = data.replace(b"\r\n", b"\n")
    return f"data:{MIME[path.suffix]};base64," + base64.b64encode(data).decode()


def logo_svg(fn, title, pad, bg, theme):
    uri = data_uri(LOGO_DIR / fn.format(theme=theme))
    if pad == "full":
        img = (f'<image href="{uri}" x="0" y="0" width="256" height="256" preserveAspectRatio="xMidYMid slice" '
               f'clip-path="url(#tile)"/>')
    else:
        img = (f'<image href="{uri}" x="{pad}" y="{pad}" width="{256 - 2 * pad}" height="{256 - 2 * pad}" '
               f'preserveAspectRatio="xMidYMid meet"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" {FRAME} role="img"><title>{html.escape(title)}</title>'
            f'<defs><clipPath id="tile"><rect width="256" height="256" rx="60"/></clipPath></defs>'
            f'<rect width="256" height="256" rx="60" fill="{bg or TILE[theme]}"/>{img}</svg>\n')


def key_of(item):
    return item[1] if item[0] == "skill" else Path(item[1].replace("-{theme}", "")).stem


def build():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    wanted = set()
    rows_html = []
    for row in ROWS:
        cells = []
        for item in row:
            key, tip = key_of(item), item[2]
            for theme in THEMES:
                svg = skill_svg(item[1], theme) if item[0] == "skill" else logo_svg(item[1], tip, item[3], item[4], theme)
                out = OUT_DIR / f"{key}-{theme}.svg"
                out.write_text(svg, encoding="utf-8", newline="\n")
                wanted.add(out.name)
            name = html.escape(tip.split(" — ")[0])
            cells.append(f'<picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/{key}-dark.svg">'
                         f'<img src="assets/svg/stack/{key}-light.svg" alt="{name}" title="{html.escape(tip)}"></picture>')
        rows_html.append("".join(cells))
    for old in OUT_DIR.glob("*.svg"):  # drop icons that are no longer listed
        if old.name not in wanted:
            old.unlink()
    block = (f"{START}：这一段由 tools/tech_stack.py 自动生成，不要手改；改图标或悬停说明请改那个脚本里的 ROWS -->\n"
             '<p align="center">\n' + "<br>\n".join(rows_html) + "\n</p>\n" + END)
    raw = README.read_bytes().decode("utf-8")
    nl = "\r\n" if "\r\n" in raw else "\n"
    text = raw.replace("\r\n", "\n")
    i, j = text.find(START), text.find(END)
    if i < 0 or j < 0:
        raise SystemExit("README.md is missing the tech-stack:start / tech-stack:end markers")
    text = text[:i] + block + text[j + len(END):]
    README.write_bytes(text.replace("\n", nl).encode("utf-8"))
    print(f"ok: {sum(len(r) for r in ROWS)} icons in {len(ROWS)} rows")


if __name__ == "__main__":
    build()
