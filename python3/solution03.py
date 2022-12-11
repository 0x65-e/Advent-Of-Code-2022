
def solve03_p1(input: list[str]) -> None:
    total_priority = 0
    for line in input:
        half = len(line) // 2
        item = list(set(line[:half]) & set(line[half:]))[0]
        if item.islower():
            total_priority += 1 + ord(item) - ord('a')
        else:
            total_priority += 27 + ord(item) - ord('A')
    print(total_priority)

def solve03_p2(input: list[str]) -> None:
    total_priority = 0
    for i in range(0, len(input), 3):
        badge = list(set(input[i]) & set(input[i+1]) & set(input[i+2]))[0]
        if badge.islower():
            total_priority += 1 + ord(badge) - ord('a')
        else:
            total_priority += 27 + ord(badge) - ord('A')
    print(total_priority)

if __name__ == "__main__":
    with open("../inputs/input03.txt") as input_file:
        input = input_file.read().splitlines() # Strip trailing newlines
    print("Part 1 solution:")
    solve03_p1(input)
    print("\nPart 2 solution:")
    solve03_p2(input)
