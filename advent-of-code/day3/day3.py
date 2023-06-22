priorities = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52
}


SUM = 0

with open("input.txt") as f:
    lines = f.read().splitlines()

    for line in lines:
        # First, split the rucksack input into the two compartments
        middle_index = int(len(line) / 2)

        print(f"Got middle index of {middle_index} for input {line}")

        first_half = line[:middle_index]
        second_half = line[middle_index:]

        first = list(first_half)
        second = list(second_half)

        common_element = set(first).intersection(second)

        common_element_str = ', '.join(common_element)

        if common_element_str is not '':
            priority = priorities[common_element_str]

            SUM += priority

        print(
            f"Common element {common_element} exists in both lists, with a priority of {priority}")

        print(
            f"Got first_half {first} and second_half {second} for input: {line}")
print(f"Sum is {SUM}")
