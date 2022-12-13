
def solve04_p1(input: list[str]) -> None:
    total_overlaps = 0
    for line in input:
        task1, task2 = line.split(",")
        start1, end1 = task1.split("-")
        start2, end2 = task2.split("-")
        start1, end1, start2, end2 = int(start1), int(end1), int(start2), int(end2)
        if start1 <= start2 and end1 >= end2:
            total_overlaps += 1
        elif start2 <= start1 and end2 >= end1:
            total_overlaps += 1
    print(total_overlaps)

def solve04_p2(input: list[str]) -> None:
    total_overlaps = 0
    for line in input:
        task1, task2 = line.split(",")
        start1, end1 = task1.split("-")
        start2, end2 = task2.split("-")
        start1, end1, start2, end2 = int(start1), int(end1), int(start2), int(end2)
        if end1 >= start2 and end1 <= end2:
            total_overlaps += 1
        elif end2 >= start1 and end2 <= end1:
            total_overlaps += 1
    print(total_overlaps)

if __name__ == "__main__":
    with open("../inputs/input04.txt") as input_file:
        input = input_file.read().splitlines() # Strip trailing newlines
    print("Part 1 solution:")
    solve04_p1(input)
    print("\nPart 2 solution:")
    solve04_p2(input)
