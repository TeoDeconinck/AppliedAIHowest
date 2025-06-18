# def faculteit(n):
#     resultaat = 1
#     for i in range(1, n + 1):
#         resultaat *= i
#     return resultaat
#
#
# n = int(input())
# k = int(input())
#
# if k >= n or n <= 0:
#     print("onbepaald", end="")
# else:
#     variatie = faculteit(n) / faculteit(n - k)
#     print(int(variatie), end="")
#



n = int(input())
k = int(input())

var = 1
i = n
while i > n-k:
    var = var * i
    i -= 1

if n >= k and k >= 0:
    print(int(var), end="")
else:
    print("onbepaald", end="")



# HWST1256 - Leve de variatie
#
# Pikken we k unieke elementen uit een totaal van n elementen, waarbij we de volgorde bewaren, dan noemen we dit een variatie. De combinatoriek levert ons het aantal mogelijke unieke volgordes (dus zonder herhaling) van k uit n elementen gegeven wordt als:
#
# (n)k = n!/(n-k)! waarbij ! staat voor faculteit
#
# Zijnde de faculteit van het totaal, gedeeld door de faculteit van de rest.
#
# Gevraagd wordt een programma te schrijven dat, gegeven n en k het aantal variaties van k uit n elementen berekent. Als een van beide getallen negatief is of k>n dan druk je 'onbepaald' af.
#
# OPGELET: Het is bij deze oefening belangrijk dat je het aantal bewerkingen minimaliseert!
#
# Invoer
# Twee positieve gehele getallen, waarbij de tweede (k) kleiner of gelijk is aan de eerste (n).
#
# Uitvoer
# Het aantal variaties als n>=k>=0. In elk ander geval wordt de boodschap 'onbepaald' afgedrukt. Het programma neemt nooit een nieuwe lijn.
#
# Voorbeelden
# Invoer:
# 10
# 2
#
# Uitvoer:
# 90
#
# Invoer:
# -6
# -10
#
# Uitvoer:
# onbepaald
#
# Invoer:
# 0
# 0
#
# Uitvoer:
# 1
#
# Invoer:
# 9
# 13
#
# Uitvoer:
# onbepaald