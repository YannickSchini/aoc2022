from argparse import ArgumentParser, FileType
from monkey import Monkey

if __name__ == "__main__":
    parser = ArgumentParser(prog="monkey_business", description="Model monkey behavior to get our stuff back")
    parser.add_argument("filename", type=FileType("r"))
    args = parser.parse_args()

    with args.filename as f:
        raw_monkeys = f.read().split("\n\n")

    monkeys = []
    for raw_monkey in raw_monkeys:
        monkeys.append(Monkey(raw_monkey.split("\n")))

    for round in range(10000):
        for monkey in monkeys:
            # print(f"\n\n Monkey {monkey.name}’s turn with the following items !!\n{monkey.starting_items}")
            monkey.turn()

    monkey_business_list = [monkey.number_of_inspections for monkey in monkeys]
    monkey_business_list.sort()
    monkey_business_list.reverse()
    print("Part 1: ", monkey_business_list[0] * monkey_business_list[1])
