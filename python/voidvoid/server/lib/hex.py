
#class HexGrid:
#    def __init__(self):
#        pass

# Axial coordinate system
# https://www.redblobgames.com/grids/hexagons/#coordinates-axial
axial = {
    'n':  ( 0, -1 )
    's':  ( 0,  1 )
    'ne': ( 1, -1 )
    'nw': (-1,  0 )
    'sw': (-1,  1 )
    'se': ( 1,  1 )
}

# Map locations
locations = {
    (0, 0): "Center",
    (0, -1): "Up left"
}