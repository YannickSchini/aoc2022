from enum import Enum

class Moves(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Result(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6

def convert_raw_to_moves(raw: str) -> Moves:
    if raw in ["A", "X"]:
        return Moves.ROCK
    elif raw in ["B", "Y"]:
        return Moves.PAPER
    elif raw in ["C", "Z"]:
        return Moves.SCISSORS
    else:
        Exception("UnknownMoveException")

def get_result(player_1_move: Moves, player_2_move: Moves) -> Result:
    if player_1_move == player_2_move:
        return Result.DRAW
    elif (player_1_move == Moves.ROCK and player_2_move == Moves.SCISSORS) or (player_1_move == Moves.PAPER and player_2_move == Moves.ROCK) or (player_1_move == Moves.SCISSORS and player_2_move == Moves.PAPER):
        return Result.WIN
    else:
        return Result.LOSS

def player_1_score(player_1_raw_move: str, player_2_raw_move: str) -> int:
    player_1_move = convert_raw_to_moves(player_1_raw_move)
    player_2_move = convert_raw_to_moves(player_2_raw_move)
    result = get_result(player_1_move, player_2_move)
    return player_1_move.value + result.value


if __name__ == "__main__":
    total_score = 0
    file = "train.txt" # Score should be 15
    # file = "input.txt"
    with open(file) as f:
        for line in f.readlines():
            total_score += player_1_score(*line.strip().split(" "))
    print(total_score)
