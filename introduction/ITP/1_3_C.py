
import sys

inputs = [i.strip() for i in sys.stdin.readlines()]

for i in inputs:
    n = sorted(map(int, i.split()))
    if n[0] == 0 and n[1] == 0:
        break
    else:
        print(f"{n[0]} {n[1]}")
