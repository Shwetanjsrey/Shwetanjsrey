import json
from html import escape

# ---------------------------------------------------------
# Load quest data
# ---------------------------------------------------------

with open("quest-data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

quests = data["quests"]


# ---------------------------------------------------------
# Theme
# ---------------------------------------------------------

# Keep the entire panel within the same visual language
# as the GitHub profile: dark navy + purple + cyan.

PURPLE = "#A855F7"
PURPLE_LIGHT = "#C084FC"

CYAN = "#38BDF8"
CYAN_LIGHT = "#67E8F9"

WHITE = "#F8FAFC"
TEXT = "#CBD5E1"
MUTED = "#94A3B8"

BACKGROUND = "#070B14"
CARD_BACKGROUND = "#0B1120"
TRACK = "#111827"
BORDER = "#273449"


# ---------------------------------------------------------
# SVG dimensions
# ---------------------------------------------------------

WIDTH = 1200
HEIGHT = 1030


# ---------------------------------------------------------
# SVG
# ---------------------------------------------------------

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}"
height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}">

<defs>

  <!-- Subtle glow used by important HUD elements -->
  <filter id="softGlow">
    <feGaussianBlur stdDeviation="3" result="blur"/>
    <feMerge>
      <feMergeNode in="blur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>

  <!-- Progress animation -->
  <style>

    .title {{
      font-family: monospace;
      font-size: 34px;
      font-weight: 700;
      letter-spacing: 1px;
      fill: {WHITE};
    }}

    .mission {{
      font-family: monospace;
      font-size: 17px;
      fill: {PURPLE_LIGHT};
    }}

    .quest-name {{
      font-family: monospace;
      font-size: 21px;
      font-weight: 700;
      letter-spacing: 0.5px;
    }}

    .description {{
      font-family: monospace;
      font-size: 15px;
      fill: {TEXT};
    }}

    .level {{
      font-family: monospace;
      font-size: 15px;
      font-weight: 700;
    }}

    .xp {{
      font-family: monospace;
      font-size: 14px;
      fill: {MUTED};
    }}

    .percentage {{
      font-family: monospace;
      font-size: 15px;
      font-weight: 700;
    }}

    .number {{
      font-family: monospace;
      font-size: 25px;
      font-weight: 700;
    }}

    .footer {{
      font-family: monospace;
      font-size: 15px;
      font-weight: 700;
      letter-spacing: 0.5px;
      fill: {TEXT};
    }}

    .progress {{
      animation: grow 1.5s ease-out;
      transform-origin: left center;
    }}

    @keyframes grow {{
      from {{
        transform: scaleX(0);
      }}

      to {{
        transform: scaleX(1);
      }}
    }}

  </style>

</defs>


<!-- =====================================================
     MAIN BACKGROUND
     ===================================================== -->

<rect
  width="{WIDTH}"
  height="{HEIGHT}"
  rx="18"
  fill="{BACKGROUND}"
/>

<rect
  x="1"
  y="1"
  width="{WIDTH - 2}"
  height="{HEIGHT - 2}"
  rx="18"
  fill="none"
  stroke="{BORDER}"
  stroke-width="2"
/>


<!-- =====================================================
     HEADER
     ===================================================== -->

<text
  x="45"
  y="58"
  class="title"
>
  CURRENT QUEST
</text>

<line
  x1="310"
  y1="47"
  x2="1150"
  y2="47"
  stroke="{PURPLE}"
  stroke-width="2"
/>

<line
  x1="310"
  y1="51"
  x2="700"
  y2="51"
  stroke="{CYAN}"
  stroke-width="1"
  opacity="0.35"
/>

<text
  x="45"
  y="95"
  class="mission"
>
  &lt; Mission: Level up every day, ship impactful projects, and keep building /&gt;
</text>
'''


# ---------------------------------------------------------
# Card layout
# ---------------------------------------------------------

card_width = 535
card_height = 220

gap_x = 55
gap_y = 25

start_x = 45
start_y = 125

bar_width = 340


# ---------------------------------------------------------
# Generate quest cards
# ---------------------------------------------------------

for i, quest in enumerate(quests):

    row = i // 2
    col = i % 2

    x = start_x + col * (card_width + gap_x)
    y = start_y + row * (card_height + gap_y)

    progress = max(
        0,
        min(100, int(quest["progress"]))
    )

    name = escape(str(quest["name"]))
    description = escape(str(quest["description"]))
    icon = escape(str(quest["icon"]))
    level = escape(str(quest["level"]))
    xp = escape(str(quest["xp"]))

    filled = bar_width * progress / 100

    # Alternate between the two colors instead of using
    # six unrelated neon colors.
    if i % 2 == 0:
        accent = PURPLE
        accent_light = PURPLE_LIGHT
    else:
        accent = CYAN
        accent_light = CYAN_LIGHT


    svg += f'''
<!-- =====================================================
     QUEST {i + 1}
     ===================================================== -->

<rect
  x="{x}"
  y="{y}"
  width="{card_width}"
  height="{card_height}"
  rx="16"
  fill="{CARD_BACKGROUND}"
  stroke="{accent}"
  stroke-width="1.5"
  opacity="0.98"
/>


<!-- Subtle top accent -->

<line
  x1="{x + 18}"
  y1="{y + 1}"
  x2="{x + card_width - 18}"
  y2="{y + 1}"
  stroke="{accent}"
  stroke-width="2"
  opacity="0.55"
/>


<!-- Number container -->

<rect
  x="{x + 20}"
  y="{y + 25}"
  width="82"
  height="82"
  rx="18"
  fill="#0A1020"
  stroke="{accent}"
  stroke-width="1.5"
/>


<!-- Number -->

<text
  x="{x + 61}"
  y="{y + 79}"
  text-anchor="middle"
  class="number"
  fill="{accent_light}"
>
  {icon}
</text>


<!-- Quest name -->

<text
  x="{x + 125}"
  y="{y + 48}"
  class="quest-name"
  fill="{accent_light}"
>
  {name}
</text>


<!-- Description -->

<text
  x="{x + 125}"
  y="{y + 80}"
  class="description"
>
  {description}
</text>


<!-- Progress track -->

<rect
  x="{x + 125}"
  y="{y + 112}"
  width="{bar_width}"
  height="12"
  rx="6"
  fill="{TRACK}"
  stroke="{BORDER}"
  stroke-width="1"
/>


<!-- Progress fill -->

<rect
  x="{x + 125}"
  y="{y + 112}"
  width="{filled}"
  height="12"
  rx="6"
  fill="{accent}"
  class="progress"
/>


<!-- Percentage -->

<text
  x="{x + 505}"
  y="{y + 123}"
  text-anchor="end"
  class="percentage"
  fill="{accent_light}"
>
  {progress}%
</text>


<!-- Level -->

<text
  x="{x + 125}"
  y="{y + 155}"
  class="level"
  fill="{accent_light}"
>
  LVL {level}
</text>


<!-- XP -->

<text
  x="{x + 505}"
  y="{y + 155}"
  text-anchor="end"
  class="xp"
>
  {xp} XP
</text>
'''


# ---------------------------------------------------------
# Overall progress
# ---------------------------------------------------------

overall_y = start_y + 3 * (card_height + gap_y) + 5

overall = max(
    0,
    min(100, int(data["overall"]))
)

overall_width = 650
overall_filled = overall_width * overall / 100


# ---------------------------------------------------------
# Overall progress panel
# ---------------------------------------------------------

svg += f'''
<!-- =====================================================
     OVERALL PROGRESS
     ===================================================== -->

<rect
  x="45"
  y="{overall_y}"
  width="1110"
  height="120"
  rx="16"
  fill="{CARD_BACKGROUND}"
  stroke="{BORDER}"
  stroke-width="1.5"
/>


<!-- Label -->

<text
  x="70"
  y="{overall_y + 38}"
  class="footer"
>
  OVERALL PROGRESS
</text>


<!-- Progress track -->

<rect
  x="70"
  y="{overall_y + 58}"
  width="{overall_width}"
  height="14"
  rx="7"
  fill="{TRACK}"
  stroke="{BORDER}"
  stroke-width="1"
/>


<!-- Progress -->

<rect
  x="70"
  y="{overall_y + 58}"
  width="{overall_filled}"
  height="14"
  rx="7"
  fill="{PURPLE}"
  class="progress"
/>


<!-- Percentage -->

<text
  x="745"
  y="{overall_y + 71}"
  class="percentage"
  fill="{PURPLE_LIGHT}"
>
  {overall}%
</text>


<!-- Rank -->

<text
  x="880"
  y="{overall_y + 38}"
  class="footer"
  fill="{CYAN_LIGHT}"
>
  {escape(str(data["rank"]))}
</text>


<!-- XP -->

<text
  x="880"
  y="{overall_y + 70}"
  class="xp"
>
  XP {escape(str(data["rankXp"]))}
</text>


</svg>
'''


# ---------------------------------------------------------
# Write SVG
# ---------------------------------------------------------

with open("quest.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("quest.svg generated successfully.")
