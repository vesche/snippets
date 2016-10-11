# -*- coding: utf-8 -*-

# +---------------+
# |      ...      |
# |      .G.      |
# |   .........   |
# |   .F.   .C.   |
# |......   ......|
# |WF.    .    EF.|
# |......   ......|
# |   .L.   .P.   |
# |   .........   |
# |      .D.      |
# |      ...      |
# +---------------+


def ringtext(x, y):
    text = ' '
    message =   "|{0: <15}|\n" \
                "+---------------+"

    if (7 <= x <= 9) and (3 <= y <= 5):
        text += "Garden"

    elif (4 <= x <= 6) and (5 <= y <= 7):
        text += "Forest"

    elif (10 <= x <= 12) and (5 <= y <= 7):
        text += "City"

    elif (1 <= x <= 3) and (7 <= y <= 9):
        text += "West Fountain"

    elif (13 <= x <= 15) and (7 <= y <= 9):
        text += "East Fountain"

    #if (x, y) == (7, 3):
    #    return "garden 0"
    #elif (x, y) == (8, 3):
    #    return "garden 1"
    #elif (x, y) == (9, 3):
    #    return "garden 2"

    return message.format(text)
