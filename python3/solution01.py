
def solve01_p1(input: list[str]) -> None:
    max_cal = 0
    curr_cal = 0
    for line in input:
        if not line:
            max_cal = max(max_cal, curr_cal)
            curr_cal = 0
        else:
            curr_cal += int(line)
    max_cal = max(max_cal, curr_cal) # Handle the final list, which might not end with an empty line
    print(max_cal)

def solve01_p2(input: list[str]) -> None:
    cal = []
    curr_cal = 0
    for line in input:
        if not line:
            cal.append(curr_cal)
            curr_cal = 0
        else:
            curr_cal += int(line)
    if curr_cal:
        cal.append(curr_cal) # Handle the final list, which might not end with an empty line
    cal.sort()
    print("Top 3: " + str(cal[-3:]))
    print("Total: " + str(sum(cal[-3:])))

if __name__ == "__main__":
    with open("../inputs/input01.txt") as input_file:
        input = input_file.read().splitlines() # Strip trailing newlines
    print("Part 1 solution:")
    solve01_p1(input)
    print("\nPart 2 solution:")
    solve01_p2(input)
