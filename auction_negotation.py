# Tiny Resource Negotiators — focused on negotiation logs

class Agent:
    def __init__(self, name, budget, wants):
        self.name, self.budget, self.wants = name, budget, wants
        self.won = []

agents = [
    Agent("Alice", 100, {"CPU":5, "RAM":4}),
    Agent("Bob",   90,  {"GPU":5, "RAM":3}),
    Agent("Charlie",110,{"CPU":3, "GPU":4})
]

BASE = 20
ROUNDS = 6

def negotiate(item):
    print(f"\n--- {item} (base ${BASE}) ---")
    cont = []
    for a in agents:
        p = a.wants.get(item,0)
        if p>0 and a.budget>=BASE:
            max_bid = min(a.budget, BASE + p*10)
            cont.append({"a":a,"max":max_bid,"p":p})
            print(f"  {a.name} joins (priority {p}, max ${max_bid})")
    if not cont:
        print("  No contestants.")
        return
    price = BASE
    leader = None
    for r in range(1, ROUNDS+1):
        print(f"  Round {r} — current ${price}")
        proposals = []
        for c in cont:
            a, m = c["a"], c["max"]
            if m > price:
                prop = price + (m-price+1)//2
                prop = min(prop, m, a.budget)
                if prop > price:
                    proposals.append((a, prop))
                    print(f"    {a.name} proposes ${prop}")
        if not proposals:
            # no raises -> award at current price to highest-capable
            possible = [c for c in cont if c["max"]>=price]
            if not possible:
                print("    No agreement.")
                return
            winner = max(possible, key=lambda c:(c["max"], c["p"], c["a"].name))["a"]
            winner.won.append(item); winner.budget -= price
            print(f"    WINNER: {winner.name} pays ${price} (remaining ${winner.budget})")
            return
        leader, price = max(proposals, key=lambda x:x[1])
        if all(c["max"]<=price for c in cont if c["a"] is not leader):
            leader.won.append(item); leader.budget -= price
            print(f"    WINNER: {leader.name} pays ${price} (remaining ${leader.budget})")
            return
    # rounds exhausted
    if leader:
        leader.won.append(item); leader.budget -= price
        print(f"  TIMEOUT: {leader.name} wins at ${price} (remaining ${leader.budget})")
    else:
        print("  No agreement.")

print("NEGOTIATION LOGS")
for r in ["CPU","GPU","RAM"]:
    negotiate(r)

print("\nRESULTS")
for a in agents:
    print(f"  {a.name}: Won = {', '.join(a.won) or 'Nothing'} | Remaining = ${a.budget}")
