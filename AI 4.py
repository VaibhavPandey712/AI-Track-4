# chat_to_plan_short.py
import random

# ----- CONFIG -----
RANDOM_SEED = None   # set int for reproducible runs, else None
MAX_STEPS = 40
NOISE = 0.25         # chance to propose a non-greedy neighbor
STUBBORN = 0.2       # chance an agent votes its own proposal

# ----- GRID -----
grid = [
    list("#########"),
    list("#S..#..G#"),
    list("#.#.#.#.#"),
    list("#...#...#"),
    list("#########"),
]
R, C = len(grid), len(grid[0])

def find(ch):
    for r in range(R):
        for c in range(C):
            if grid[r][c] == ch:
                return (r,c)
    return None

start = find('S'); goal = find('G')

def neigh(pos):
    r,c = pos
    moves = {"UP":(r-1,c),"DOWN":(r+1,c),"LEFT":(r,c-1),"RIGHT":(r,c+1)}
    return {m:coord for m,coord in moves.items() if 0<=coord[0]<R and 0<=coord[1]<C and grid[coord[0]][coord[1]]!='#'}

def md(a,b): return abs(a[0]-b[0])+abs(a[1]-b[1])

agents = ["Alice","Bob"]

def propose(pos):
    v = neigh(pos)
    if not v: return ("STAY", pos)
    items = list(v.items())
    items.sort(key=lambda it: (md(it[1], goal), random.random()))
    if random.random() < NOISE and len(items)>1:
        return random.choice(items[1:])
    return items[0]

def vote(agent, proposals):
    # prefer best heuristic; but sometimes stubbornly vote own
    best = min(proposals.values(), key=lambda x: md(x[1], goal))
    if random.random() < STUBBORN and agent in proposals:
        return proposals[agent]
    return best

def run(seed=None):
    if seed is not None: random.seed(seed)
    else: random.seed()
    pos = start; path=[pos]; msgs=[]
    steps=0
    while pos!=goal and steps<MAX_STEPS:
        steps+=1
        props={ag:propose(pos) for ag in agents}
        for ag,p in props.items(): msgs.append(f"{ag}: PROPOSE {p[0]}->{p[1]}")
        votes={ag:vote(ag,props) for ag in agents}
        for ag,v in votes.items(): msgs.append(f"{ag}: VOTE {v[0]}->{v[1]}")
        # tally by coord
        tally={}
        for v in votes.values():
            key=(v[1][0],v[1][1])
            tally[key]=tally.get(key,0)+1
        best = max(tally.items(), key=lambda it: (it[1], -md(it[0], goal)))[0]
        pos = (best[0], best[1]); path.append(pos)
        msgs.append(f"SYSTEM: MOVE -> {pos}")
    return {"success": pos==goal, "steps": len(path)-1, "path":path, "msgs":msgs}

if __name__=="__main__":
    res = run(RANDOM_SEED)
    # print trimmed conversation
    print("\n--- LOG (last 50) ---")
    for m in res['msgs'][-50:]:
        print(m)
    print("\n--- PATH VISUAL ---")
    gv=[row[:] for row in grid]
    for r,c in res['path']:
        if gv[r][c] not in ('S','G'): gv[r][c]='*'
    for row in gv: print("".join(row))
    if res['success']:
        print(f"\nResult: Reached goal in {res['steps']} steps. ✅")
    else:
        print(f"\nResult: Failed to reach goal within step limit ({MAX_STEPS}). ❌")
    print("\nTip: lower NOISE and STUBBORN to increase chance of success; increase MAX_STEPS for more attempts.")
