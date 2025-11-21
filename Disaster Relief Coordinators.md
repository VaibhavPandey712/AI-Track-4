📘 README #2 — Disaster Relief Coordinators (Professional Edition)

(for disaster_relief_coordinators.py 

disaster_relief_coordinators

)

🧵 Overview

This project simulates three grid-based agents delivering resources to fixed relief locations.
Agents communicate with a central Coordinator and negotiate tasks through simple REQUEST/ASSIGN messages.

Each agent moves one step at a time toward assigned targets.
The simulation:

Prints message logs

Tracks completed relief points

Generates a coverage image (relief_coverage.png)

🌍 How It Works
1️⃣ User Input
Enter max steps (1–15):


If invalid → default = 50.

2️⃣ Grid Setup

Grid size: 8 × 6

Agents at fixed starting coordinates:

A: (0,0)
B: (7,0)
C: (3,5)


Relief points (6 total):

(1,2), (2,4), (6,1), (5,4), (4,2), (7,5)

3️⃣ Agents Pick Nearest Relief Point

Each agent calculates Manhattan distance and selects the nearest unmet position:

dist = abs(x1-x2) + abs(y1-y2)


Then sends a message:

A: REQUEST (2,4)

4️⃣ Coordinator Assigns the Task

Coordinator replies:

Coord: ASSIGN (2,4) -> A


Assignment ensures no two agents target the same point.

5️⃣ Movement Toward Target

Agents move step-by-step:

Horizontal first

Then vertical

Example:

A: MOVE (1,0)
A: MOVE (1,1)
A: MOVE (1,2)

6️⃣ Delivery Completion

Once at the target:

A: DELIVERED (1,2)


Coordinator marks the relief point as covered.

7️⃣ Visualization

At the end:

Green squares = delivered

Red X = unmet

Colored lines = agent paths

Saved as:

relief_coverage.png

🧠 Core Logic (Simple Terms)
✔ Nearest-Target Assignment

Each agent always serves the closest remaining relief point.

✔ REQUEST → ASSIGN → MOVE → DELIVERED

A complete message loop for each target.

✔ Deterministic Movement

No randomness.
Same run = same path.

✔ Low Complexity

Perfect for demonstrations.
Stable and easy to follow.

💻 How to Run
python3 disaster_relief_coordinators.py


Use Enter to accept default max steps.

🔍 Example Log Output
A: REQUEST (1,2)
Coord: ASSIGN (1,2) -> A
A: MOVE (1,0)
A: MOVE (1,1)
A: MOVE (1,2)
A: DELIVERED (1,2)
...
Covered: {(1,2), (5,4), ...}
Unmet: {(7,5)}

🎯 Project Purpose

✔ Demonstrates message-based coordination
✔ Shows distributed decision-making
✔ Clean movement logic
✔ Displays coverage via PNG
✔ Great for Track-4 mini-hackathons

📎 Files

disaster_relief_coordinators.py — main simulation

relief_coverage.png — auto-generated

relief_diagram.png — architecture diagram (save in /assets)
