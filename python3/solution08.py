
def solve08_p1(input: list[str]) -> None:
    matrix = [ list(map(int, line)) for line in input ]
    visible_matrix = [ [ 0 ] * len(line) for line in input ]
    # Rows
    for i, row in enumerate(matrix):
        max_height = -1
        for j, height in enumerate(row):
            if height > max_height:
                max_height = height
                visible_matrix[i][j] = 1
        max_height = -1
        for j, height in enumerate(reversed(row), start=1):
            if height > max_height:
                max_height = height
                visible_matrix[i][-j] = 1
    # Columns
    for j in range(0, len(matrix[0])):
        max_height = -1
        for i in range(0, len(matrix)):
            if matrix[i][j] > max_height:
                max_height = matrix[i][j]
                visible_matrix[i][j] = 1
        max_height = -1
        for i in range(len(matrix)-1,-1,-1):
            if matrix[i][j] > max_height:
                max_height = matrix[i][j]
                visible_matrix[i][j] = 1
    print("Visible trees: {}".format(sum([ sum(row) for row in visible_matrix ])))

def solve08_p2(input: list[str]) -> None:
    matrix = [ list(map(int, line)) for line in input ]
    sight_matrix = [ [ 1 ] * len(line) for line in input ]
    # Rows
    for i, row in enumerate(matrix):
        # Hold a "stack" of descending tree heights that may block line of sight
        tree_stack = [ (float("inf"), 0) ]
        for j, height in enumerate(row):
            # Remove trees that this tree will "shadow" by being taller
            while height > tree_stack[-1][0]:
                tree_stack.pop()
            # Calculate distance to next tree at least as high as this one
            sight_matrix[i][j] *= j - tree_stack[-1][1]
            # This tree also shadows equal height trees (but they block its line of sight)
            while height == tree_stack[-1][0]:
                tree_stack.pop()
            # Add this tree to the stack
            tree_stack.append((height, j))
        tree_stack = [ (float("inf"), len(row)-1) ]
        for j, height in enumerate(reversed(row), start=1):
            while height > tree_stack[-1][0]:
                tree_stack.pop()
            sight_matrix[i][-j] *= tree_stack[-1][1] - len(row) + j
            while height == tree_stack[-1][0]:
                tree_stack.pop()
            tree_stack.append((height, len(row)-j))
    # Columns
    for j in range(0, len(matrix[0])):
        tree_stack = [ (float("inf"), 0) ]
        for i in range(0, len(matrix)):
            while matrix[i][j] > tree_stack[-1][0]:
                tree_stack.pop()
            sight_matrix[i][j] *= i - tree_stack[-1][1]
            while matrix[i][j] == tree_stack[-1][0]:
                tree_stack.pop()
            tree_stack.append((matrix[i][j], i))
        tree_stack = [ (float("inf"), len(matrix)-1) ]
        for i in range(len(matrix)-1,-1,-1):
            while matrix[i][j] > tree_stack[-1][0]:
                tree_stack.pop()
            sight_matrix[i][j] *= tree_stack[-1][1] - i
            tree_stack.append((matrix[i][j], i))
    print("Best tree: {}".format(max([ max(row) for row in sight_matrix ])))

if __name__ == "__main__":
    with open("../inputs/input08.txt") as input_file:
        input = input_file.read().splitlines() # Strip trailing newlines
    print("Part 1 solution:")
    solve08_p1(input)
    print("\nPart 2 solution:")
    solve08_p2(input)
