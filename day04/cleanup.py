from typing import List

def get_ranges_from_elf_pair(elf_pair: str) -> (List, List):
    elf1_assignment, elf2_assignment = elf_pair.split(",")
    return get_range_from_assignment(elf1_assignment), get_range_from_assignment(elf2_assignment)

def get_range_from_assignment(assignment: str) -> List:
    start, end = assignment.split("-")
    return list(range(int(start), int(end)+1))

def are_ranges_completely_overlapping(range_1: List, range_2: List):
    if range_1[0] <= range_2[0] and range_1[-1] >= range_2[-1]:
        return True
    elif range_2[0] <= range_1[0] and range_2[-1] >= range_1[-1]:
        return True
    else:
        return False

def are_ranges_partially_overlapping(range_1: List, range_2: List):
    if range_1[0] in range_2:
        return True
    elif range_1[-1] in range_2:
        return True
    elif range_2[0] in range_1:
        return True
    elif range_2[-1] in range_1:
        return True
    else:
        return False

if __name__ == "__main__":
    filename = "input.txt"
    # filename = "test.txt" # Part 1 answer should be 2, Part 2 answer should be 4
    total_part_1 = 0
    total_part_2 = 0
    with open(filename) as f:
        elf_pairs = f.readlines()
        for elf_pair in elf_pairs:
            range_elf_1, range_elf_2 = get_ranges_from_elf_pair(elf_pair.strip())
            total_part_1 += are_ranges_completely_overlapping(range_elf_1, range_elf_2)
            total_part_2 += are_ranges_partially_overlapping(range_elf_1, range_elf_2)
    print(total_part_1, total_part_2)
