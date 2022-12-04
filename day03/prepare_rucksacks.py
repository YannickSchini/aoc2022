from typing import List

def get_duplicate_item_from_rucksacks(rucksack: str) -> str:
    number_of_items = len(rucksack)
    first_compartment = rucksack[:number_of_items//2]
    second_compartment = rucksack[number_of_items//2:]
    return set(first_compartment).intersection(second_compartment)

def get_badge_from_rucksacks(rucksack_1: str, rucksack_2: str, rucksack_3: str) -> str:
    return set(rucksack_1) & set(rucksack_2) & set(rucksack_3)

def get_value_from_item(item: str) -> int:
    if ord(item) >= ord("a"):
        return ord(item) - ord("a") + 1
    else:
        return ord(item) - ord("A") + 1 + 26

if __name__ == "__main__":
    # filename = "train.txt" # Part 1 result should be 157, part 2 result should be 70
    filename = "input.txt"
    total_part_1 = 0
    with open(filename) as f:
        rucksacks = f.readlines()
        for rucksack in rucksacks:
            duplicate_item = get_duplicate_item_from_rucksacks(rucksack.strip()).pop()
            total_part_1 += get_value_from_item(duplicate_item)

    print("Part 1:" ,total_part_1)

    total_part_2 = 0
    with open(filename) as f:
        lines = f.readlines()
        for i in range(len(lines)//3):
            total_part_2 += get_value_from_item(*get_badge_from_rucksacks(lines[3*i].strip(), lines[3*i+1].strip(), lines[3*i+2].strip()))

    print("Part 2:", total_part_2)
