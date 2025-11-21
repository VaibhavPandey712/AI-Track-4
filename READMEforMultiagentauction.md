📘 README #1 — Multi-Agent Auction (Professional Edition)

(for multi_agent_auction_clean.py 

multi_agent_auction_clean

)

🧵 Overview

This project simulates a multi-agent auction, where several bidding agents compete to “own” a task by sending structured messages (RAISE/PASS).
A central Coordinator runs fixed auction rounds, tracks the highest bid, and announces the winner.

Everything happens through message logs, making it perfect for demonstrating:

Negotiation

Communication

Allocation

Simple reasoning under constraints

No GUI.
No plots.
Just clean, terminal-based multi-agent negotiation.

🚀 How the Auction Works
1️⃣ User Input

At the start:

Enter task value to be in the auction:


If nothing or invalid value is entered → default 100 is used.

2️⃣ Agents and Their Willingness

Agents:

A, B, C, D


Each agent computes a maximum willingness:

limit = value * random_factor + bias


Random factor: 0.6 to 1.3

Bias: A < B < C < D (so some agents consistently bid stronger)

This determines how far each agent will go before PASSING.

3️⃣ Coordinator Opens Auction

Example message:

Coord: ANNOUNCE T1 value=100


5 rounds in total.
Each round has:

ROUND START

Agents attempt RAISE or PASS

ROUND END with current leader

4️⃣ Agents Try to Outbid Each Other

If their limit > current bid:

They RAISE by a random increment (5–15)

Else:

They PASS

Sample messages:

A: RAISE -> 15
B: PASS cannot_beat
C: RAISE -> 27
D: PASS limit_reached

5️⃣ Winner Is Selected

Coordinator announces:

Coord: WINNER C bid=92 profit=8


Where:

profit = task_value - winning_bid

🧠 Core Logic (Explained Simply)
✔ Willingness Function

An agent won’t bid above their personal limit.

✔ Rounds

Each round, all agents get a chance to respond.

✔ RAISE

Agent increases bid if allowed.

✔ PASS

Agent gives up for the round.

✔ Winner

Highest bid after round 5.

💻 How to Run
python3 multi_agent_auction_clean.py


Enter task value or press Enter for default.

🔍 Example Output (Simplified)
Coord: ANNOUNCE T1 value=100
Coord: ROUND 1 START bid=0
A: RAISE -> 12
B: PASS cannot_beat
C: RAISE -> 24
D: PASS limit_reached
Coord: ROUND 1 END leader=C bid=24
...
Coord: WINNER C bid=87 profit=13

🎯 Purpose of This Project

✔ Shows message-based negotiation
✔ Demonstrates agent reasoning
✔ Clean, easy-to-read logs
✔ Perfect for communication-based AI hackathons

📎 Files

multi_agent_auction_clean.py — main simulation

auction_diagram.png — architecture diagram (put in /assets)
