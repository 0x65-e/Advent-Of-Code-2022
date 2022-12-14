from collections import deque
from typing import Optional

def construct_heightmap(input: list[str]) -> tuple[list[int], tuple[int, int], tuple[int, int]]:
    heightmap = list()
    for i, row in enumerate(input):
        heightrow = list()
        for j, char in enumerate(row):
            if char == 'S':
                start = (i, j)
                heightrow.append(0)
            elif char == 'E':
                dest = (i, j)
                heightrow.append(25)
            else:
                heightrow.append(ord(char) - ord('a'))
        heightmap.append(heightrow)
    return (heightmap, start, dest)

def bfs_board(start, visited, goal_condition, explore_condition) -> tuple[Optional[tuple[int, int]], int]:
    visited[start[0]][start[1]] = True
    max_i, max_j = len(visited), len(visited[0])
    step = 0
    explore_q = deque()
    explore_q.append(start)
    explore_q.append(None)
    goal_reached = None
    while explore_q:
        next_step = explore_q.popleft()
        if next_step == None:
            step += 1
            explore_q.append(None)
        else:
            i, j = next_step
            if goal_condition(i, j):
                goal_reached = (i, j)
                break
            for test_i, test_j in [(i-1,j), (i,j-1), (i+1,j), (i,j+1)]:
                if test_i >= 0 and test_j >= 0 and test_i < max_i and test_j < max_j:
                    if not visited[test_i][test_j] and explore_condition(i, j, test_i, test_j):
                        visited[test_i][test_j] = True
                        explore_q.append((test_i, test_j))
    return (goal_reached, step)

def solve12_p1(input: list[str]) -> None:
    heightmap, start, end = construct_heightmap(input)
    visited = [ [ False ] * len(row) for row in heightmap ]
    goal, steps = bfs_board(start, visited, lambda i, j: (i, j) == end, lambda i, j, test_i, test_j: heightmap[test_i][test_j] <= heightmap[i][j] + 1)
    if goal == None:
        raise Exception("No complete path")
    print(steps)

def solve12_p2(input: list[str]) -> None:
    heightmap, _, start = construct_heightmap(input)
    visited = [ [ False ] * len(row) for row in heightmap ]
    goal, steps = bfs_board(start, visited, lambda i, j: heightmap[i][j] == 0, lambda i, j, test_i, test_j: heightmap[test_i][test_j] >= heightmap[i][j] - 1)
    if goal == None:
        raise Exception("No complete path")
    print(steps)

if __name__ == "__main__":
    with open("../inputs/input12.txt") as input_file:
        input = input_file.read().splitlines() # Strip trailing newlines
    print("Part 1 solution:")
    solve12_p1(input)
    print("\nPart 2 solution:")
    solve12_p2(input)
