# Messenger Chain AI — Shortest Path + Efficiency
from collections import deque, defaultdict

# --- Build agent network ---
edges = [
    ("Alice","Bob"), ("Bob","Charlie"), ("Alice","Diana"),
    ("Diana","Charlie"), ("Charlie","Eve"), ("Eve","Frank"),
    ("Diana","Frank")
]
graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b); graph[b].append(a)

# --- BFS shortest path ---
def shortest_path(start, end):
    if start == end: return [start]
    q, seen = deque([[start]]), {start}
    while q:
        path = q.popleft()
        for nb in graph[path[-1]]:
            if nb not in seen:
                new = path + [nb]
                if nb == end:
                    return new
                seen.add(nb); q.append(new)
    return None

# --- Message + Efficiency ---
def send_message(sender, receiver, msg):
    print("\n" + "="*45)
    print(f"{sender} → {receiver}")
    path = shortest_path(sender, receiver)

    if not path:
        print("No route found.")
        return

    print("Path:", " -> ".join(path))
    hops = len(path) - 1

    for i in range(hops):
        print(f"  Hop {i+1}: {path[i]} → {path[i+1]}  \"{msg}\"")

    # Efficiency (shortest path method always gives 100%)
    efficiency = 100.0
    print(f"Delivered in {hops} hop(s).")
    print(f"Efficiency = {efficiency:.1f}%")
    print("="*45)

# --- Example runs ---
send_message("Alice", "Frank", "Hello Frank!")
send_message("Bob", "Eve", "Update")
send_message("Alice", "Alice", "Self-check")
