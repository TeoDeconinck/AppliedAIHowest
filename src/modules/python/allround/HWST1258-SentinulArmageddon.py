array = []

while len(array) < 10:
    getal = int(input())
    if getal == 0:
        break
    array.append(getal)

if len(array) == 0:
    print("0 0", end="")
else:
    print(array.index(min(array)) +1, end=" ")
    print(array.index(max(array)) +1, end="")

#
# HWST1258 - Sentinul Armageddon
#
# Lees gehele getallen (int) in tot je een nul krijgt of tot je er 10 hebt. Druk daarop het volgnummer van het kleinste en grootste ontvangen getal af gescheiden door een spatie (volgnummers beginnen bij 1, een eventuele nul reken je niet mee, je neemt ook geen nieuwe lijn). Bij een lege dataset (direct een 0) geef je twee nullen terug met een spatie ertussen.
#
# Invoer
# Een reeks gehele getallen afgesloten met een nul of maximaal 10 gehele getallen.
#
# Uitvoer
# Volgnummer van kleinste en grootste van alle ingelezen getallen, uitgezonderd de eventuele nul op het einde, gescheiden door een spatie. Er wordt ook geen nieuwe lijn genomen! Geef '0 0' terug in het geval meteen een nul wordt opgegeven.
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
# 4 3 (geen nieuwe lijn)
#
# Invoer:
# 0
#
# Uitvoer:
# 0 0 (geen nieuwe lijn)