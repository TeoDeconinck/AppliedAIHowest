
getal = int(input())

if getal < 0:
    print('-', end="")
    getal = -getal

reversed = 0

while getal != 0:
    reversed = reversed * 10 + getal % 10
    getal = getal //10

print(reversed, end="")



# HWST1242 - Cijferwissel volledig
#
# Lees een geheel getal in (int). Schrijf het getal van achter naar voren. Neem daarbij geen nieuwe lijn. Teken blijft bewaard.
#
# Invoer
# Een geheel getal.
#
# Uitvoer
# Het getal maar met de cijfers van achter naar voor, inclusief teken.
#
# Voorbeelden
# Invoer:
# 1234
#
# Uitvoer:
# 4321
#
# Invoer:
# -1234
#
# Uitvoer:
# -4321
#
# Invoer:
# 0
#
# Uitvoer:
# 0
#
# Invoer:
# -6
#
# Uitvoer:
# -6
#
# Invoer:
# 4
#
# Uitvoer:
# 4