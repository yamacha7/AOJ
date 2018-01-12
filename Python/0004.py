while True:
    try:
        input_line = input()
        if input_line == '':
            break
        else:
            a, b, c, d, e, f = map(float, input_line.split())
            x = (b*f-c*e) / (b*d-a*e)
            y = (c-a*x)/b
            print("{:.3f} {:.3f}".format(x+0,y+0))
    except:
        break
