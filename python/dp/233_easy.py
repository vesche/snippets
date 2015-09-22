brick, door, edge, roof_left, roof_right, tip, window = '-', '|', '+', '/', \
'\\', 'A', 'o'

house_space = 's'
space = door_space = void = ' '

blueprint = []
house = []

def funky_width(n):
    return n*5-(n-1)

def main():
    # save blueprint
    for _ in range(input()):
        blueprint.append(raw_input())
        house.append([])
    
    # create empty house
    max_width = funky_width(len(blueprint[-1]))
    for li in house:
        for _ in range(max_width):
            li.append(void)
    
    # throw down some brick yo
    for line in range(len(blueprint)):
        for char in range(len(blueprint[line])):
            if blueprint[line][char] == '*':
                house[line][funky_width(char):funky_width(char+1)] = [edge, \
                brick, brick, brick, edge]

    # scrap inners
    for line in range(len(house)):
        for char in range(len(house[line])):
            try:
                # strip bricks
                if (house[line][char] == brick) and (line != 0) and \
                (house[line-1][char] in [brick, house_space]):
                    house[line][char] = house_space
                # strip edges
                if (house[line][char] == edge) and (line != 0) and \
                (house[line][char-1] == house[line][char+1]):
                    #raw_input(house[line][char-1])
                    #raw_input(house[line][char+1])
                    house[line][char] = house[line][char+1]
            except:
                continue
    
    for line in house:
        print ''.join(line)
    
        
if __name__ == "__main__":
    main()