a, b = map(int, input().split())
d, r = divmod(a, b)
print("{} {} {:.5f}".format(d,r,a/b))