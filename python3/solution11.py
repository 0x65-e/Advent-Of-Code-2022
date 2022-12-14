from collections import deque
import operator

class Monkey:

    def __init__(self, op: str, test_divisor: int, destinations: tuple[int, int], starting_items: list[int], stress_management):
        self._test = Monkey._construct_test(op)
        self._test_divisor = test_divisor
        self._destinations = destinations
        self._inventory = deque()
        self._inventory.extend(starting_items)
        self._stress_management = stress_management
        self._inspected = 0

    def _construct_test(op: str):
        _, _, l_operand, op, r_operand = op.split(" ")

        if op == "+":
            op_fn = operator.add
        elif op == "*":
            op_fn = operator.mul
        else:
            raise Exception("Operation not + or *")

        if l_operand == "old" and r_operand == "old":
            return lambda old: op_fn(old, old)
        elif l_operand == "old":
            r_operand = int(r_operand)
            return lambda old: op_fn(old, r_operand)
        elif r_operand == "old":
            l_operand = int(l_operand)
            return lambda old: op_fn(l_operand, old)
        else:
            raise Exception("Error in operation formula, no old value")

    def take_turn(self) -> list[tuple[str, int]]:
        output = list()
        while self._inventory:
            item = self._inventory.popleft()
            new_item = self._test(item)
            new_item = self._stress_management(new_item)
            destination = self._destinations[0] if new_item % self._test_divisor == 0 else self._destinations[1]
            output.append((destination, new_item))
            self._inspected += 1
        return output

    def add_item(self, item: int) -> None:
        self._inventory.append(item)

    def get_inventory(self) -> list[int]:
        return list(self._inventory)

    def get_inspected_count(self) -> int:
        return self._inspected

def parse_monkeys(input: list[str], stress_fn) -> dict:
    monkeys = dict() # Python 3.7+ has ordered dictionaries by default. For Python 3.6 or below, use collections.OrderedDict
    # Parse monkeys
    for i in range(0, len(input), 7):
        monkey_name = input[i][7:-1]
        starting_inventory = map(int, input[i+1][18:].split(", "))
        op = input[i+2][13:]
        divisor = int(input[i+3][21:].rstrip())
        dest1 = input[i+4].rstrip().split(" ")[-1]
        dest2 = input[i+5].rstrip().split(" ")[-1]
        monkeys[monkey_name] = Monkey(op, divisor, (dest1, dest2), starting_inventory, stress_fn)
    return monkeys

def play_game(num_rounds: int, monkeys: dict) -> list[int]:
    for _ in range(num_rounds):
        for monkey in monkeys.values():
            items = monkey.take_turn()
            # Dispatch items to new monkeys
            for dest, item in items:
                monkeys[dest].add_item(item)
    inspected_counts = [ monkey.get_inspected_count() for monkey in monkeys.values() ]
    inspected_counts.sort()
    return inspected_counts

def solve11_p1(input: list[str]) -> None:
    monkeys = parse_monkeys(input, lambda stress: stress // 3)
    inspected_counts = play_game(20, monkeys)
    print("Monkeys: {}".format(inspected_counts))
    print("Monkey business: {}".format(inspected_counts[-2] * inspected_counts[-1]))

def solve11_p2(input: list[str]) -> None:
    big_modulus = 1 # Modulo is preserved under another, larger modulo as long as the smaller modulus is a factor of the larger one
    for i in range(3, len(input), 7):
        divisor = int(input[i][21:].rstrip())
        big_modulus *= divisor
    monkeys = parse_monkeys(input, lambda stress: stress % big_modulus)
    inspected_counts = play_game(10000, monkeys)
    print("Monkeys: {}".format(inspected_counts))
    print("Monkey business: {}".format(inspected_counts[-2] * inspected_counts[-1]))

if __name__ == "__main__":
    with open("../inputs/input11.txt") as input_file:
        input = input_file.read().splitlines() # Strip trailing newlines
    print("Part 1 solution:")
    solve11_p1(input)
    print("\nPart 2 solution:")
    solve11_p2(input)
