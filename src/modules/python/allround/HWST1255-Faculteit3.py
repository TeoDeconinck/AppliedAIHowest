
getal = int(input())
faculteit = 1

while getal < 0:
    getal = int(input())

if getal >= 0:
    for i in range(1, getal + 1):
        faculteit *= i

    print(faculteit, end="")






#
#
# HWST1255 - Faculteit 3
#
# Lees een geheel getal in (int of long) en druk de faculteit af van dit getal (neem geen nieuwe lijn bij het afdrukken). Blijf aandringen op een positief getal zolang je een negatief krijgt.
#
# De faculteit van een getal is gedefinieerd als n! = n * (n-1) * (n-2) * ... * 2 * 1, en 0! = 1 per definitie.
#
# Invoer
# Een geheel getal.
#
# Uitvoer
# De faculteit van het ingegeven getal (zonder return). Zolang de invoer kleiner dan 0 is moet het programma een nieuw geheel getal opvragen.
#
# Voorbeelden
# Invoer:
# 6
#
# Uitvoer:
# 720
#
# Invoer:
# -6
# -3
# 4
#
# Uitvoer:
# 24
#
# Invoer:
# 0
#
# Uitvoer:
# 1