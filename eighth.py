# negotiating_cleaners.py
# Simple, rule-based zone allocation for cleaners.
# Output: conflict-free task completion log.

class Cleaner:
    def __init__(self, name, preferred_zones, priority=0):
        """
        name: string id
        preferred_zones: list of zone ids in preference order
        priority: integer (higher wins tie conflicts)
        """
        self.name = name
        self.preferred = list(preferred_zones)
        self.priority = priority
        self.assigned = []

    def __repr__(self):
        return f"{self.name}(p={self.priority})"


def negotiate(cleaners, zones=None):
    """
    Simple negotiation:
      - Each cleaner proposes zones in their preference order.
      - If multiple cleaners propose the same zone in the same round,
        the cleaner with higher priority wins that zone.
      - Ties (same priority) are resolved by cleaner order.
      - Rounds continue until everyone either has no preferences left
        or all zones are assigned.
    Produces logs of proposals, conflicts, and final allocation.
    """
    assigned = {}          # zone -> cleaner.name
    remaining = {c.name: list(c.preferred) for c in cleaners}

    print("="*60)
    print("CLEANER NEGOTIATION LOG")
    print("="*60)

    round_no = 1
    while True:
        # Build proposals for this round: zone -> list of cleaners proposing it
        proposals = {}
        for c in cleaners:
            prefs = remaining.get(c.name)
            if not prefs:
                continue
            # propose their top remaining preference this round
            zone = prefs[0]
            proposals.setdefault(zone, []).append(c)

        if not proposals:
            # no more proposals
            break

        print(f"\nRound {round_no} proposals:")
        for zone, proposers in proposals.items():
            names = ", ".join(f"{p.name}(pri={p.priority})" for p in proposers)
            print(f"  Zone {zone} proposed by: {names}")

        # Resolve proposals
        for zone, proposers in proposals.items():
            if zone in assigned:
                # already assigned in prior round (skip)
                for p in proposers:
                    # remove this zone from their remaining prefs
                    if remaining.get(p.name):
                        if remaining[p.name][0] == zone:
                            remaining[p.name].pop(0)
                print(f"  Zone {zone} already assigned to {assigned[zone]}")
                continue

            # choose winner by highest priority, tie-break by original cleaners order
            proposers_sorted = sorted(proposers, key=lambda x: (-x.priority, cleaners.index(x)))
            winner = proposers_sorted[0]
            assigned[zone] = winner.name
            winner.assigned.append(zone)
            print(f"  RESOLVE: Zone {zone} -> {winner.name}")

            # Remove assigned zone from all cleaners' remaining prefs
            for c in cleaners:
                if zone in remaining.get(c.name, []):
                    remaining[c.name] = [z for z in remaining[c.name] if z != zone]

        # Advance: remove empty prefs
        for c in cleaners:
            if not remaining.get(c.name):
                remaining[c.name] = []

        round_no += 1

    # Final log
    print("\n" + "="*60)
    print("FINAL ALLOCATION (Conflict-free)")
    for c in cleaners:
        print(f"  {c.name}: {', '.join(c.assigned) if c.assigned else 'No zones'}")
    print("="*60)


# ---------------------------
# Example usage (run as script)
if __name__ == "__main__":
    cleaners = [
        Cleaner("A", ["Z1","Z2","Z3"], priority=2),
        Cleaner("B", ["Z2","Z4","Z5"], priority=1),
        Cleaner("C", ["Z1","Z6"], priority=1)
    ]
    negotiate(cleaners)
