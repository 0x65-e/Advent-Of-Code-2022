
def solve10_p1(input: list[str]) -> None:
    signal_strengths = list()
    clock = 0
    register = 1
    for operation in input:
        if operation.startswith("addx"):
            clock += 2
            if clock % 40 == 20 or clock % 40 == 21:
                signal_strengths.append((10 * (clock // 10) * register))
            register += int(operation[5:])
        else:
            clock += 1
            if clock % 40 == 20:
                signal_strengths.append(clock * register)
    print(signal_strengths[:6])
    print("Sum: {}".format(sum(signal_strengths[:6])))

def solve10_p2(input: list[str]) -> None:
    display = [ ['.'] * 40 for _ in range(6) ]
    clock = 0
    register = 1
    for operation in input:
        if operation.startswith("addx"):
            for _ in range(2):
                if abs(clock % 40 - register) <= 1:
                    display[clock // 40][clock % 40] = '#'
                clock += 1
            register += int(operation[5:])
        else:
            if abs(clock % 40 - register) <= 1:
                display[clock // 40][clock % 40] = '#'
            clock += 1
    print("\n".join([ "".join(line) for line in display ]))

if __name__ == "__main__":
    with open("../inputs/input10.txt") as input_file:
        input = input_file.read().splitlines() # Strip trailing newlines
    print("Part 1 solution:")
    solve10_p1(input)
    print("\nPart 2 solution:")
    solve10_p2(input)
