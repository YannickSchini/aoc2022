from argparse import ArgumentParser, FileType
from typing import List

def check_if_visible_from_direction(tree_height: str, trees_from_direction: str):
    return tree_height > max(trees_from_direction)

def is_visible(x: int, y: int, grid: List[str]):
    len_x = len(grid)
    len_y = len(grid[0])
    if x == 0 or y == 0 or x == len_x - 1 or y == len_y - 1:
        return True
    elif check_if_visible_from_direction(grid[x][y], grid[x][:y]):
        return True
    elif check_if_visible_from_direction(grid[x][y], grid[x][y+1:]):
        return True
    elif check_if_visible_from_direction(grid[x][y], "".join([grid[i][y] for i in range(x)])):
        return True
    elif check_if_visible_from_direction(grid[x][y], "".join([grid[i][y] for i in range(x+1, len_x)])):
        return True
    else:
        return False

def get_viewing_distance(tree_height: str, trees_from_direction: str) -> int:
    for i in range(len(trees_from_direction)):
        if trees_from_direction[i] < tree_height:
            pass
        else:
            return i + 1
    return len(trees_from_direction)

def calculate_scenic_score(x: int, y: int, grid: List[str]) -> int:
    len_x = len(grid)
    len_y = len(grid[0])
    first_direction = get_viewing_distance(grid[x][y], grid[x][:y][::-1])
    second_direction = get_viewing_distance(grid[x][y], grid[x][y+1:])
    third_direction = get_viewing_distance(grid[x][y], "".join([grid[i][y] for i in range(x)])[::-1])
    fourth_direction = get_viewing_distance(grid[x][y], "".join([grid[i][y] for i in range(x+1, len_x)]))
    return first_direction * second_direction * third_direction * fourth_direction

if __name__ == "__main__":
    parser = ArgumentParser(prog = 'fix_radio', description = 'This program fixes the radio by finding the end of the required token')
    parser.add_argument("filename", type=FileType("r"))
    args = parser.parse_args()

    with args.filename as f:
        grid = list(map(str.strip, f.readlines()))
    sum = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            sum += is_visible(x, y, grid)
    print("Part 1: ", sum)

    max_scenic_score = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            current_score = calculate_scenic_score(x, y, grid)
            if current_score > max_scenic_score:
                max_scenic_score = current_score
    print("Part 2: ", max_scenic_score)
