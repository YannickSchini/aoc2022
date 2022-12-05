from typing import List, Tuple


def get_number_of_stacks(raw_stacks: str) -> int:
    last_line = raw_stacks.split("\n")[-1]
    last_char = last_line.strip()[-1]
    return int(last_char)


def process_raw_stacks(raw_stacks: str) -> List[List[str]]:
    num_of_stacks = get_number_of_stacks(raw_stacks)
    stacks = [[] for i in range(num_of_stacks)]
    raw_stacks = raw_stacks.split("\n")[:-1] # remove last line
    for line in raw_stacks[::-1]:
        for i in range(num_of_stacks):
            if line[1+i*4] != " ":
                stacks[i].append(line[1+i*4])
    return stacks

def process_raw_moves(raw_moves: str) -> List[Tuple]:
    tuples = []
    for line in raw_moves.split("\n")[:-1]:
        line_content_as_list = line.split(" ")
        tuples.append((int(line_content_as_list[1]), int(line_content_as_list[3]), int(line_content_as_list[5])))
    return tuples

def execute_move_on_stacks_part_1(move: Tuple, stacks: List[List[str]]) -> List[List[str]]:
    for i in range(move[0]):
        crate_to_move = stacks[move[1]-1].pop()
        stacks[move[2]-1].append(crate_to_move)
    return stacks

def execute_move_on_stacks_part_2(move: Tuple, stacks: List[List[str]]) -> List[List[str]]:
    crates_to_move = stacks[move[1]-1][len(stacks[move[1]-1])-move[0]:]
    stacks[move[2]-1] += crates_to_move
    del stacks[move[1]-1][len(stacks[move[1]-1])-move[0]:]
    return stacks


if __name__ == "__main__":
    filename = "input.txt"
    # filename = "test.txt" # Result for part1 should be "CMZ", result for part 2 should be "MCD"
    with open(filename) as f:
        content = f.read()
    stacks, moves = content.split("\n\n")
    stacks = process_raw_stacks(stacks)
    moves = process_raw_moves(moves)
    for move in moves:
        # stacks_part_1 = execute_move_on_stacks_part_1(move, stacks)
        stacks_part_2 = execute_move_on_stacks_part_2(move, stacks)
    message = ""
    for stack in stacks_part_2:
        message += stack[-1]
    print(message)
