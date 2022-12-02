from enum import Enum

class Scores(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    LOSS = 0
    DRAW = 3
    WIN = 6

Moves = Enum("Moves", ["ROCK", "PAPER", "SCISSORS"])

Result = Enum("Result", ["WIN", "DRAW", "LOSS"])

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
    if player_1_move is player_2_move:
        return Result.DRAW
    elif (player_1_move is Moves.ROCK and player_2_move is Moves.SCISSORS) or (player_1_move is Moves.PAPER and player_2_move is Moves.ROCK) or (player_1_move is Moves.SCISSORS and player_2_move is Moves.PAPER):
        return Result.WIN
    else:
        return Result.LOSS

def player_1_score(player_1_raw_move: str, player_2_raw_move: str) -> int:
    player_1_move = convert_raw_to_moves(player_1_raw_move)
    player_2_move = convert_raw_to_moves(player_2_raw_move)
    result = get_result(player_1_move, player_2_move)
    print(result)
    return Scores[player_1_move.name].value + Scores[result.name].value


if __name__ == "__main__":
    total_score = 0
    file = "train.txt" # Score should be 15
    file = "input.txt"
    with open(file) as f:
        for line in f.readlines():
            total_score += player_1_score(*line.strip().split(" "))
    print(total_score)
