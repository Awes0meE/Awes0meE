"""Generate the oscilloscope header SVGs (assets/svg/scope-dark.svg and scope-light.svg).

用法（在仓库根目录运行）：
    python tools/scope.py

改示波器上的文字：只改下面的 TEXT，然后重新运行上面这条命令，深色和浅色两张图会一起更新。
布局参考真实的 4 通道数字示波器正面：左边 7 寸屏 + 下方软键，右边功能键、Vertical/Horizontal/Trigger 旋钮，底部电源、USB、BNC 输入口。
"""
import math
from pathlib import Path

# ✏️ 示波器上的所有文字都在这里
TEXT = {
    "brand": "",                                         # 机身左上角品牌（留空就不显示）
    "model": "",                                         # 品牌右边的型号小字（留空就不显示）
    "status_tag": "iRidium",                             # 屏幕左上角色块
    "status": ["RUN", "H  2023 → NOW", "Delay 0.00s"],  # 屏幕顶栏
    "status_right": "1 GSa/s  14 Mpts",                  # 屏幕顶栏右侧
    "title": "iRidium",                                  # 屏幕右栏大字
    "title_sub": "LAB",                                  # 屏幕右栏第二行（和大字合起来读作 iRidium Lab）
    "title_tag": "ROBOTICS × FULL-STACK",           # 屏幕右栏第三行
    "channels": ["HARDWARE", "FIRMWARE", "SOFTWARE"],    # CH1 / CH2 / CH3
    "trigger": "TRIG  CH1 ↑",                       # 屏幕右栏底部
    "menu": ["MCU", "PCB", "CONTROL", "SENSOR FUSION", "WEB & AI", "1/2 ▸"],  # 屏幕底部菜单第 1 页（对应下面一排软键）
    # 屏幕底部菜单第 2 页：协议解码。和第 1 页每 5 秒轮换一次；一格里用 \n 分成上下两行
    "decode": ["DECODE", "UART\nRS232", "I2C", "CAN\nModbus", "SPI\n1-Wire", "2/2 ◂"],
}

OUT = Path(__file__).resolve().parent.parent / "assets" / "svg"

VW, VH = 840, 440
# screen
SX, SY, SW, SH = 24, 34, 520, 314
# graticule inside the screen
GX, GY, GW, GH = 30, 60, 390, 240
DX, DY = GW / 10, GH / 8
# right column inside the screen
IX = GX + GW + 6
IW = SX + SW - IX - 6
# menu bar inside the screen
MY = SY + SH - 40
# front panel
PX = 560
CYCLES = 2

THEMES = {
    "dark": dict(
        body="#1A1A18", body_edge="#2C2C28", bezel="#0B0B0A", label="#CFCFCA", label_muted="#8A8A84",
        key="#2B2B27", key_edge="#3A3A35", key_text="#D8D8D2", knob_hi="#5A5A54", knob_lo="#1E1E1B",
        knob_edge="#45453F", section="#3A3A35", metal_hi="#D9D9D6", metal_lo="#6E6E6A",
        port="#0E0E0D", foot="#121211",
    ),
    "light": dict(
        body="#E8E9EC", body_edge="#C9CCD2", bezel="#2A2C31", label="#2A2C31", label_muted="#6B7079",
        key="#F6F7F9", key_edge="#BFC3CA", key_text="#3A3F48", knob_hi="#FFFFFF", knob_lo="#B9BDC4",
        knob_edge="#9AA0A9", section="#C3C7CE", metal_hi="#F4F4F2", metal_lo="#8E9096",
        port="#1D1F23", foot="#BFC2C8",
    ),
}
# the screen itself is dark in both themes, like a real instrument
SCREEN = dict(bg="#05080B", grid="#1F2C36", axis="#36505F", tick="#4E6E80", text="#E6EEF3",
              muted="#7F95A3", bar="#0E151B", bar_edge="#22313C", ch=["#66CCFF", "#FF7400", "#C792EA"],
              tag="#FF7400", run="#3DDC84")

FONT_COND = "'Barlow Condensed','Arial Narrow','Roboto Condensed','Helvetica Neue',Arial,sans-serif"
FONT_SANS = "'Segoe UI','Helvetica Neue',Arial,sans-serif"
FONT_MONO = "ui-monospace,SFMono-Regular,Consolas,'Liberation Mono',Menlo,monospace"


def f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def saddle_path(phase):
    """SVPWM modulating wave of one phase: sine plus min-max zero-sequence injection."""
    cy, amp = GY + GH / 2, 2.7 * DY
    pts = []
    for i in range(0, int(GW) + 1, 2):
        th = i / GW * 2 * math.pi * CYCLES
        v = [math.sin(th - k * 2 * math.pi / 3) for k in range(3)]
        m = v[phase] - (max(v) + min(v)) / 2
        pts.append((GX + i, cy - amp * m * 2 / math.sqrt(3)))
    return "M" + " L".join(f"{f(x)} {f(y)}" for x, y in pts)


def graticule():
    s = SCREEN
    out = []
    for i in range(1, 10):
        x = GX + i * DX
        out.append(f'<line x1="{f(x)}" y1="{GY}" x2="{f(x)}" y2="{GY + GH}"/>')
    for j in range(1, 8):
        y = GY + j * DY
        out.append(f'<line x1="{GX}" y1="{f(y)}" x2="{GX + GW}" y2="{f(y)}"/>')
    grid = f'<g stroke="{s["grid"]}" stroke-width="1" stroke-dasharray="1 3">' + "".join(out) + "</g>"
    cx, cy = GX + GW / 2, GY + GH / 2
    ticks = []
    for k in range(1, 50):
        x = GX + k * DX / 5
        ticks.append(f'<line x1="{f(x)}" y1="{f(cy - 2.5)}" x2="{f(x)}" y2="{f(cy + 2.5)}"/>')
    for k in range(1, 40):
        y = GY + k * DY / 5
        ticks.append(f'<line x1="{f(cx - 2.5)}" y1="{f(y)}" x2="{f(cx + 2.5)}" y2="{f(y)}"/>')
    return (grid
            + f'<rect x="{GX}" y="{GY}" width="{GW}" height="{GH}" fill="none" stroke="{s["axis"]}"/>'
            + f'<g stroke="{s["axis"]}"><line x1="{GX}" y1="{f(cy)}" x2="{GX + GW}" y2="{f(cy)}"/>'
              f'<line x1="{f(cx)}" y1="{GY}" x2="{f(cx)}" y2="{GY + GH}"/></g>'
            + f'<g stroke="{s["tick"]}">' + "".join(ticks) + "</g>")


def key(c, x, y, w, h, label, fill=None, text=None, size=7.5, led=None):
    fill = fill or c["key"]
    text = text or c["key_text"]
    out = (f'<rect x="{f(x)}" y="{f(y + 1.5)}" width="{f(w)}" height="{f(h)}" rx="{f(min(h / 2, 5))}" fill="#000" opacity="0.25"/>'
           f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" rx="{f(min(h / 2, 5))}" fill="{fill}" stroke="{c["key_edge"]}"/>')
    if led:
        out += f'<rect x="{f(x + 3)}" y="{f(y + 3)}" width="{f(w - 6)}" height="{f(h - 6)}" rx="{f(min(h / 2 - 3, 3))}" fill="none" stroke="{led}" stroke-width="1.6"/>'
    if label:
        out += (f'<text x="{f(x + w / 2)}" y="{f(y + h / 2 + size * 0.36)}" class="sans" font-size="{size}" font-weight="600" '
                f'fill="{text}" text-anchor="middle">{esc(label)}</text>')
    return out


def knob(c, x, y, r, angle, label=None, grad="knob"):
    a = math.radians(angle - 90)
    out = (f'<circle cx="{f(x)}" cy="{f(y + 2)}" r="{f(r + 1)}" fill="#000" opacity="0.28"/>'
           f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r + 2.5)}" fill="{c["knob_edge"]}"/>'
           f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="url(#{grad})"/>'
           f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="none" stroke="{c["knob_edge"]}" stroke-width="2.2" '
           f'stroke-dasharray="1.2 2.2" opacity="0.8"/>'
           f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r * 0.62)}" fill="url(#{grad}-cap)"/>'
           f'<line x1="{f(x + r * 0.15 * math.cos(a))}" y1="{f(y + r * 0.15 * math.sin(a))}" '
           f'x2="{f(x + r * 0.55 * math.cos(a))}" y2="{f(y + r * 0.55 * math.sin(a))}" stroke="{c["label"]}" '
           f'stroke-width="1.6" stroke-linecap="round"/>')
    if label:
        out += (f'<text x="{f(x)}" y="{f(y + r + 11)}" class="sans" font-size="6.5" fill="{c["label_muted"]}" '
                f'text-anchor="middle" letter-spacing="0.4">{esc(label)}</text>')
    return out


def bnc(c, x, y, n, color):
    return (f'<text x="{f(x)}" y="{f(y - 22)}" class="sans" font-size="8" font-weight="700" fill="{color}" text-anchor="middle">{n}</text>'
            f'<circle cx="{f(x)}" cy="{f(y)}" r="17" fill="{color}" opacity="0.9"/>'
            f'<circle cx="{f(x)}" cy="{f(y)}" r="14" fill="url(#metal)" stroke="{c["metal_lo"]}"/>'
            f'<circle cx="{f(x)}" cy="{f(y)}" r="9.5" fill="{c["port"]}"/>'
            f'<circle cx="{f(x)}" cy="{f(y)}" r="5.5" fill="#E7E3D6"/>'
            f'<circle cx="{f(x)}" cy="{f(y)}" r="1.8" fill="url(#metal)"/>'
            f'<rect x="{f(x - 16)}" y="{f(y - 1.5)}" width="4" height="3" rx="1" fill="{c["metal_lo"]}"/>'
            f'<rect x="{f(x + 12)}" y="{f(y - 1.5)}" width="4" height="3" rx="1" fill="{c["metal_lo"]}"/>')


def section_label(c, x1, x2, y, label):
    return (f'<line x1="{f(x1)}" y1="{f(y)}" x2="{f(x2)}" y2="{f(y)}" stroke="{c["section"]}"/>'
            f'<rect x="{f((x1 + x2) / 2 - 3.2 * len(label) - 4)}" y="{f(y - 5)}" width="{f(6.4 * len(label) + 8)}" height="10" fill="{c["body"]}"/>'
            f'<text x="{f((x1 + x2) / 2)}" y="{f(y + 2.6)}" class="sans" font-size="7.5" font-weight="700" '
            f'fill="{c["label_muted"]}" text-anchor="middle" letter-spacing="1">{esc(label)}</text>')


def screen_layer():
    s = SCREEN
    ch = s["ch"]
    parts = [f'<rect x="{SX}" y="{SY}" width="{SW}" height="{SH}" fill="{s["bg"]}"/>']
    # status bar
    tag_w = 46
    parts.append(f'<rect x="{SX + 4}" y="{SY + 5}" width="{tag_w}" height="15" rx="2" fill="{s["tag"]}"/>'
                 f'<text x="{SX + 4 + tag_w / 2}" y="{SY + 15.8}" class="sans" font-size="9" font-weight="700" fill="#0B0B0A" text-anchor="middle">{esc(TEXT["status_tag"])}</text>')
    run, tb, delay = TEXT["status"]
    parts.append(f'<rect x="{SX + 56}" y="{SY + 5}" width="30" height="15" rx="2" fill="{s["run"]}" class="run"/>'
                 f'<text x="{SX + 71}" y="{SY + 15.8}" class="mono" font-size="8.5" font-weight="700" fill="#05080B" text-anchor="middle">{esc(run)}</text>'
                 f'<text x="{SX + 94}" y="{SY + 16}" class="mono" font-size="9" fill="{s["text"]}">{esc(tb)}</text>'
                 f'<text x="{SX + 208}" y="{SY + 16}" class="mono" font-size="9" fill="{s["muted"]}">{esc(delay)}</text>'
                 f'<text x="{SX + SW - 8}" y="{SY + 16}" class="mono" font-size="9" fill="{s["muted"]}" text-anchor="end">{esc(TEXT["status_right"])}</text>'
                 f'<line x1="{SX}" y1="{SY + 24}" x2="{SX + SW}" y2="{SY + 24}" stroke="{s["bar_edge"]}"/>')
    # graticule + traces
    parts.append(graticule())
    cx, cy = GX + GW / 2, GY + GH / 2
    parts.append(f'<path d="M{f(cx)} {GY} l-5 0 l5 7 l5 -7z" fill="{s["tag"]}"/>'
                 f'<path d="M{GX + GW} {f(cy - 2 * DY)} l6 -5 v10z" fill="{s["tag"]}" transform="translate(0 0)"/>')
    parts.append(f'<path d="M{GX - 1} {f(cy - 6)} h6 l4 6 l-4 6 h-6z" fill="{ch[0]}"/>')
    parts.append(f'<text x="{GX + 2.5}" y="{f(cy + 3)}" class="mono" font-size="7.5" font-weight="700" fill="#05080B">1</text>')
    parts.append('<g filter="url(#phosphor)">' + "".join(
        f'<path d="{saddle_path(k)}" fill="none" stroke="{ch[k]}" stroke-width="1.8" stroke-linecap="round" '
        f'stroke-linejoin="round" pathLength="1000" class="sweep"/>' for k in (2, 1, 0)) + "</g>")
    # right info column
    y = GY
    parts.append(f'<rect x="{IX}" y="{GY}" width="{IW}" height="{GH}" rx="3" fill="{s["bar"]}" stroke="{s["bar_edge"]}"/>')
    parts.append(f'<text x="{IX + 8}" y="{y + 26}" class="cond" font-size="25" font-weight="700" fill="{s["text"]}" '
                 f'textLength="{IW - 16}" lengthAdjust="spacingAndGlyphs">{esc(TEXT["title"])}</text>'
                 f'<text x="{IX + 8}" y="{y + 42}" class="cond" font-size="12.5" font-weight="600" fill="{ch[0]}" letter-spacing="1">{esc(TEXT["title_sub"])}</text>'
                 f'<text x="{IX + 8}" y="{y + 55}" class="mono" font-size="7.2" fill="{s["muted"]}">{esc(TEXT["title_tag"])}</text>')
    by = y + 66
    for k, name in enumerate(TEXT["channels"]):
        yy = by + k * 46
        parts.append(f'<rect x="{IX + 6}" y="{yy}" width="{IW - 12}" height="40" rx="3" fill="#0A1015" stroke="{ch[k]}" stroke-opacity="0.75"/>'
                     f'<rect x="{IX + 6}" y="{yy}" width="{IW - 12}" height="13" rx="3" fill="{ch[k]}"/>'
                     f'<rect x="{IX + 6}" y="{yy + 8}" width="{IW - 12}" height="5" fill="{ch[k]}"/>'
                     f'<text x="{IX + 11}" y="{yy + 10}" class="mono" font-size="8" font-weight="700" fill="#05080B">CH{k + 1}</text>'
                     f'<text x="{IX + IW - 11}" y="{yy + 10}" class="mono" font-size="7" fill="#05080B" text-anchor="end">DC 1M</text>'
                     f'<text x="{IX + 11}" y="{yy + 31}" class="cond" font-size="15.5" font-weight="700" fill="{s["text"]}" letter-spacing="0.6">{esc(name)}</text>')
    parts.append(f'<text x="{IX + 8}" y="{GY + GH - 9}" class="mono" font-size="8" fill="{s["muted"]}">{esc(TEXT["trigger"])}</text>')
    # menu bar
    parts.append(f'<rect x="{SX}" y="{MY}" width="{SW}" height="40" fill="{s["bar"]}"/>'
                 f'<line x1="{SX}" y1="{MY}" x2="{SX + SW}" y2="{MY}" stroke="{s["bar_edge"]}"/>')
    n = len(TEXT["menu"])
    cw = SW / n
    for i in range(1, n):
        x0 = SX + i * cw
        parts.append(f'<line x1="{f(x0)}" y1="{MY + 6}" x2="{f(x0)}" y2="{MY + 34}" stroke="{s["bar_edge"]}"/>')
    # page 1: the normal menu; page 2: protocol decode. The two pages cross-fade in turn.
    pg1, pg2 = [], []
    for i, m in enumerate(TEXT["menu"]):
        x0 = SX + i * cw
        pg1.append(f'<text x="{f(x0 + cw / 2)}" y="{MY + 24.5}" class="sans" font-size="10" font-weight="600" fill="{s["text"]}" text-anchor="middle">{esc(m)}</text>')
    for i, cell in enumerate(TEXT["decode"][:n]):
        cx = f(SX + i * cw + cw / 2)
        lines = cell.split("\n")
        if i == 0:
            pg2.append(f'<text x="{cx}" y="{MY + 24.5}" class="sans" font-size="10" font-weight="700" fill="{s["tag"]}" text-anchor="middle">{esc(cell)}</text>')
        elif len(lines) == 1:
            pg2.append(f'<text x="{cx}" y="{MY + 24.5}" class="sans" font-size="10" font-weight="600" fill="{s["text"]}" text-anchor="middle">{esc(cell)}</text>')
        else:
            pg2.append(f'<text x="{cx}" y="{MY + 17.5}" class="sans" font-size="9" font-weight="600" fill="{s["text"]}" text-anchor="middle">{esc(lines[0])}</text>'
                       f'<text x="{cx}" y="{MY + 30}" class="sans" font-size="9" font-weight="600" fill="{s["muted"]}" text-anchor="middle">{esc(lines[1])}</text>')
    parts.append('<g class="pg1">' + "".join(pg1) + '</g><g class="pg2">' + "".join(pg2) + "</g>")
    # beam
    parts.append(f'<g class="beam"><line x1="{GX}" y1="{GY}" x2="{GX}" y2="{GY + GH}" stroke="{s["tag"]}" stroke-width="1" stroke-dasharray="3 3" opacity="0.8"/></g>')
    return (f'<g clip-path="url(#scr)">' + "".join(parts) + "</g>"
            + f'<rect x="{SX}" y="{SY}" width="{SW}" height="{SH}" fill="url(#glass)"/>')


def panel(c):
    ch = SCREEN["ch"]
    p = []
    x0, x1 = PX, VW - 18
    # universal knob + function keys
    p.append(knob(c, x0 + 22, 62, 15, 30, "ADJUST", "knob"))
    labels = [["CURSORS", "ACQUIRE", "SAVE", None], ["MEASURE", "DISPLAY", "UTILITY", None]]
    kw, kh = 40, 17
    for r, row in enumerate(labels):
        for i, lab in enumerate(row):
            x = x0 + 50 + i * (kw + 5)
            y = 42 + r * 24
            if lab is None:
                if r == 0:
                    p.append(key(c, x, y, kw + 12, kh, "RUN/STOP", fill="#F2C94C", text="#2A2200", size=7))
                else:
                    p.append(key(c, x, y, kw + 12, kh, "AUTO", fill="#2F80ED", text="#FFFFFF", size=7.5))
            else:
                p.append(key(c, x, y, kw, kh, lab, size=6.6))
    # navigate row
    y = 90
    p.append(key(c, x0 + 50, y, 40, 15, "DECODE", size=6.4))
    for i, g in enumerate(["◀", "■", "▶"]):
        p.append(key(c, x0 + 95 + i * 22, y, 18, 15, g, size=7))
    p.append(key(c, x0 + 165, y, 42, 15, "HISTORY", size=6.4))
    p.append(key(c, x0 + 212, y, 50 - 2, 15, "DEFAULT", size=6.4))
    # sections
    y = 132
    v1, v2 = x0, x0 + 86
    h1, h2 = x0 + 92, x0 + 178
    t1, t2 = x0 + 184, x1
    p.append(section_label(c, v1, v2, y, "VERTICAL"))
    p.append(section_label(c, h1, h2, y, "HORIZONTAL"))
    p.append(section_label(c, t1, t2, y, "TRIGGER"))
    # vertical: channel keys + scale/position
    for k in range(3):
        p.append(key(c, v1 + 2, 148 + k * 32, 24, 22, str(k + 1), size=9.5, led=ch[k], text=ch[k]))
    p.append(knob(c, v1 + 60, 180, 22, -35, "SCALE"))
    p.append(knob(c, v1 + 60, 252, 13, 60, "POSITION"))
    p.append(key(c, v1 + 2, 282, 80, 15, "DIGITAL", size=6.4))
    # horizontal
    p.append(knob(c, h1 + 43, 180, 22, 20, "SCALE"))
    p.append(knob(c, h1 + 43, 252, 13, -50, "POSITION"))
    for i, lab in enumerate(["MATH", "REF", "ROLL"]):
        p.append(key(c, h1 + 2 + i * 29, 282, 26, 15, lab, size=6))
    # trigger
    for i, lab in enumerate(["SETUP", "AUTO", "NORMAL", "SINGLE"]):
        p.append(key(c, t1 + 4, 146 + i * 26, 38, 18, lab, size=6.4,
                     fill="#2F80ED" if lab == "AUTO" else None, text="#FFFFFF" if lab == "AUTO" else None))
    p.append(knob(c, t1 + 60, 186, 13, 15, "LEVEL"))
    p.append(f'<circle cx="{t1 + 60}" cy="236" r="3.5" fill="{SCREEN["tag"]}" class="run"/>'
             f'<text x="{t1 + 60}" y="250" class="sans" font-size="6.5" fill="{c["label_muted"]}" text-anchor="middle">TRIG&#39;D</text>')
    p.append(key(c, t1 + 4, 282, 76, 15, "FORCE", size=6.4))
    # utility row
    for i, lab in enumerate(["SEARCH", "ZOOM", "PRINT", "CLEAR", "MENU"]):
        p.append(key(c, x0 + 2 + i * 53, 314, 48, 15, lab, size=6.4))
    # BNC inputs
    y = 395
    for k in range(3):
        p.append(bnc(c, x0 + 40 + k * 66, y, str(k + 1), ch[k]))
    p.append(f'<text x="{x0 + 106}" y="{y + 30}" class="sans" font-size="6.2" fill="{c["label_muted"]}" text-anchor="middle">'
             f'1MΩ ‖ 16pF   ⚠ 300Vpk CAT I</text>')
    # probe compensation
    p.append(f'<rect x="{x1 - 24}" y="{y - 14}" width="6" height="16" rx="1" fill="url(#metal)"/>'
             f'<rect x="{x1 - 12}" y="{y - 14}" width="6" height="16" rx="1" fill="url(#metal)"/>'
             f'<text x="{x1 - 15}" y="{y + 12}" class="sans" font-size="5.8" fill="{c["label_muted"]}" text-anchor="middle">1kHz 3V</text>')
    return "".join(p)


def build(name, c):
    # the SVG description follows TEXT, so it stays right when the labels change
    global DESC
    chans = ", ".join(f"CH{i + 1} {n}" for i, n in enumerate(TEXT["channels"]))
    DESC = (f"A digital oscilloscope front panel. Three overlapping saddle-shaped traces on {chans}. "
            f"{TEXT['title']} {TEXT['title_sub']}, {TEXT['title_tag']}.")
    style = f"""
    .cond{{font-family:{FONT_COND};font-stretch:condensed}}
    .sans{{font-family:{FONT_SANS}}}
    .mono{{font-family:{FONT_MONO}}}
    @media (prefers-reduced-motion: no-preference){{
      .sweep{{stroke-dasharray:1000;stroke-dashoffset:1000;animation:sweep 5s cubic-bezier(.4,0,.2,1) -3.3s infinite}}
      .beam{{animation:beam 5s cubic-bezier(.4,0,.2,1) -3.3s infinite}}
      .run{{animation:blink 1.4s steps(2,start) infinite}}
      .pg1{{animation:pg1 10s infinite}}
      .pg2{{animation:pg2 10s infinite}}
    }}
    .pg2{{opacity:0}}
    @keyframes pg1{{0%,44%{{opacity:1}}50%,94%{{opacity:0}}100%{{opacity:1}}}}
    @keyframes pg2{{0%,44%{{opacity:0}}50%,94%{{opacity:1}}100%{{opacity:0}}}}
    @keyframes sweep{{0%{{stroke-dashoffset:1000}}70%{{stroke-dashoffset:0}}92%{{stroke-dashoffset:0;opacity:1}}100%{{stroke-dashoffset:0;opacity:0}}}}
    @keyframes beam{{0%{{transform:translateX(0)}}70%{{transform:translateX({GW}px)}}100%{{transform:translateX({GW}px)}}}}
    @keyframes blink{{to{{opacity:.35}}}}
    """
    softkeys = []
    n = len(TEXT["menu"])
    cw = SW / n
    for i in range(n):
        softkeys.append(key(c, SX + i * cw + cw / 2 - 26, SY + SH + 12, 52, 13, ""))
    softkeys.append(f'<circle cx="{SX + SW + 3}" cy="{SY + SH + 18.5}" r="7" fill="{c["key"]}" stroke="{c["key_edge"]}"/>'
                    f'<circle cx="{SX + SW + 3}" cy="{SY + SH + 18.5}" r="3.5" fill="#2F80ED"/>')
    bottom_left = (
        f'<circle cx="{SX + 22}" cy="402" r="13" fill="{c["key"]}" stroke="{c["key_edge"]}"/>'
        f'<circle cx="{SX + 22}" cy="402" r="9" fill="none" stroke="#3DDC84" stroke-width="2"/>'
        f'<path d="M{SX + 22} 396 v6" stroke="#3DDC84" stroke-width="2" stroke-linecap="round"/>'
        f'<rect x="{SX + 52}" y="394" width="26" height="14" rx="2" fill="{c["port"]}" stroke="{c["key_edge"]}"/>'
        f'<rect x="{SX + 56}" y="398" width="18" height="4" fill="{c["metal_lo"]}"/>'
        f'<text x="{SX + 65}" y="420" class="sans" font-size="6" fill="{c["label_muted"]}" text-anchor="middle">USB</text>'
        f'<rect x="{SX + 88}" y="394" width="22" height="14" rx="3" fill="{c["port"]}" stroke="{c["key_edge"]}"/>'
        f'<text x="{SX + 99}" y="420" class="sans" font-size="6" fill="{c["label_muted"]}" text-anchor="middle">HDMI</text>'
    )
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VW} {VH}" width="{VW}" height="{VH}" role="img" aria-labelledby="t d">
<title id="t">iRidium oscilloscope</title>
<desc id="d">{esc(DESC)}</desc>
<defs>
<style>{style}</style>
<clipPath id="scr"><rect x="{SX}" y="{SY}" width="{SW}" height="{SH}" rx="3"/></clipPath>
<filter id="phosphor" x="-5%" y="-20%" width="110%" height="140%"><feGaussianBlur stdDeviation="1.8" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<linearGradient id="body" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c["body"]}"/><stop offset="1" stop-color="{c["body_edge"]}" stop-opacity="0.55"/></linearGradient>
<linearGradient id="glass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.07"/><stop offset="0.35" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>
<radialGradient id="knob" cx="0.38" cy="0.32" r="0.8"><stop offset="0" stop-color="{c["knob_hi"]}"/><stop offset="1" stop-color="{c["knob_lo"]}"/></radialGradient>
<radialGradient id="knob-cap" cx="0.4" cy="0.35" r="0.75"><stop offset="0" stop-color="{c["knob_hi"]}"/><stop offset="1" stop-color="{c["knob_lo"]}" stop-opacity="0.85"/></radialGradient>
<linearGradient id="metal" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c["metal_hi"]}"/><stop offset="1" stop-color="{c["metal_lo"]}"/></linearGradient>
</defs>
<rect x="1" y="1" width="{VW - 2}" height="{VH - 2}" rx="20" fill="{c["body"]}" stroke="{c["body_edge"]}" stroke-width="2"/>
<rect x="1" y="1" width="{VW - 2}" height="{VH - 2}" rx="20" fill="url(#body)"/>
<rect x="8" y="8" width="{VW - 16}" height="{VH - 16}" rx="15" fill="none" stroke="{c["body_edge"]}" opacity="0.7"/>
{f'<text x="{SX}" y="25" class="cond" font-size="17" font-weight="700" fill="{c["label"]}" letter-spacing="0.5">{esc(TEXT["brand"])}</text>' if TEXT["brand"] else ""}
{f'<text x="{SX + 64}" y="24" class="sans" font-size="8" fill="{c["label_muted"]}" letter-spacing="0.4">{esc(TEXT["model"])}</text>' if TEXT["model"] else ""}
<rect x="{SX - 6}" y="{SY - 6}" width="{SW + 12}" height="{SH + 12}" rx="7" fill="{c["bezel"]}"/>
{screen_layer()}
{"".join(softkeys)}
{bottom_left}
<line x1="{PX - 8}" y1="34" x2="{PX - 8}" y2="{VH - 30}" stroke="{c["body_edge"]}" opacity="0.8"/>
{panel(c)}
</svg>
"""
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"scope-{name}.svg").write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    for n, c in THEMES.items():
        build(n, c)
    print("written to", OUT)
