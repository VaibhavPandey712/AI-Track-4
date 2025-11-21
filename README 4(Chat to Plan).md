Chat-to-Plan Navigators

(for chat_to_plan_short.py)

🧵 Overview

This project simulates collaborative path planning, where multiple agents use text-based negotiation to decide how to navigate a grid world.

At every step:

Each agent proposes a direction

Agents vote on the best move

Majority-approved move is executed

This showcases:

Consensus formation

Noisy negotiation

Multi-agent decision-making

Joint planning

Simple console logs show the entire negotiation process.

🚀 How the Navigation Works
1️⃣ Shared Environment

A small maze/grid containing:

S → Start

G → Goal

# → Wall

. → Free path

Both agents share the same position and move together.

2️⃣ Agents

Agents:

Alice

Bob

Each has a heuristic for moving toward the goal.

Sometimes:

They pick greedy moves

They make noisy/random choices

They disagree, requiring a vote

3️⃣ PROPOSE–VOTE Protocol

At each step:

Alice: PROPOSE RIGHT -> (1,2)
Bob: PROPOSE DOWN -> (2,1)

Alice: VOTE RIGHT
Bob: VOTE DOWN

SYSTEM: CHOSEN RIGHT


Majority (or tie-break rule) decides the final move.

4️⃣ Success / Failure

The run ends when:

✔ Agents reach the goal
OR
❌ They exceed 40 steps (realistic failure)

🧠 Core Logic (Explained Simply)

✔ Agents compute valid moves
✔ Evaluate Manhattan distance to goal
✔ Propose best move (with some noise)
✔ Vote based on lowest heuristic
✔ Update shared path

💻 How to Run
python3 chat_to_plan_short.py


The program prints last 50 messages for readability.

🔍 Example Output (Simplified)
Alice: PROPOSE RIGHT -> (1,2)
Bob: PROPOSE RIGHT -> (1,2)
Alice: VOTE RIGHT
Bob: VOTE RIGHT
SYSTEM: MOVE -> (1,2)

...

Result: Reached goal in 15 steps


or sometimes:

Result: Failed to reach goal within step limit (40).


(Randomness makes it realistic.)

🎯 Purpose of This Project

✔ Demonstrates negotiation-based planning
✔ Perfect interactive message logs
✔ Shows consensus formation
✔ Models uncertainty via noisy proposals
