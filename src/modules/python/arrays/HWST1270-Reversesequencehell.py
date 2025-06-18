list = [0] * 100
i = 0
while i < 100:
    list[i] = input()
    i += 1

i = len(list) - 1
while i >= 0:
    print(list[i])
    i -= 1