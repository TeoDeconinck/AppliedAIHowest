basis = int(input())

while basis <= 0:
    basis = int(input())

if basis % 2 == 1:
    aantalAfTeDrukkenSterren = 1
    aantalAfTeDrukkenSpaties = basis // 2
else:
    aantalAfTeDrukkenSterren = 2
    aantalAfTeDrukkenSpaties = (basis - 1) // 2

while aantalAfTeDrukkenSterren <= basis:
    aantalAfgedrukteSpaties = 0
    while aantalAfgedrukteSpaties < aantalAfTeDrukkenSpaties:
        print(" ", end="")
        aantalAfgedrukteSpaties += 1

    aantalAfgedrukteSterren = 0
    while aantalAfgedrukteSterren < aantalAfTeDrukkenSterren:
        print("*", end="")
        aantalAfgedrukteSterren += 1

    print()

    aantalAfTeDrukkenSterren += 2
    aantalAfTeDrukkenSpaties -= 1
#
#     **
#    ****
#   ******
#  ********
# **********
#
#      *
#     ***
#    *****
#   *******
#  *********
# ***********

#
# aantalSterren = 0
# if hoogte % 2 != 0:
#     print("*", end="")
# else:
#     print("**", end="")
# print()
# if hoogte % 2 == 0:
#     aantalWhiteSpaces = hoogte // 2 - 1
# else:
#
#     aantalWhiteSpaces = hoogte // 2
# #
# # while aantalWhiteSpaces != 0:
# #     print("!", end="")
# #     aantalWhiteSpaces -=1
#
#
# while aantalSterren < aantalLijnen:
#
#     print("**", end="")
#     aantalSterren += 2
# # while aantalWhiteSpaces != 0:
# #     print(" ", end="")
# #     aantalWhiteSpaces -=1