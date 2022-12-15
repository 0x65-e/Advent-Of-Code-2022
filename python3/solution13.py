from functools import cmp_to_key
from typing import Optional

def parse(input: str) -> tuple[list, str]:
    assert input[0] == '[',"Input does not start with a list"
    out = list()
    register = 0
    in_digit = False
    i = 1
    while i < len(input):
        if input[i].isdigit():
            register = 10 * register + int(input[i])
            in_digit = True
            i += 1
        elif input[i] == ',':
            out.append(register)
            register = 0
            in_digit = False
            i += 1
        elif input[i] == '[':
            sublist, input = parse(input[i:])
            out.append(sublist)
            i = 1 if input[0] == ',' else 0
        elif input[i] == ']':
            if in_digit:
                out.append(register)
            return (out, input[i+1:])
        else:
            raise Exception("Unknown element")
    raise Exception("No closing brackets")

def compare(left: list, right: list) -> Optional[bool]:
    left_shorter = len(left) < len(right)
    same_length = len(left) == len(right)
    for left_elem, right_elem in zip(left, right):
        if type(left_elem) is int and type(right_elem) is int:
            if left_elem != right_elem:
                return left_elem < right_elem
        else:
            if type(left_elem) is int:
                left_elem = [ left_elem ]
            elif type(right_elem) is int:
                right_elem = [ right_elem ]
            result = compare(left_elem, right_elem)
            if result != None:
                return result
    return None if same_length else left_shorter

def cmp_int(left: list, right: list) -> int:
    result = compare(left, right)
    if result == None:
        return 0
    return 1 if result else -1

def solve13_p1(input: list[str]) -> None:
    out = list()
    for i in range(0, len(input), 3):
        left, right = parse(input[i]), parse(input[i+1])
        assert left[1] == '',"Characters remaining after parse"
        assert right[1] == '',"Characters remaining after parse"
        if compare(left, right):
            out.append((i//3)+1)
    print(out)
    print("Sum: {}".format(sum(out)))

def solve13_p2(input: list[str]) -> None:
    DIVIDER_PACKET_1 = [[2]]
    DIVIDER_PACKET_2 = [[6]]
    packets = list()
    for i in range(0, len(input), 3):
        packets.append(parse(input[i])[0]) # Skip assert since it's checked in p1
        packets.append(parse(input[i+1])[0])
    packets.append(DIVIDER_PACKET_1)
    packets.append(DIVIDER_PACKET_2)
    packets.sort(key=cmp_to_key(cmp_int), reverse=True)
    index_1 = packets.index(DIVIDER_PACKET_1) + 1
    index_2 = packets.index(DIVIDER_PACKET_2) + 1
    print("Indices: {} {}".format(index_1, index_2))
    print(index_1 * index_2)

if __name__ == "__main__":
    with open("../inputs/input13.txt") as input_file:
        input = input_file.read().splitlines() # Strip trailing newlines
    print("Part 1 solution:")
    solve13_p1(input)
    print("\nPart 2 solution:")
    solve13_p2(input)
