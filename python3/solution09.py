
def unique_positions(input: list[str], num_knots: int) -> None:
    knots = [ [0, 0] for _ in range(num_knots) ]
    visited = set()
    visited.add((knots[-1][0], knots[-1][1]))
    for line in input:
        dir, steps = line.split(" ")
        steps = int(steps)
        for _ in range(steps):
            if dir == "U":
                knots[0][1] += 1
            elif dir == "R":
                knots[0][0] += 1
            elif dir == "D":
                knots[0][1] -= 1
            elif dir == "L":
                knots[0][0] -= 1
            for i in range(1, num_knots):
                if abs(knots[i-1][0] - knots[i][0]) > 1 or abs(knots[i-1][1] - knots[i][1]) > 1:
                    knots[i][0] += max(min(knots[i-1][0] - knots[i][0], 1), -1)
                    knots[i][1] += max(min(knots[i-1][1] - knots[i][1], 1), -1)
                else:
                    break
            visited.add((knots[-1][0], knots[-1][1]))
    print("Unique positions: {}".format(len(visited)))

def solve09_p1(input: list[str]) -> None:
    unique_positions(input, 2)

def solve09_p2(input: list[str]) -> None:
    unique_positions(input, 10)

if __name__ == "__main__":
    with open("../inputs/input09.txt") as input_file:
        input = input_file.read().splitlines() # Strip trailing newlines
    print("Part 1 solution:")
    solve09_p1(input)
    print("\nPart 2 solution:")
    solve09_p2(input)
