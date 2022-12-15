
def construct_board(input: list[str], with_floor: bool) -> tuple[list[list[bool]], int, int, int]:
    min_x, max_x, max_y = float("inf"), 0, 0
    segments = list()
    for line in input:
        vertices = list()
        coordinates = line.split(" -> ")
        for coord in coordinates:
            x, y = map(int, coord.split(","))
            vertices.append((x, y))
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        segments.append(vertices)
    max_y += 2
    x_border = max_y if with_floor else 1 # Slight overestimation in the case with a floor, but not by much
    max_x += x_border
    min_x -= x_border
    board = [ [ False ] * (max_x - min_x + 1) for _ in range(max_y+1) ]
    for segment in segments:
        for v1, v2 in zip(segment, segment[1:]):
            if v1[0] == v2[0]:
                start_y, end_y = min(v1[1], v2[1]), max(v1[1], v2[1])
                for y in range(start_y, end_y + 1):
                    board[y][v1[0]-min_x] = True
            else:
                start_x, end_x = min(v1[0], v2[0]), max(v1[0], v2[0])
                for x in range(start_x, end_x + 1):
                    board[v1[1]][x-min_x] = True
    if with_floor:
        for x in range(min_x, max_x+1):
            board[max_y][x-min_x] = True
    return (board, min_x, max_x, max_y)

def solve14_p1(input: list[str]) -> None:
    START_POS = (500, 0)
    board, min_x, max_x, max_y = construct_board(input, False)
    step = 0
    sand_x, sand_y = START_POS
    prev_pos = list() # optimization - start at most recent unblocked position since the next grain will follow the same path to there
    while True:
        if sand_x == min_x or sand_x == max_x or sand_y == max_y:
            break
        # Try moving all three directions
        next_row = board[sand_y+1]
        if not next_row[sand_x-min_x]:
            prev_pos.append((sand_x, sand_y))
            sand_y += 1
            continue
        if not next_row[sand_x-min_x-1]:
            prev_pos.append((sand_x, sand_y))
            sand_x -= 1
            sand_y += 1
            continue
        if not next_row[sand_x-min_x+1]:
            prev_pos.append((sand_x, sand_y))
            sand_x += 1
            sand_y += 1
            continue
        # Can't move, come to rest
        board[sand_y][sand_x-min_x] = True
        sand_x, sand_y = prev_pos.pop()
        step += 1
    print(step)

def solve14_p2(input: list[str]) -> None:
    START_POS = (500, 0)
    board, min_x, max_x, max_y = construct_board(input, True)
    step = 0
    sand_x, sand_y = START_POS
    prev_pos = list()
    while True:
        # Try moving all three directions
        next_row = board[sand_y+1]
        if not next_row[sand_x-min_x]:
            prev_pos.append((sand_x, sand_y))
            sand_y += 1
            continue
        if not next_row[sand_x-min_x-1]:
            prev_pos.append((sand_x, sand_y))
            sand_x -= 1
            sand_y += 1
            continue
        if not next_row[sand_x-min_x+1]:
            prev_pos.append((sand_x, sand_y))
            sand_x += 1
            sand_y += 1
            continue
        # Can't move, come to rest
        board[sand_y][sand_x-min_x] = True
        step += 1
        if (sand_x, sand_y) == START_POS:
            break
        sand_x, sand_y = prev_pos.pop()
    print(step)

if __name__ == "__main__":
    with open("../inputs/input14.txt") as input_file:
        input = input_file.read().splitlines() # Strip trailing newlines
    print("Part 1 solution:")
    solve14_p1(input)
    print("\nPart 2 solution:")
    solve14_p2(input)
