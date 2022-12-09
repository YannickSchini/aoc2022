from argparse import ArgumentParser, FileType
from dataclasses import dataclass
from enum import Enum
from typing import List

class Direction(Enum):
    N = (1, 0)
    S = (-1, 0)
    E = (0, 1)
    W = (0, -1)

@dataclass(eq=True)
class Position:
    x: int
    y: int


def convert_raw_dir_to_dir(raw_dir: str) -> Direction:
    if raw_dir == "U":
        return Direction.N
    elif raw_dir == "R":
        return Direction.E
    elif raw_dir == "D":
        return Direction.S
    elif raw_dir == "L":
        return Direction.W
    else:
        raise Exception(f"Unknown direction: {raw_dir}")

def move_head(head_position: Position, direction: Direction) -> Position:
    return Position(head_position.x + direction.value[0], head_position.y + direction.value[1])

def should_tail_move(head_position: Position, tail_position: Position) -> bool:
    if head_position == tail_position:
        return False
    elif abs(head_position.x - tail_position.x) <= 1 and abs(head_position.y - tail_position.y) <= 1:
        return False
    else:
        return True

def get_sign(a: int) -> int:
    return (a>0) - (a<0)

def move_tail(head_position: Position, tail_position: Position) -> Position:
    return Position(tail_position.x + get_sign(head_position.x - tail_position.x), tail_position.y + get_sign(head_position.y - tail_position.y))

def unique(list_of_pos: List[Position]):
    result = []
    for pos in list_of_pos:
        if pos not in result:
            result.append(pos)
    return result

if __name__ == "__main__":
    parser = ArgumentParser(prog = "rope_movement", description = "This program calculates the rope movements")
    parser.add_argument("filename", type=FileType("r"))
    args = parser.parse_args()

    head_position = Position(0, 0)
    tail_position = Position(0, 0)
    history_of_tail_positions = [tail_position]
    with args.filename as f:
        moves = list(map(str.strip, f.readlines()))

    for move in moves:
        raw_direction, raw_amplitude = move.split(" ")
        amplitude = int(raw_amplitude)
        direction = convert_raw_dir_to_dir(raw_direction)
        for i in range(amplitude):
            head_position = move_head(head_position, direction)
            if should_tail_move(head_position, tail_position):
                tail_position = move_tail(head_position, tail_position)
                history_of_tail_positions.append(tail_position)

    print("Part 1: ", len(unique(history_of_tail_positions)))

    full_rope = [Position(0, 0), Position(0, 0), Position(0, 0), Position(0, 0), Position(0, 0), Position(0, 0), Position(0, 0), Position(0, 0), Position(0, 0), Position(0, 0)]
    history_of_tail_positions = [full_rope[-1]]
    for move in moves:
        raw_direction, raw_amplitude = move.split(" ")
        amplitude = int(raw_amplitude)
        direction = convert_raw_dir_to_dir(raw_direction)
        for i in range(amplitude):
            full_rope[0] = move_head(full_rope[0], direction)
            for index in range(1, len(full_rope)):
                if should_tail_move(full_rope[index-1], full_rope[index]):
                    full_rope[index] = move_tail(full_rope[index-1], full_rope[index])
            history_of_tail_positions.append(full_rope[-1])

    print("Part 2: ", len(unique(history_of_tail_positions)))
