import random, time

# --- User input ---
A = int(input("Agents? [4]: ") or 4)
T = int(input("Tasks? [6]: ") or 6)
G = int(input("Grid size? [8]: ") or 8)
D = float(input("Delay? [0.3]: ") or 0.3)

# --- Init agents at random positions ---
agents = [(i+1, (random.randrange(G), random.randrange(G)), 0) for i in range(A)]
# format: (id, position, busy_until)

def manh(a, b): return abs(a[0]-b[0])+abs(a[1]-b[1])

time_now = 0

for tid in range(1, T+1):
    px, py = random.randrange(G), random.randrange(G)
    dx, dy = random.randrange(G), random.randrange(G)
    print(f"\nTask {tid}: REQ:P{px},{py}-D{dx},{dy}")

    # Collect ETAs
    etas = []
    for i,(aid, pos, busy) in enumerate(agents):
        if time_now < busy:
            print(f"A{aid} -> BUSY")
            continue
        eta = manh(pos, (px,py)) + manh((px,py), (dx,dy))
        etas.append((eta, aid))
        print(f"A{aid} -> ETA:{eta}")

    if not etas:
        print("No free agents, skipping task.")
        continue

    eta, chosen = min(etas)
    print(f"A{chosen} -> TAKE")

    # Update agent state
    duration = eta + 1
    time_now += duration
    agents = [(aid, (dx,dy), time_now if aid==chosen else busy)
              for (aid,pos,busy) in agents]

    time.sleep(D)

# Summary
print("\n--- SUMMARY ---")
for aid,pos,busy in agents:
    print(f"A{aid} @ {pos}, busy_until={busy}")
print("Done.")
