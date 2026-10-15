
from itertools import combinations

s = {1, 2, 3}
power_set = set()

for i in range(len(s) + 1):
    for c in combinations(s, i):
        power_set.add(frozenset(c))

print("Power Set:", power_set)
