import random, os, time

ACTIONS = ["MOVE", "TURN", "PICK", "DROP"]
SYMS = list("!@#$%^&*abcxyz123")
AGENTS = 5
GEN = 40
ITERS = 80

# each agent: action → symbol it uses
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
            cnt[s] = cnt.get(s, 0) + 1
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
    print(f"Gen {g + 1}/{GEN}  Success: {rate * 100:.1f}%")
    print("Success bar:", "#" * int(rate * 40))

    vocab = majority_vocab()
    print("\nEvolving Vocabulary:")
    for act, sym in vocab.items():
        print(f" {act} -> {sym}")

    time.sleep(0.1)

print("\nFinal Vocabulary:")
for act, sym in majority_vocab().items():
    print(f"{act} -> {sym}")
