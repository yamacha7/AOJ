x = int(input())

h = x // 3600
m = x % 3600 // 60
s = x - (h * 3600 + m * 60) #s = x % 3600 % 60

print('{0}:{1}:{2}'.format(h, m, s))
# print(h, m, s, sep=":")
