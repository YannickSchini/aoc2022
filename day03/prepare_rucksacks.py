def get_duplicate_item_from_rucksacks(rucksack: str) -> str:
    number_of_items = len(rucksack)
    first_compartment = rucksack[:number_of_items//2]
    second_compartment = rucksack[number_of_items//2:]
    return set(first_compartment).intersection(second_compartment)

def get_value_from_item(item: str) -> int:
    if ord(item) >= ord("a"):
        return ord(item) - ord("a") + 1
    else:
        return ord(item) - ord("A") + 1 + 26

if __name__ == "__main__":
    # filename = "train.txt" # Part 1 result should be 157
    filename = "input.txt"
    total = 0
    with open(filename) as f:
        rucksacks = f.readlines()
        for rucksack in rucksacks:
            duplicate_item = get_duplicate_item_from_rucksacks(rucksack.strip()).pop()
            total += get_value_from_item(duplicate_item)

    print(total)

