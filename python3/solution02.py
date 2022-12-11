
def solve02_p1(input: list[str]) -> None:
    round_score = [[4, 8, 3], [1, 5, 9], [7, 2, 6]] # Precomputed matrix of all possible games - opponent's play x own play
    total_score = 0
    for game in input:
        opp, own = game.split(" ")
        opp_i, own_i = ord(opp) - ord('A'), ord(own) - ord('X')
        total_score += round_score[opp_i][own_i]
    print(total_score)

def solve02_p2(input: list[str]) -> None:
    round_score = [[3, 4, 8], [1, 5, 9], [2, 6, 7]] # Precomputed matrix of all possible games - opponent's play x outcome
    total_score = 0
    for game in input:
        opp, outcome = game.split(" ")
        opp_i, outcome_i = ord(opp) - ord('A'), ord(outcome) - ord('X')
        total_score += round_score[opp_i][outcome_i]
    print(total_score)

if __name__ == "__main__":
    with open("../inputs/input02.txt") as input_file:
        input = input_file.read().splitlines() # Strip trailing newlines
    print("Part 1 solution:")
    solve02_p1(input)
    print("\nPart 2 solution:")
    solve02_p2(input)
