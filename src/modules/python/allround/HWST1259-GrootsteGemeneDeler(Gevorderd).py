import math

grootste = int(input())
kleinste = int(input())

if kleinste > grootste:
    kleinste, grootste = grootste, kleinste

deler = kleinste
ggd = 0
found = False

while deler > math.sqrt(kleinste) and not found:
    if kleinste % deler == 0:
        if grootste % deler == 0:
            ggd = deler
            found = True
        else:
            complementaireDeler = kleinste // deler
            if grootste % complementaireDeler == 0:
                ggd = complementaireDeler
    deler -= 1

print (ggd, end='')

# HWST1259 - Grootste gemene deler (zwaar gevorderd!)
#
# Lees twee positieve gehele getallen in (er mag verondersteld worden dat beide getallen positief zullen zijn!). Geef de grootste deler die beide getallen gemeenschappelijk hebben, ook wel de grootste gemene deler of ggd genoemd. Je mag hiertoe het algoritme van Euclides NIET gebruiken. Doe dit bovendien zo efficiënt mogelijk. Gebruik geen tabellen. Geen nieuwe lijn op het einde!
#
# Tips:
#
# een deler van een getal levert als rest nul op, als je het getal erdoor deel.
# de helft van alle de delers van een getal ligt onder of op de vierkantwortel van het getal
# een vierkantswortel trekken kan in Python d.m.v. math.sqrt(getal). Schrijf hiertoe bovenaan je programma import math.
# de ggd zal steeds kleiner of gelijk zijn aan het kleinste van beide getallen.
# zoek vanaf het kleinste getal naar 1 naar gemeenschappelijke delers, de eerste die je tegenkomt zal meteen ook de grootste zijn, het programma mag in dat geval direct stoppen
# aangezien delers meer verspreid zijn naarmate ze groter worden, kan nog een optimalisatie zijn ze toch langs voor te zoeken. Zo weet je dat als 2 een deler is, de complementaire deler de tweede grootste zal zijn, enz ...
# als je een deler gevonden hebt in de bovenste helft van alle delers van het kleinste getal die niet gemeenschappelijk is met de delers van het grootste getal, dan kun je de overeenkomstige deler in de onderste helft alsnog controleren als zijnde een deler van het grootste getal. Indien zo bewaar je hem als sde voorlopig beste maar mag het programma niet meteen stoppen.
# Good luck!
#
# Invoer
# Twee gehele getallen waarvan het programma mag aannemen dat ze positief zijn.
#
# Uitvoer
# De grootste gemeenschappelijke deler van beide getallen.
#
# Voorbeelden
# Invoer:
# 225
# 15
#
# Uitvoer:
# 15
#
# Invoer:
# 15
# 12
#
# Uitvoer:
# 3