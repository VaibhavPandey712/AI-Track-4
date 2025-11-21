import random
random.seed(1)

AGENTS = ["A", "B", "C", "D"]

try:
    task_value = int(input("Enter task value to be in the auction: "))
    if task_value <= 0: task_value = 100
except:
    task_value = 100

TASK = {"id": "T1", "value": task_value}
ROUNDS = 5

msgs = []
def msg(a,t): msgs.append(f"{a}: {t}")

def willingness(agent, value):
    base = value * random.uniform(0.6, 1.3)
    adj = (ord(agent[0]) - ord("A")) * 8
    return base + adj

def simulate(task):
    tid, value = task["id"], task["value"]
    msg("Coord", f"ANNOUNCE {tid} value={value}")

    limits = {a: willingness(a, value) for a in AGENTS}
    current = 0
    leader = None

    for r in range(1, ROUNDS+1):
        msg("Coord", f"ROUND {r} START bid={current}")
        for a in AGENTS:
            if limits[a] > current:
                inc = random.randint(5, 15)
                new_bid = current + inc
                if new_bid <= limits[a]:
                    current = new_bid
                    leader = a
                    msg(a, f"RAISE -> {new_bid}")
                else:
                    msg(a, "PASS limit_reached")
            else:
                msg(a, "PASS cannot_beat")
        msg("Coord", f"ROUND {r} END leader={leader} bid={current}")

    profit = value - current
    msg("Coord", f"WINNER {leader} bid={current} profit={profit}")
    return leader, current, profit

winner, bid, profit = simulate(TASK)

print("\n--- MESSAGE LOG ---")
for m in msgs: print(m)

print("\n--- RESULT ---")
print(f"Winner={winner}, Bid={bid}, Profit={profit}")
