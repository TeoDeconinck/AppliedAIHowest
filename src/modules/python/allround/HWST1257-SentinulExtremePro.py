array = []

while len(array) < 10:
    getal = int(input())
    if getal == 0:
        break
    array.append(getal)

if len(array) == 0:
    print("0 0", end="")
else:
    print(min(array), end=" ")
    print(max(array), end="")

#
# HWST1257 - Sentinul Extreme Pro
#
# Lees gehele getallen (int) in tot je een nul krijgt of tot je er 10 hebt. Druk daarop het kleinste en grootste ontvangen getal af gescheiden door een spatie (een eventuele nul reken je niet mee, je neemt ook geen nieuwe lijn). Bij een lege dataset (direct een 0) geef je twee nullen terug met een spatie ertussen.
#
# Invoer
# Een reeks gehele getallen afgesloten met een nul of maximaal 10 gehele getallen.
#
# Uitvoer
# Kleinste en grootste van alle ingelezen getallen, uitgezonderd de eventuele nul op het einde, gescheiden door een spatie. Er wordt ook geen nieuwe lijn genomen! Geef '0 0' terug in het geval meteen een nul wordt opgegeven.
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