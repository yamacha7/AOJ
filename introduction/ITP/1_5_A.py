while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    else:
        for i in range(0, h):
            print("#" * w)
        print("")
