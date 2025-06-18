getal = int(input())
array = []

while getal != 0:
    array.append(getal)
    getal = int(input())


if len(array) == 0:
    print("0 0", end="")
else:
    print(min(array), end=" ")
    print(max(array), end="")








# Lees gehele getallen (int) in tot je een nul krijgt. Druk daarop het kleinste en grootste ontvangen getal af gescheiden door een spatie (de nul reken je niet mee, je neemt ook geen nieuwe lijn). Bij een lege dataset (direct een 0) geef je twee nullen terug met een spatie ertussen.
#
# Invoer
# Een reeks gehele getallen afgesloten met een nul.
#
# Uitvoer
# Kleinste en grootste van alle ingelezen getallen, uitgezonderd de nul op het einde, gescheiden door een spatie. Er wordt ook geen nieuwe lijn genomen! Geef '0 0' terug in het geval meteen een nul wordt opgegeven.
#
# Voorbeeld
# Invoer:
# 1
# -2
# 3
# -4
# 0
#
# Uitvoer:
# -4 3 (geen nieuwe lijn)
#
# Invoer:
# 0
#
# Uitvoer:
# 0 0 (geen nieuwe lijn)