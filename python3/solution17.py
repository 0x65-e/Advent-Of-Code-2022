
def move(board: list[list[bool]], rock: tuple[int, int], type: int, direction: str) -> tuple[bool, tuple[int, int]]:
    rock_types = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (1, 0), (0, 1), (1, 1)]
    ]
    # Try move
    rock_x, rock_y = rock
    if direction == '<':
        rock_x -= 1
    elif direction == '>':
        rock_x += 1
    elif direction == 'v':
        rock_y -= 1
    blocked = False
    for delta_x, delta_y in rock_types[type]:
        x, y = rock_x + delta_x, rock_y + delta_y
        while y >= len(board):
            board.append([ False ] * 7)
        if x >= 0 and x < 7 and not board[y][x]:
            continue
        blocked = True
        break
    if blocked:
        rock_x, rock_y = rock # Restore old position
        # If can't fall, this is the final resting place for the rock
        if direction == 'v':
            for delta_x, delta_y in rock_types[type]:
                x, y = rock_x + delta_x, rock_y + delta_y
                board[y][x] = True
    return (blocked, (rock_x, rock_y))

def get_top_of_board(board: list[list[bool]]) -> int:
    for i, row in enumerate(reversed(board), 1):
        if any(row):
            return len(board) - i
    raise Exception("No top of board")

def get_bottom_of_board(board: list[list[bool]]) -> int:
    counters = [ False ] * 7
    for i, row in enumerate(reversed(board), 1):
        for j in range(7):
            counters[j] |= row[j]
        if all(counters):
            return len(board) - i
    raise Exception("No bottom of board")

def is_top_row_full(board: list[list[bool]]) -> int:
    for i, row in enumerate(reversed(board), 1):
        if any(row):
            return all(row)

def print_board(board: list[list[bool]]) -> None:
    for row in reversed(board):
        print('|' + "".join(['#' if e else '.' for e in row ]) + '|')

def solve17_p1(input: list[str]) -> None:
    input = input[0] # One line
    board = [ [ True ] * 7 ]
    rock = (2, 4)
    num_rocks = 0
    i = 0
    while num_rocks < 2022:
        _, rock = move(board, rock, num_rocks % 5, input[i])
        blocked, rock = move(board, rock, num_rocks % 5, 'v')
        if blocked:
            rock = (2, get_top_of_board(board) + 4)
            num_rocks += 1
        i = (i + 1) % len(input)
    print(get_top_of_board(board))

def solve17_p2(input: list[str]) -> None:
    input = input[0] # One line
    board = [ [ True ] * 7 ]
    offset = 0
    rock = (2, 4)
    num_rocks = 0
    i = 0
    while num_rocks < 1_000_000_000_000:
        _, rock = move(board, rock, num_rocks % 5, input[i])
        blocked, rock = move(board, rock, num_rocks % 5, 'v')
        i = (i + 1) % len(input)
        if blocked:
            #cutoff = get_bottom_of_board(board)
            #board = board[cutoff:]
            #offset += cutoff
            rock = (2, get_top_of_board(board) + 4)
            num_rocks += 1
    print(offset + get_top_of_board(board))

if __name__ == "__main__":
    with open("../inputs/input17.txt") as input_file:
        input = input_file.read().splitlines() # Strip trailing newlines
    print("Part 1 solution:")
    solve17_p1(input)
    print("\nPart 2 solution:")
    solve17_p2(input)
