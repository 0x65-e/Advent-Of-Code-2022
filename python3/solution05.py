
def solve05_p1(input: list[str]) -> None:
    split = input.index("")
    crates = input[:split]
    num_stacks = len(list(filter(None, crates[-1].split(" "))))
    stacks = [ list() for _ in range(0, num_stacks) ]
    # Construct the initial stacks based on their position in the string
    for crate_line in crates[:-1]:
        for i in range(0, num_stacks):
            if crate_line[i*4:i*4+3].rstrip():
                stacks[i].append(crate_line[i*4:i*4+3])
    for stack in stacks:
        stack.reverse()
    # Apply operations in order
    for line in input[split+1:]:
        _, num, _, src, _, dest = line.split(" ")
        num, src, dest = int(num), int(src), int(dest)
        stacks[dest-1].extend(reversed(stacks[src-1][-num:])) # Reverse since moving 1-by-1
        del stacks[src-1][-num:]
    stack_top = [ stack[-1] for stack in stacks ]
    print(stack_top)

def solve05_p2(input: list[str]) -> None:
    split = input.index("")
    crates = input[:split]
    num_stacks = len(list(filter(None, crates[-1].split(" "))))
    stacks = [ list() for _ in range(0, num_stacks) ]
    # Construct the initial stacks based on their position in the string
    for crate_line in crates[:-1]:
        for i in range(0, num_stacks):
            if crate_line[i*4:i*4+3].rstrip():
                stacks[i].append(crate_line[i*4:i*4+3])
    for stack in stacks:
        stack.reverse()
    # Apply operations in order
    for line in input[split+1:]:
        _, num, _, src, _, dest = line.split(" ")
        num, src, dest = int(num), int(src), int(dest)
        stacks[dest-1].extend(stacks[src-1][-num:]) # Same thing, no reverse this time
        del stacks[src-1][-num:]
    stack_top = [ stack[-1] for stack in stacks ]
    print(stack_top)

if __name__ == "__main__":
    with open("../inputs/input05.txt") as input_file:
        input = input_file.read().splitlines() # Strip trailing newlines
    print("Part 1 solution:")
    solve05_p1(input)
    print("\nPart 2 solution:")
    solve05_p2(input)
