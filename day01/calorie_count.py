from typing import Dict

def process_input(file_name: str) -> Dict[int, int]:
    calories_per_elf = {}
    number_of_elf = 0
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            if line == "\n":
                number_of_elf += 1
            elif number_of_elf in calories_per_elf.keys():
                calories_per_elf[number_of_elf] += int(line.strip())
            else:
                calories_per_elf[number_of_elf] = int(line.strip())
    return calories_per_elf

def get_top_3(calories_per_elf: Dict[int, int]) -> int:
    top_3_calories = 0
    for i in range(3):
        top_elf = max(calories_per_elf, key=calories_per_elf.get)
        top_3_calories += calories_per_elf.pop(top_elf)
    return top_3_calories

if __name__ == "__main__":
    # calories_per_elf = process_input("train.txt")
    calories_per_elf = process_input("input.txt")
    print("Max calories for one elf (first puzzle): ", max(calories_per_elf.values()))
    print("Top 3 calories (second puzzle): ", get_top_3(calories_per_elf))
