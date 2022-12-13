from collections import defaultdict

def solve06_p1(input: list[str]) -> None:
    char_count = defaultdict(int)
    for i, char in enumerate(input[0]):
        char_count[char] += 1
        # Remove old character
        if i >= 4:
            char_count[input[0][i-4]] -= 1
            if char_count[input[0][i-4]] == 0:
                del char_count[input[0][i-4]]
        # Check if all unique
        if i >= 3:
            if len(char_count) == 4:
                print(i+1)
                break

def solve06_p2(input: list[str]) -> None:
    char_count = defaultdict(int)
    for i, char in enumerate(input[0]):
        char_count[char] += 1
        # Remove old character
        if i >= 14:
            char_count[input[0][i-14]] -= 1
            if char_count[input[0][i-14]] == 0:
                del char_count[input[0][i-14]]
        # Check if all unique
        if i >= 13:
            if len(char_count) == 14:
                print(i+1)
                break

if __name__ == "__main__":
    with open("../inputs/input06.txt") as input_file:
        input = input_file.read().splitlines() # Strip trailing newlines
    print("Part 1 solution:")
    solve06_p1(input)
    print("\nPart 2 solution:")
    solve06_p2(input)
