limit = int(input())

isPriem = [True] * (limit + 1)

print(1, '', end='')

getal  = 2
while getal < len(isPriem):
    if isPriem[getal]:
        print(getal, '',end='')
        veelvoud = getal * 2
        while veelvoud < len(isPriem):
            isPriem[veelvoud] = False
            veelvoud += getal
    getal += 1