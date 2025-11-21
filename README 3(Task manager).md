Task Division Through Communication

(for task_division_short.py)

🧵 Overview

This project implements a multi-agent task allocation system where agents coordinate using short communication messages (PROPOSE / ACK) to divide tasks fairly.

There is no central authority — task allocation emerges through message-based negotiation.

This makes the system ideal for demonstrating:

Agent communication

Decentralized decision-making

Negotiation under constraints

Balanced workload distribution

Simple logs.
No GUI.
Just pure agent-to-agent interaction.

🚀 How Task Allocation Works
1️⃣ Task Pool

The system begins with a set of tasks:

Each task has:

ID (T1, T2, T3…)

Duration/Cost

Example:
("T1", 3) → Task T1 needs 3 time units.

2️⃣ Agents

Agents:

A

B

C

Each agent performs:

Perceive available tasks

Propose taking a task

Wait for peers to ACK

Assign task to themselves

Continue until task pool is empty

3️⃣ PROPOSE–ACK Protocol

A simple, clean message passing loop:

A: PROPOSE T1(3)
B: ACK T1
C: ACK T1
A: ASSIGNED T1


This ensures:

No conflicts

Clear ownership

Reproducible behavior

4️⃣ Workload Calculation

After assignment:

Each agent’s total load is computed

Makespan = max(total_workloads)

Balance = evenness of distribution

Useful for performance evaluation.

🧠 Core Logic (Explained Simply)

✔ Agents take turns proposing
✔ Others ACK to avoid collisions
✔ Assigned tasks accumulate per agent
✔ All tasks exhausted → evaluation metrics computed

💻 How to Run
python3 task_division_short.py

🔍 Example Output (Simplified)
A: PROPOSE T1(3)
B: ACK T1
C: ACK T1
A: ASSIGNED T1

B: PROPOSE T2(2)
A: ACK T2
C: ACK T2
B: ASSIGNED T2

ASSIGNMENTS {'A':[('T1',3)], 'B':[('T2',2)], 'C':[('T3',4)]}
Makespan 4 Total 9

🎯 Purpose of This Project

✔ Shows decentralized task assignment
✔ Demonstrates PROPOSE–ACK message flow
✔ Easy logs for hackathon presentations
✔ Excellent example of collaborative multi-agent communication
