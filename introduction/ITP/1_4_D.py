n = input()

nums = list(map(int, input().split())) # map()メソッドの戻り値に気を付ける

print(min(nums),max(nums), sum(nums))
