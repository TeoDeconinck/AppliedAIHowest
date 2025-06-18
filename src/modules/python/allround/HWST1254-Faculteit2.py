getal = int(input())
faculteit = 1

if getal >= 0:
    for i in range(1, getal + 1):
        faculteit *= i

    print(faculteit, end="")
else:
    print("onbepaald", end="")




#
# HWST1254 - Faculteit 2
#
# Lees een geheel getal in (int of long) en druk de faculteit af van dit getal (neem geen nieuwe lijn bij het afdrukken). Geef 'onbepaald' terug als een negatief getal wordt opgegeven.
#
# De faculteit van een getal is gedefinieerd als n! = n * (n-1) * (n-2) * ... * 2 * 1, en 0! = 1 per definitie.
#
# Invoer
# Een geheel getal.
#
# Uitvoer
# De faculteit van het ingegeven getal (zonder return). Voor alle invoer kleiner dan 0 moet het programma 'onbepaald' teruggeven.
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
#
# Uitvoer:
# onbepaald
#
# Invoer:
# 0
#
# Uitvoer:
# 1