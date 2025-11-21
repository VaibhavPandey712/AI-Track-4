# Minimal Message-Passing Maze (matches your desired output style)
from collections import deque

maze = [
  ['.','.','.','W','.','.','.','.'],
  ['.','W','.','W','.','W','W','.'],
  ['.','W','.','.','.','.','W','.'],
  ['.','.','W','W','W','.','.','.'],
  ['.','.','.','.','W','.','W','.'],
  ['W','W','.','.','.','.','W','.'],
  ['.','.','.','W','.','.','.','.'],
  ['.','W','.','.','.','.','.','T']
]

class Agent:
    def __init__(self,name,start):
        self.name=name
        self.start=start
        self.visited={start}
        self.parent={start:None}
        self.q=deque([start])
    def step(self):
        if not self.q: return None
        r,c=self.q.popleft()
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<8 and 0<=nc<8 and maze[nr][nc]!='W' and (nr,nc) not in self.visited:
                self.visited.add((nr,nc))
                self.parent[(nr,nc)]=(r,c)
                self.q.append((nr,nc))
                if maze[nr][nc]=='T': return (nr,nc)
        return None
    def share_to(self,other):
        new=self.visited - other.visited
        for cell in new:
            other.visited.add(cell)
            other.parent[cell]=self.parent.get(cell)
        return len(new)
    def path_to(self,end):
        p=[]; cur=end
        while cur is not None:
            p.append(cur); cur=self.parent.get(cur)
        return list(reversed(p))

A=Agent('A',(0,0)); B=Agent('B',(0,7)); C=Agent('C',(7,0))
agents=[A,B,C]
pairs=[(A,B),(A,C),(B,C)]

step=0; msgs=[]; treasure=None; winner=None
while step<200 and not treasure:
    step+=1
    for a in agents:
        found=a.step()
        if found:
            treasure, winner = found, a
            break
    if step%3==0:
        print(f"\n══ Step {step} MESSAGE FLOW ══")
        for s,r in pairs:
            n=s.share_to(r)
            if n>0:
                msg=f"{s.name}→{r.name}: {n} cells"
                print("  "+msg); msgs.append(msg)

if not treasure:
    print("Treasure not found.")
else:
    path=winner.path_to(treasure)
    print("\n"+"="*50)
    print(f"✓ Treasure found by Agent {winner.name} in {step} steps")
    print(f"✓ Path length: {len(path)} | Messages: {len(msgs)}\n")
    print("PATH VISUALIZATION:")
    print("   "+" ".join(str(i) for i in range(8)))
    for i in range(8):
        line=f"{i}  "
        for j in range(8):
            if (i,j) in path:
                line += "S " if (i,j)==path[0] else "T " if maze[i][j]=='T' and (i,j)==path[-1] else "* "
            else:
                line += "X " if maze[i][j]=='W' else ". "
        print(line)
    print("\nLegend: S=Start, T=Treasure, *=Path, X=Wall, .=Empty")
