def main():
    encoded, literal = 0, 0

    with open("08_input.txt") as f:
        lines = f.read().splitlines()

    for line in lines:
        extra = 4
        for char in line[1:-1]:
            if char == "\\" or char == '"':
                extra += 1

        encoded += len(line) + extra
        literal += len(line)

    return encoded - literal

if __name__ == "__main__":
    print main()
