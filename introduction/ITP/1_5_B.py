while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    else:
        for i in range(0, h):
            if i == 0 or i == h-1:
                print("#" * w)
            else:
                print("#" + "." * (w-2) + "#")
        print("")
