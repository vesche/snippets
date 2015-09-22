brick, door, edge, roof_left, roof_right, tip, window = '-', '|', '+', '/', \
'\\', 'A', 'o'

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
    
    # drop edges and bricks
    for line in range(len(blueprint)):
        for char in range(len(blueprint[line])):
            try:
                if blueprint[line][char]=='*' and blueprint[line-1][char]!='*':
                    house[line][funky_width(char)] = '+'
                    house[line][funky_width(char+1)] = '+'
            except:
                continue
    
    for line in house:
        print ''.join(line)
    
        
if __name__ == "__main__":
    main()