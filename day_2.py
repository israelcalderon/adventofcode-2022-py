from collections import namedtuple
from enum import Enum
from typing import List


class Shape(Enum):
    ROCK = 'ROCK'
    PAPER = 'PAPER'
    SCISSORS = 'SCISSORS'


class MatchResult:
    WIN = 'WIN'
    DRAW = 'DRAW'
    LOOSE = 'LOOSE'


class MatchScore(Enum):
    WIN = 6
    DRAW = 3
    LOOSE = 0


class ShapeScore(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


SHAPES = {
    'A': Shape.ROCK.value,
    'X': Shape.ROCK.value,
    'B': Shape.PAPER.value,
    'Y': Shape.PAPER.value,
    'C': Shape.SCISSORS.value,
    'Z': Shape.SCISSORS.value,
}

RESULTS = {
    'X': MatchResult.LOOSE,
    'Y': MatchResult.DRAW,
    'Z': MatchResult.WIN,
}


COUNTER = {
    Shape.ROCK.value: Shape.PAPER.value,
    Shape.PAPER.value: Shape.SCISSORS.value,
    Shape.SCISSORS.value: Shape.ROCK.value,
}


REVERSE_COUNTER = {v: k for k, v in COUNTER.items()}


CounterStrategy = namedtuple('CounterStrategy', ['rival_move', 'your_move'])
ResultStrategy = namedtuple('ResultStrategy', ['rival_move', 'match_result'])


def get_strategies(
    strategy: CounterStrategy | ResultStrategy
) -> List[CounterStrategy]:
    with open('day_2_input') as file:
        return [strategy(*line.split()) for line in file]


def get_score_by_shape(shape_code: str) -> int:
    return ShapeScore[shape_code].value


def get_score_by_match_result(match_result: str) -> int:
    return MatchScore[match_result].value


def get_match_result(your_move: str, rival_move: str) -> str:
    if your_move == rival_move:
        return MatchResult.DRAW

    if your_move == COUNTER[rival_move]:
        return MatchResult.WIN

    return MatchResult.LOOSE


def get_shape_to_play(rival_move: str, result_expected: str) -> str:
    if result_expected == MatchResult.DRAW:
        return rival_move

    if result_expected == MatchResult.LOOSE:
        return REVERSE_COUNTER[rival_move]

    return COUNTER[rival_move]


def compute_counter_strategy(strategies: List[CounterStrategy]) -> List[int]:
    scores = []
    for strategy in strategies:
        your_move, rival_move = (
            SHAPES[strategy.your_move], SHAPES[strategy.rival_move]
        )

        match_result = get_match_result(your_move, rival_move)
        score = get_score_by_match_result(match_result)
        score += get_score_by_shape(your_move)
        scores.append(score)
    return scores


def compute_result_strategy(strategies: List[ResultStrategy]) -> List[int]:
    scores = []
    for strategy in strategies:
        rival_move, result = (
            SHAPES[strategy.rival_move], RESULTS[strategy.match_result]
        )
        shape_to_play = get_shape_to_play(rival_move, result)

        score = get_score_by_match_result(result)
        score += get_score_by_shape(shape_to_play)
        scores.append(score)
    return scores


def main():
    counter_strategies = get_strategies(CounterStrategy)
    scores_using_counter = compute_counter_strategy(counter_strategies)

    result_strategies = get_strategies(ResultStrategy)
    scores_using_result = compute_result_strategy(result_strategies)

    print(f'Score using counter strategy: {sum(scores_using_counter)}')
    print(f'Score using result strategy: {sum(scores_using_result)}')


if __name__ == '__main__':
    main()
