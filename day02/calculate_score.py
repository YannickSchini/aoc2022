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

def convert_raw_to_results(raw: str) -> Result:
    if raw == "X":
        return Result.LOSS
    elif raw == "Y":
        return Result.DRAW
    elif raw == "Z":
        return Result.WIN
    else:
        Exception("UnknownResultException")

def get_result_for_player_2(player_1_move: Moves, player_2_move: Moves) -> Result:
    if player_1_move == player_2_move:
        return Result.DRAW
    elif (player_1_move == Moves.ROCK and player_2_move == Moves.SCISSORS) or (player_1_move == Moves.PAPER and player_2_move == Moves.ROCK) or (player_1_move == Moves.SCISSORS and player_2_move == Moves.PAPER):
        return Result.LOSS
    else:
        return Result.WIN

def get_move_for_player_2(player_1_move: Moves, target_result: Result) -> Result:
    if target_result == Result.DRAW:
        return player_1_move
    elif player_1_move == Moves.ROCK:
        if target_result == Result.WIN:
            return Moves.PAPER
        else:
            return Moves.SCISSORS
    elif player_1_move == Moves.PAPER:
        if target_result == Result.WIN:
            return Moves.SCISSORS
        else:
            return Moves.ROCK
    elif player_1_move == Moves.SCISSORS:
        if target_result == Result.WIN:
            return Moves.ROCK
        else:
            return Moves.PAPER
    else:
        Exception("WTF is happening?!")

def player_2_score_part_1(player_1_raw_move: str, player_2_raw_move: str) -> int:
    player_1_move = convert_raw_to_moves(player_1_raw_move)
    player_2_move = convert_raw_to_moves(player_2_raw_move)
    result = get_result_for_player_2(player_1_move, player_2_move)
    return player_2_move.value + result.value

def player_2_score_part_2(player_1_raw_move: str, expected_result_raw: str) -> int:
    player_1_move = convert_raw_to_moves(player_1_raw_move)
    expected_result = convert_raw_to_results(expected_result_raw)
    player_2_move = get_move_for_player_2(player_1_move, expected_result)
    return player_2_move.value + expected_result.value


if __name__ == "__main__":
    total_score = 0
    # file = "train.txt" # Score should be 15 for part 1, 12 for part 2
    file = "input.txt"
    with open(file) as f:
        for line in f.readlines():
            # total_score += player_2_score_part_1(*line.strip().split(" "))
            total_score += player_2_score_part_2(*line.strip().split(" "))
    print(total_score)
