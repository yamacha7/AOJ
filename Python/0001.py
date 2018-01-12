mountains = []
for i in range(0,10):
    input_line = input()
    mountains.append(int(input_line))

sorted_mountains = sorted(mountains, reverse=True)
for i in range(0, 3):
    print(sorted_mountains[i])
