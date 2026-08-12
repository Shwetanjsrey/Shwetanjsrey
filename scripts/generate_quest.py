import json
from html import escape

with open("quest-data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

quests = data["quests"]

colors = [
    "#A855F7",
    "#38BDF8",
    "#22D3EE",
    "#4ADE80",
    "#F59E0B",
    "#EC4899"
]

WIDTH = 1200
HEIGHT = 1030

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}" height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}">

<defs>
  <style>
    .title {{
      font: 700 34px monospace;
      fill: #f8fafc;
    }}

    .mission {{
      font: 18px monospace;
      fill: #a78bfa;
    }}

    .quest-name {{
      font: 700 22px monospace;
    }}

    .description {{
      font: 17px sans-serif;
      fill: #cbd5e1;
    }}

    .level {{
      font: 700 16px monospace;
    }}

    .xp {{
      font: 15px monospace;
      fill: #94a3b8;
    }}

    .percentage {{
      font: 700 17px monospace;
    }}

    .footer {{
      font: 700 17px monospace;
      fill: #cbd5e1;
    }}

    .track {{
      fill: #111827;
      stroke: #334155;
      stroke-width: 1;
    }}

    .progress {{
      animation: grow 1.5s ease-out;
      transform-origin: left;
    }}

    @keyframes grow {{
      from {{ transform: scaleX(0); }}
      to {{ transform: scaleX(1); }}
    }}
  </style>
</defs>

<rect width="1200" height="1030" rx="18" fill="#070b14"/>
<rect x="1" y="1" width="1198" height="1028" rx="18"
      fill="none" stroke="#273449" stroke-width="2"/>

<text x="45" y="58" class="title">🎯 CURRENT QUEST</text>
<line x1="350" y1="47" x2="1150" y2="47"
      stroke="#8b5cf6" stroke-width="2"/>

<text x="45" y="95" class="mission">
  &lt; Mission: Level up every day, ship impactful projects, and keep building /&gt;
</text>
'''

card_width = 535
card_height = 220
gap_x = 55
gap_y = 25
start_x = 45
start_y = 125

for i, quest in enumerate(quests):
    row = i // 2
    col = i % 2

    x = start_x + col * (card_width + gap_x)
    y = start_y + row * (card_height + gap_y)

    color = colors[i % len(colors)]
    progress = max(0, min(100, int(quest["progress"])))

    name = escape(quest["name"])
    description = escape(quest["description"])
    icon = escape(quest["icon"])
    level = escape(str(quest["level"]))
    xp = escape(quest["xp"])

    bar_width = 410
    filled = bar_width * progress / 100

    svg += f'''
<rect x="{x}" y="{y}" width="{card_width}" height="{card_height}"
      rx="16" fill="#0b1120" stroke="{color}" stroke-width="2"/>

<rect x="{x + 20}" y="{y + 25}" width="82" height="82"
      rx="18" fill="#0f172a" stroke="{color}" stroke-width="2"/>

<text x="{x + 61}" y="{y + 79}"
      text-anchor="middle"
      font-size="34">{icon}</text>

<text x="{x + 125}" y="{y + 48}"
      class="quest-name"
      fill="{color}">{name}</text>

<text x="{x + 125}" y="{y + 80}"
      class="description">{description}</text>

<rect x="{x + 125}" y="{y + 112}"
      width="{bar_width}" height="13"
      rx="6" class="track"/>

<rect x="{x + 125}" y="{y + 112}"
      width="{filled}" height="13"
      rx="6" fill="{color}"
      class="progress"/>

<text x="{x + 125}" y="{y + 155}"
      class="level"
      fill="{color}">LVL {level}</text>

<text x="{x + 535}" y="{y + 155}"
      text-anchor="end"
      class="xp">{xp} XP</text>

<text x="{x + 535}" y="{y + 112}"
      text-anchor="end"
      class="percentage"
      fill="{color}">{progress}%</text>
'''

overall_y = start_y + 3 * (card_height + gap_y) + 5

overall = max(0, min(100, int(data["overall"])))
overall_width = 690
overall_filled = overall_width * overall / 100

svg += f'''
<rect x="45" y="{overall_y}"
      width="1110" height="120"
      rx="16"
      fill="#0b1120"
      stroke="#334155"
      stroke-width="2"/>

<text x="70" y="{overall_y + 38}"
      class="footer">OVERALL PROGRESS</text>

<rect x="70" y="{overall_y + 58}"
      width="{overall_width}" height="16"
      rx="8" class="track"/>

<rect x="70" y="{overall_y + 58}"
      width="{overall_filled}" height="16"
      rx="8" fill="#8b5cf6"
      class="progress"/>

<text x="785" y="{overall_y + 72}"
      class="percentage"
      fill="#a78bfa">{overall}%</text>

<text x="900" y="{overall_y + 38}"
      class="footer">{escape(data["rank"])}</text>

<text x="900" y="{overall_y + 70}"
      class="xp">XP {escape(data["rankXp"])}</text>

</svg>
'''

with open("quest.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("quest.svg generated successfully.")
