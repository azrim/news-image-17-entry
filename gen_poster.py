"""Generate a newspaper-style infographic for Nov 17, 2026 world news."""
from PIL import Image, ImageDraw, ImageFont
import textwrap

W, H = 1024, 1024

# Color palette - dark editorial
BG        = (12, 15, 25)       # deep navy
CREAM     = (245, 240, 228)
INK       = (22, 22, 26)
RED       = (200, 42, 36)
GOLD      = (218, 175, 85)
GREY_TEXT = (180, 176, 168)
CARD_BG   = (240, 236, 224)
DARK_CARD = (28, 34, 52)
ACCENT_BL = (45, 100, 160)
STRIPE    = (38, 44, 62)

def font(name, size):
    return ImageFont.truetype(f"C:/Windows/Fonts/{name}", size)

fb  = lambda s: font("georgiab.ttf", s)   # bold serif
fr  = lambda s: font("georgia.ttf", s)    # regular serif
fi  = lambda s: font("georgiai.ttf", s)    # italic serif
fsa = lambda s: font("arialbd.ttf", s)    # bold sans
fsr = lambda s: font("arial.ttf", s)      # regular sans

img = Image.new("RGB", (W, H), BG)
d   = ImageDraw.Draw(img)

# ── Decorative border ──
d.rectangle([8, 8, W-8, H-8], outline=GOLD, width=2)
d.rectangle([14, 14, W-14, H-14], outline=(60, 56, 44), width=1)

# ── Masthead ──
y = 32
d.text((W//2, y), "THE DAILY WORLD", anchor="mt", font=fb(52), fill=CREAM)
y += 60
# decorative line
d.line([60, y, W-60, y], fill=RED, width=4)
y += 10
d.text((W//2, y), "TUESDAY, 17 NOVEMBER 2026", anchor="mt", font=fsa(16), fill=GOLD)
y += 22
d.text((W//2, y), "Five stories that shaped the day  ·  Agent-rendered summary",
       anchor="mt", font=fi(14), fill=GREY_TEXT)
y += 26
d.line([60, y, W-60, y], fill=GOLD, width=1)
y += 14

# ── Lead story (big card) ──
lead_top = y
lead_h = 175
d.rectangle([28, lead_top, W-28, lead_top + lead_h], fill=DARK_CARD)
# red accent bar
d.rectangle([28, lead_top, 36, lead_top + lead_h], fill=RED)

# Region tag
d.text((52, lead_top + 12), "SHENZHEN", font=fsa(13), fill=RED)
d.text((52, lead_top + 32), "APEC Summit Convenes:", font=fb(28), fill=CREAM)
d.text((52, lead_top + 68), "World Leaders Gather in China", font=fb(26), fill=CREAM)

# Sub-details
sub_lines = [
    "Xi Jinping holds bilateral talks with Mexico's Sheinbaum and",
    "Canada's Carney. Putin arrives amid Western tensions. Trade,",
    "climate and AI governance top the agenda for 21 economies."
]
ty = lead_top + 104
for ln in sub_lines:
    d.text((52, ty), ln, font=fr(14), fill=GREY_TEXT)
    ty += 19

y = lead_top + lead_h + 14

# ── Story cards (2×2 grid) ──
stories = [
    {
        "region": "MANILA",
        "tag_color": ACCENT_BL,
        "headline": "Trump's Asia Tour:\nQuad Summit & Kim\nMeeting Floated",
        "body": "US President in Manila for Quad\ntalks with Japan, Australia, India.\nPossible DPRK summit discussed."
    },
    {
        "region": "WASHINGTON",
        "tag_color": (140, 50, 50),
        "headline": "NSA Comms Network\nSuffers Classified\nSecurity Outage",
        "body": "Sensitive US national security\ncommunications went offline.\nInvestigation underway; cause unclear."
    },
    {
        "region": "MIDDLE EAST",
        "tag_color": (60, 130, 80),
        "headline": "Germany Pushes Israel\non Gaza Humanitarian\nAid Access",
        "body": "Berlin urges opening more aid\ncorridors. Jordan blocks Telegram\nciting security concerns."
    },
    {
        "region": "GLOBAL",
        "tag_color": (160, 120, 40),
        "headline": "Nov 17 'Blackout'\nHoax Goes Viral,\nQuickly Debunked",
        "body": "Misinformation about a worldwide\npower outage spreads on social\nmedia; authorities confirm hoax."
    },
]

cols, rows = 2, 2
pad_x, pad_y = 28, 0
gap = 12
cw = (W - 2 * pad_x - gap) // cols
ch = 184

for i, s in enumerate(stories):
    r, c = divmod(i, cols)
    x = pad_x + c * (cw + gap)
    cy = y + r * (ch + gap)

    # card background
    d.rectangle([x, cy, x + cw, cy + ch], fill=CARD_BG)
    # accent strip
    d.rectangle([x, cy, x + 6, cy + ch], fill=s["tag_color"])

    # region tag
    d.text((x + 20, cy + 8), s["region"], font=fsa(12), fill=s["tag_color"])

    # headline
    hl_lines = s["headline"].split("\n")
    hy = cy + 26
    for hl in hl_lines:
        d.text((x + 20, hy), hl, font=fb(19), fill=INK)
        hy += 24

    # body
    bd_lines = s["body"].split("\n")
    by = cy + 106
    for bl in bd_lines:
        d.text((x + 20, by), bl, font=fr(13), fill=(80, 78, 72))
        by += 18

y = y + 2 * (ch + gap) + 8

# ── Bottom ticker / extra context ──
d.line([40, y, W-40, y], fill=GOLD, width=1)
y += 10

ticker_items = [
    "ECONOMY  Oil edges up on APEC trade signals",
    "TECH  EU AI Act enforcement timeline advances",
    "SPORTS  NBA early season upsets continue",
]
tx = 48
for ti_text in ticker_items:
    parts = ti_text.split("  ", 1)
    # label
    lw = d.textlength(parts[0], font=fsa(11))
    d.text((tx, y), parts[0], font=fsa(11), fill=GOLD)
    d.text((tx + lw + 6, y), parts[1], font=fr(11), fill=GREY_TEXT)
    y += 16

y += 6

# ── Footer ──
d.line([40, y, W-40, y], fill=RED, width=3)
y += 8
d.text((W//2, y), "Sources: AP, Reuters, Al Jazeera, 17 Nov 2026  ·  Agent-rendered editorial summary",
       anchor="mt", font=fsr(11), fill=(140, 136, 128))

# ── Decorative corner marks ──
for cx, cy in [(20, 20), (W-20, 20), (20, H-20), (W-20, H-20)]:
    d.ellipse([cx-3, cy-3, cx+3, cy+3], fill=GOLD)

img.save("poster.png", optimize=True)
print(f"saved poster.png  ({img.size[0]}x{img.size[1]})")
