import sys

n = int(input())
r0 = int(input())
r1 = int(input())
maxv = r1 - r0
minv = min(r0, r1)

for i in map(int, sys.stdin.readlines()):
    if maxv < i - minv:
        maxv = i - minv
        if 0 > i - minv:
            minv = i
    elif minv > i:
        minv = i

print(maxv)
