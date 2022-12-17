import functools

MAX_VALVES = 0
CONN_MAP = dict()
RATE_MAP = dict()

def setup_dp(input: list[str]):
    global MAX_VALVES
    num_useful_valves = 0
    for line in input:
        this_valve, connections = line.split("; ")
        valve_name = this_valve[6:8]
        flow_rate = int(this_valve[this_valve.index("=")+1:])
        RATE_MAP[valve_name] = (flow_rate, num_useful_valves)
        if flow_rate != 0:
            num_useful_valves += 1
        if connections[21] == 's':
            connections = connections[23:].split(", ")
        else:
            connections = connections[22:].split(", ")
        CONN_MAP[valve_name] = connections
    MAX_VALVES = 2 ** (num_useful_valves) - 1

@functools.cache
def dp(node: str, open_valves: int, time_remaining: int) -> int:
    if open_valves == MAX_VALVES: # Shortcut when all useful valves are already open
        return 0
    if time_remaining <= 1:
        return 0
    rate, node_num = RATE_MAP[node]
    conns = CONN_MAP[node]
    best = 0
    for next_node in conns:
        # Move to another node
        future_reward = dp(next_node, open_valves, time_remaining - 1)
        best = max(best, future_reward)
    # If the valve is turnable:
    if rate != 0 and (open_valves & 2 ** node_num == 0):
        # Turn on this valve and then move
        new_valves = open_valves | 2 ** node_num
        reward = rate * (time_remaining - 1)
        for next_node in conns:
            future_reward = dp(next_node, new_valves, time_remaining - 2)
            best = max(best, reward + future_reward)
    return best

def solve16_p1() -> None:
    print(dp('AA', 0, 30))

def solve16_p2() -> None:
    global MAX_VALVES
    best = 0
    # The game with two players is really just two simultaneous single-player games with disjoint sets of valves
    # ... which can use the same implementation as part 1 and benefit from the existing cache
    # Still takes about a minute and a half, so it could be optimized further, but it sure beats a solution that runs for several hours
    for elephant in range(MAX_VALVES // 2 + 1): # divide by 2 since the second half is the same values but swapped
        best = max(best, dp('AA', elephant, 26) + dp('AA', MAX_VALVES ^ elephant, 26))
    print(best)

if __name__ == "__main__":
    with open("../inputs/input16.txt") as input_file:
        input = input_file.read().splitlines() # Strip trailing newlines
    setup_dp(input)
    print("Part 1 solution:")
    solve16_p1()
    print("\nPart 2 solution:")
    solve16_p2()
