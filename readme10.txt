📦 Delivery Talkers – README
A Lightweight Simulation of Agents Communicating to Complete Delivery Tasks
📝 Overview

This project simulates a team of delivery agents who coordinate using simple encoded messages and basic negotiation rules.
Each delivery task has:

A pickup location

A drop location

Agents calculate their ETA (Estimated Time to Complete) and the one with the shortest ETA automatically takes the task.

The goal of the project is to show how simple message exchanges can reduce overall delivery time, similar to how real delivery fleets optimize routes.

The simulation shows everything in the terminal (no GUI, no plots).

🚀 How It Works
1️⃣ User Inputs

When you run the script, you’ll be asked:

Agents? [4]:
Tasks? [6]:
Grid size? [8]:
Delay? [0.3]:


You can press Enter to accept default values or type custom values.

2️⃣ Agents Are Placed Randomly

Each agent starts at a random (x,y) position on a G×G grid.

(id, position, busy_until_time)

3️⃣ Task Generation

For every task:

Random pickup point (px,py)

Random drop point (dx,dy)

Printed as encoded message:

REQ:Ppx,py-Ddx,dy

4️⃣ Agents Respond

Idle agents respond with ETA:

A1 -> ETA:7
A2 -> ETA:5
A3 -> BUSY

5️⃣ Fastest Agent Takes the Task
A2 -> TAKE


The chosen agent becomes busy for:

ETA + 1 time units

6️⃣ Simulation Pauses (Delay)

time.sleep(D) creates a small animation effect.

7️⃣ Summary Printed

At the end:

A1 @ (5,7), busy_until=19
A2 @ (3,2), busy_until=13
...

🧠 Core Logic (Easy Explanation)
✔ Manhattan Distance

Used to calculate ETA:

distance = abs(x1-x2) + abs(y1-y2)

✔ ETA = distance to pickup + distance to drop
✔ Task Assignment

The free agent with smallest ETA is chosen.

✔ Agent Updates

After completing task:

Position updated to drop location

busy_until updated

💻 How to Run
Step 1: Save the Python file

Example name: delivery_talkers.py

Step 2: Run in terminal
python delivery_talkers.py

Step 3: Enter inputs (or press Enter for defaults)

Example:

Agents? [4]: 3
Tasks? [6]: 5
Grid size? [8]: 10
Delay? [0.3]: 0.2

🔍 Example Output
Task 1: REQ:P2,5-D7,3
A1 -> ETA:6
A2 -> ETA:9
A3 -> BUSY
A1 -> TAKE

Task 2: REQ:P1,2-D4,0
A1 -> BUSY
A2 -> ETA:7
A3 -> ETA:8
A2 -> TAKE

🎯 Project Purpose

✔ Demonstrates multi-agent communication
✔ Shows how simple message rules allow coordination
✔ Useful for AI/ML hackathons, agent communication, simulation projects
✔ Fully terminal-based, no graphics