# Messenger Chain AI - Shortest Path Communication

## 📋 Objective
Pass a message across multiple agents with minimal hops using the shortest communication chain.

---

## 🎯 Theory

### What is Messenger Chain AI?
Messenger Chain AI is a communication system where multiple agents (nodes) are connected in a network. When one agent needs to send a message to another, the system finds the **shortest path** between them to minimize the number of hops (intermediate agents) the message must pass through.

### Key Concepts

#### 1. **Graph Representation**
- **Nodes**: Represent agents (e.g., Alice, Bob, Charlie)
- **Edges**: Represent direct communication links between agents
- **Undirected Graph**: Communication works both ways (if A can message B, then B can message A)

#### 2. **BFS (Breadth-First Search)**
- A graph traversal algorithm that explores neighbors level by level
- **Guarantees shortest path** in unweighted graphs
- Uses a **queue** (FIFO - First In First Out) data structure
- **Time Complexity**: O(V + E) where V = vertices, E = edges

#### 3. **Why BFS for Shortest Path?**
- BFS explores all nodes at distance k before exploring nodes at distance k+1
- The first time we reach the destination, we've found the shortest path
- Perfect for unweighted graphs (all hops count equally)

#### 4. **Efficiency Metric**
- **Hops**: Number of intermediate jumps needed
- **Efficiency**: In this implementation, always 100% because we use the optimal (shortest) path
- Lower hops = Higher efficiency

---

## 🖼️ Visual Representation

### Network Graph
```
        Alice
       /     \
     Bob    Diana
      |       |  \
   Charlie----   Frank
      |          /
     Eve--------
```

### Message Flow Example (Alice → Frank)
```
Alice → Diana → Frank
  ↓       ↓       ↓
Hop 1   Hop 2   Delivered
```

**Placeholder for diagram**: `images/messenger_chain_network.png`  
**Placeholder for flow**: `images/message_path_visualization.png`

---

## 💻 Complete Code with Line-by-Line Explanation

```python
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
```

---

## 📝 Line-by-Line Code Explanation

### **Lines 1-2: Imports**
```python
from collections import deque, defaultdict
```
- **`deque`**: Double-ended queue for efficient BFS (O(1) append/pop from both ends)
- **`defaultdict`**: Auto-creates empty lists for new keys, perfect for adjacency lists

---

### **Lines 4-7: Define Network Edges**
```python
edges = [
    ("Alice","Bob"), ("Bob","Charlie"), ("Alice","Diana"),
    ("Diana","Charlie"), ("Charlie","Eve"), ("Eve","Frank"),
    ("Diana","Frank")
]
```
- List of tuples representing direct connections between agents
- Each tuple `(A, B)` means agents A and B can communicate directly
- This defines the network topology

---

### **Lines 8-10: Build Adjacency List Graph**
```python
graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b); graph[b].append(a)
```
- **Line 8**: Create empty graph where each key gets an empty list by default
- **Line 9**: Iterate through each edge
- **Line 10**: Add both directions (undirected graph)
  - `graph[a].append(b)`: A can reach B
  - `graph[b].append(a)`: B can reach A

**Example Result**:
```
graph = {
    "Alice": ["Bob", "Diana"],
    "Bob": ["Alice", "Charlie"],
    "Diana": ["Alice", "Charlie", "Frank"],
    ...
}
```

---

### **Lines 12-26: BFS Shortest Path Function**
```python
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
```

#### **Line 13: Base Case**
```python
if start == end: return [start]
```
- If sender = receiver, path is just that single node

#### **Line 14: Initialize BFS**
```python
q, seen = deque([[start]]), {start}
```
- **`q`**: Queue initialized with the starting path `[[start]]`
- **`seen`**: Set to track visited nodes, prevents cycles
- Each queue item is a **complete path** (list of nodes)

#### **Line 15-17: BFS Main Loop**
```python
while q:
    path = q.popleft()
    for nb in graph[path[-1]]:
```
- **Line 15**: Continue while queue has paths to explore
- **Line 16**: Pop the leftmost (oldest) path from queue
- **Line 17**: Iterate through neighbors of the last node in current path

#### **Line 18-22: Explore Neighbors**
```python
if nb not in seen:
    new = path + [nb]
    if nb == end:
        return new
    seen.add(nb); q.append(new)
```
- **Line 18**: Only process unvisited neighbors
- **Line 19**: Create new path by extending current path with neighbor
- **Line 20-21**: If we reached destination, **return immediately** (guaranteed shortest!)
- **Line 22**: Mark neighbor as seen and add new path to queue for further exploration

#### **Line 23: No Path Found**
```python
return None
```
- If BFS completes without finding destination, no path exists

---

### **Lines 28-47: Send Message Function**

#### **Lines 29-31: Header and Find Path**
```python
print("\n" + "="*45)
print(f"{sender} → {receiver}")
path = shortest_path(sender, receiver)
```
- Print visual separator and route info
- Call BFS to find shortest path

#### **Lines 33-35: Handle No Path**
```python
if not path:
    print("No route found.")
    return
```
- Exit gracefully if agents are disconnected

#### **Lines 37-38: Display Path**
```python
print("Path:", " -> ".join(path))
hops = len(path) - 1
```
- Show complete path as: `Alice -> Diana -> Frank`
- **Hops** = nodes in path - 1 (number of jumps between nodes)

#### **Lines 40-41: Show Each Hop**
```python
for i in range(hops):
    print(f"  Hop {i+1}: {path[i]} → {path[i+1]}  \"{msg}\"")
```
- Iterate through each hop
- Display which agent forwards the message to next agent
- Shows message content at each step

#### **Lines 43-47: Efficiency Report**
```python
efficiency = 100.0
print(f"Delivered in {hops} hop(s).")
print(f"Efficiency = {efficiency:.1f}%")
print("="*45)
```
- **Efficiency**: Always 100% because we use optimal shortest path
- Display total hops and efficiency
- Close with visual separator

---

### **Lines 49-52: Example Demonstrations**
```python
send_message("Alice", "Frank", "Hello Frank!")
send_message("Bob", "Eve", "Update")
send_message("Alice", "Alice", "Self-check")
```
- **Example 1**: Long path message (tests multi-hop routing)
- **Example 2**: Different sender/receiver pair
- **Example 3**: Self-message (tests base case)

---

## 🚀 How to Run

### Prerequisites
```bash
# Python 3.6+ (uses f-strings)
python --version
```

### Execution
```bash
# Navigate to project directory
cd "C:\Users\ranay\PycharmProjects\AI hackaton\.venv"

# Run the script
python seventh.py
```

---

## 📊 Sample Output

```
=============================================
Alice → Frank
Path: Alice -> Diana -> Frank
  Hop 1: Alice → Diana  "Hello Frank!"
  Hop 2: Diana → Frank  "Hello Frank!"
Delivered in 2 hop(s).
Efficiency = 100.0%
=============================================

=============================================
Bob → Eve
Path: Bob -> Charlie -> Eve
  Hop 1: Bob → Charlie  "Update"
  Hop 2: Charlie → Eve  "Update"
Delivered in 2 hop(s).
Efficiency = 100.0%
=============================================

=============================================
Alice → Alice
Path: Alice
Delivered in 0 hop(s).
Efficiency = 100.0%
=============================================
```

---

## 🔍 Key Insights

### Why This Matters
1. **Minimizes Latency**: Fewer hops = faster message delivery
2. **Reduces Load**: Less messages passed through network
3. **Optimal Resource Usage**: No redundant routing

### Real-World Applications
- **Routing Protocols**: Internet packet routing (OSPF, BGP)
- **Social Networks**: Friend suggestions (mutual connections)
- **Logistics**: Package delivery route optimization
- **Telecommunications**: Call routing through minimal switches

---

## 🎓 Learning Outcomes

After understanding this code, you should be able to explain:

1. **Graph Theory Basics**: Nodes, edges, adjacency lists
2. **BFS Algorithm**: How it works and why it finds shortest paths
3. **Queue Operations**: FIFO principle in algorithm implementation
4. **Path Tracking**: How to reconstruct the path from BFS
5. **Efficiency Metrics**: Measuring communication performance

---

## 🔧 Possible Extensions

1. **Weighted Edges**: Use Dijkstra's algorithm for different communication costs
2. **Dynamic Networks**: Add/remove agents at runtime
3. **Message Priority**: Queue management for urgent messages
4. **Load Balancing**: Distribute messages across multiple paths
5. **Failure Handling**: Reroute if an agent goes offline
6. **Broadcast Messages**: One-to-many communication
7. **Real Efficiency**: Compare actual path vs theoretical optimal

---

## 📚 References

- **BFS Algorithm**: [Wikipedia - Breadth-First Search](https://en.wikipedia.org/wiki/Breadth-first_search)
- **Graph Theory**: [Introduction to Algorithms (CLRS)](https://mitpress.mit.edu/books/introduction-algorithms)
- **Python Collections**: [Python Docs - collections](https://docs.python.org/3/library/collections.html)

---

**Created for**: AI Hackathon - Track 4: Communication & Negotiation Agents  
**Topic**: #7 Messenger Chain AI  
**Date**: 2025

