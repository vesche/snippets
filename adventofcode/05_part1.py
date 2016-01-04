from string import ascii_lowercase

def main():
    nice_count = 0
    bad_pairs = ['ab', 'cd', 'pq', 'xy']
    vowels = list('aeiou')

    with open("05_input.txt", 'r') as f:
        for s in f.read().splitlines():
            nice = True

            # bad pairs
            for pair in bad_pairs:
                if pair in s:
                    nice = False

            # 3 vowels
            vowel_count = 0
            for letter in s:
                if letter in vowels:
                    vowel_count += 1
            if vowel_count < 3:
                nice = False

            # two letters in a row
            count = 0
            for letter in ascii_lowercase:
                if letter * 2 in s:
                    count += 1
            if count == 0:
                nice = False

            # naughty or nice
            if nice:
                nice_count += 1

    return nice_count

if __name__ == "__main__":
    print main()
