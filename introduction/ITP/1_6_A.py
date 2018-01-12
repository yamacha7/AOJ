n = input()
nums = list(map(int,input().split()))
cnt=0
for i in reversed(nums):
    if cnt==0:
        print(i,end="")
        cnt += 1
    else:
        print(" {}".format(i),end="")
print()
