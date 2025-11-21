# task_division_short.py
from collections import deque, defaultdict
tasks = [("T1",3),("T2",2),("T3",4),("T4",1),("T5",2),("T6",3)]
agents = ["A","B","C"]
msgs=[]

q=deque(tasks)
assign=defaultdict(list)
i=0
while q:
    ag=agents[i%len(agents)]
    t=q.popleft()
    msgs.append(f"{ag}: PROPOSE take {t[0]}({t[1]})")
    # everyone ACKs simply (minimal protocol)
    for o in agents:
        if o!=ag: msgs.append(f"{o}: ACK {t[0]}")
    assign[ag].append(t)
    msgs.append(f"{ag}: ASSIGNED {t[0]}")
    i+=1

# compute simple metrics
work = {a: sum(d for _,d in assign[a]) for a in agents}
makespan = max(work.values())
total=sum(d for _,d in tasks)
util = total / (makespan * len(agents))
# balance score (1 - normalized std)
import statistics
loads=list(work.values())
stdev = statistics.pstdev(loads) if len(loads)>1 else 0
balance = 1 - (stdev / (max(loads) or 1))

print("\n--- MESSAGES ---")
print(*msgs, sep="\n")
print("\n--- ASSIGNMENTS ---")
for a in agents: print(a, assign[a], "total=", work[a])
print(f"\nTotal={total}  Makespan={makespan}  Util={util:.3f}  Balance={balance:.3f}")
