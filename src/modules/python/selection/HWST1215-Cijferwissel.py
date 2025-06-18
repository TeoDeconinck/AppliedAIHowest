getal = int(input())

if getal < 0:
    print("-", end="")
    getal = -getal

if 9 < getal and getal < 100:
    print(getal % 10, end="")
    print(getal // 10, end="")
else:
    print(getal, end="")