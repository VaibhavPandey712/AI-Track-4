import random, matplotlib.pyplot as plt
random.seed(1)

GRID_W, GRID_H = 8, 6
AGENTS = {"A":(0,0),"B":(7,0),"C":(3,5)}
RELIEF = [(1,2),(2,4),(6,1),(5,4),(4,2),(7,5)]

try:
    MAX_STEPS = int(input("Enter max steps (1-15): "))
    if MAX_STEPS<=0: MAX_STEPS=50
except:
    MAX_STEPS=50

msgs = []
def msg(a,t): msgs.append(f"{a}: {t}")
def dist(a,b): return abs(a[0]-b[0])+abs(a[1]-b[1])

def simulate():
    unmet=set(RELIEF); pos=dict(AGENTS); paths={a:[p] for a,p in pos.items()}
    for step in range(MAX_STEPS):
        if not unmet: break
        for a in AGENTS:
            if not unmet: break
            tgt=min(unmet,key=lambda p:dist(pos[a],p))
            msg(a,f"REQUEST {tgt}")
            msg("Coord",f"ASSIGN {tgt} -> {a}")
            x,y=pos[a]; tx,ty=tgt
            nx = x + (1 if tx>x else -1 if tx<x else 0)
            ny = y + (1 if ty>y else -1 if ty<y else 0)
            if nx!=x: ny=y
            pos[a]=(nx,ny); paths[a].append((nx,ny))
            msg(a,f"MOVE {pos[a]}")
            if pos[a]==tgt:
                msg(a,f"DELIVERED {tgt}")
                unmet.discard(tgt)
    return paths, unmet

paths, unmet = simulate()
covered=set(RELIEF)-unmet

print("\n--- MESSAGE LOG ---")
for m in msgs[:200]: print(m)
print("Covered:", covered); print("Unmet:", unmet)

fig,ax=plt.subplots(figsize=(7,5))
ax.set_xlim(-0.5,GRID_W-0.5); ax.set_ylim(-0.5,GRID_H-0.5)
ax.set_xticks(range(GRID_W)); ax.set_yticks(range(GRID_H)); ax.grid(True)

for p in RELIEF:
    if p in covered: ax.scatter(*p,marker='s',s=160,color='green')
    else: ax.scatter(*p,marker='x',s=120,color='red')
    ax.text(p[0]+0.1,p[1]+0.1,str(p),fontsize=8)

for a,pts in paths.items():
    xs=[x for x,y in pts]; ys=[y for x,y in pts]
    ax.plot(xs,ys,linewidth=2,label=f"Agent {a}")
    ax.text(xs[-1]+0.1,ys[-1]+0.1,a)

plt.gca().invert_yaxis()
plt.legend(); plt.title("Disaster Relief Coverage")
plt.tight_layout(); plt.savefig("relief_coverage.png")
print("[Saved relief_coverage.png]")
