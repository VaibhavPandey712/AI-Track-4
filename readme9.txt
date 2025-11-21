# Message Passing (README)

## Overview

This README explains the **Message Passing** concept used in the Language Evolving Agents project. The goal is to show how agents send and interpret symbols that gradually evolve into a shared communication protocol.

This file covers:

* What message passing means
* How agents communicate using actions and symbols
* How convergence happens
* Explanation of every part of the code

---

## What is Message Passing?

Message Passing is a method where:

* One agent (Speaker) **sends a message** to another.
* The message contains a **symbol** representing an action.
* The receiving agent (Listener) **interprets** the symbol.
* The listener adjusts its knowledge to better understand the speaker next time.

Message passing is the core of how these agents evolve a shared language.

---

## How It Works in the Code

Below is the short Python code we built:

```python
import random, os, time

ACTIONS = ["MOVE","TURN","PICK","DROP"]
SYMS = list("!@#$%^&*abcxyz123")
AGENTS = 5
GEN = 40
ITERS = 80

agents = [
    {a: random.choice(SYMS) for a in ACTIONS}
    for _ in range(AGENTS)
]

def clear(): print("\033[H\033[J", end="")

def majority_vocab():
    vocab = {}
    for a in ACTIONS:
        cnt = {}
        for ag in agents:
            s = ag[a]
            cnt[s] = cnt.get(s,0)+1
        vocab[a] = max(cnt, key=cnt.get)
    return vocab

for g in range(GEN):
    success = 0

    for _ in range(ITERS):
        sp, rc = random.sample(agents, 2)
        action = random.choice(ACTIONS)
        sym = sp[action]
        guess = rc[action]
        
        if guess == sym:
            success += 1
        else:
            rc[action] = sym

        if random.random() < 0.01:
            rc[action] = random.choice(SYMS)

    clear()
    rate = success / ITERS
    print(f"Gen {g+1}/{GEN}  Success: {rate*100:.1f}%")
    print("Success bar:", "#" * int(rate * 40))
    
    vocab = majority_vocab()
    print("\nEvolving Vocabulary:")
    for act, sym in vocab.items():
        print(f" {act} -> {sym}")

    time.sleep(0.1)

print("\nFinal Vocabulary:")
for act, sym in majority_vocab().items():
    print(f"{act} -> {sym}")
```

---

## Step-by-Step Explanation

### 1. **Action and Symbol Space**

Agents must communicate actions using random symbols:

* Actions: MOVE, TURN, PICK, DROP
* Symbols: `!@#$%^&*abcxyz123`

Each agent initially picks **random symbols** for each action.

---

### 2. **Agents' Knowledge Representation**

Each agent stores:

```
{ action: symbol }
```

Example:

```
MOVE → '@'
TURN → 'c'
```

This simulates an internal dictionary mapping.

---

### 3. **Message Passing Interaction**

Each iteration:

1. Random speaker and receiver selected.
2. Speaker chooses a random action.
3. Speaker sends **symbol = mapping[action]**.
4. Listener guesses using **its own mapping[action]**.
5. If guess wrong → listener learns speaker's symbol.

This is how agents slowly synchronize.

---

### 4. **Mutation**

There is a small chance the listener randomly picks a new symbol.
This prevents stagnation and helps explore symbol space.

---

### 5. **Generation-Level Feedback**

After many interactions:

* Success rate is calculated.
* Majority vocabulary (most common symbol per action) is printed.
* ASCII bar graph shows evolution.

---

## Why Message Passing Works

This system mimics how language evolves:

* **Repeated communication** causes alignment.
* **Feedback** ensures errors reduce.
* **Mutations** introduce occasional innovations.

Eventually, all agents agree on the same symbols for each action.

---

## Final Output

The terminal will show:

* Generational success
* Success bar
* Current shared vocabulary
* Final evolved language

This demonstrates how communication protocols can emerge spontaneously from repeated message passing.

---

## End of Message Passing README
