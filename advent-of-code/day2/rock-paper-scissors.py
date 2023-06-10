OPPONENT_PLAYS = {
    "A": {
        "NAME": "ROCK",
        "VALUE": 1,
    },
    "B": {
        "NAME": "PAPER",
        "VALUE": 2,
    },
    "C": {
        "NAME": "SCISSORS",
        "VALUE": 3,
    }
}

YOUR_PLAYS = {
    "X": {
        "NAME": "ROCK",
        "VALUE": 1,
    },
    "Y": {
        "NAME": "PAPER",
        "VALUE": 2,
    },
    "Z": {
        "NAME": "SCISSORS",
        "VALUE": 3,
    }
}

OUTCOMES = {
    "A": {
        "X": {
            "RESULT": "DRAW",
            "VALUE": 3
        },
        "Y": {
            "RESULT": "WIN",
            "VALUE": 6,
        },
        "Z": {
            "RESULT": "LOSE",
            "VALUE": 0,
        }
    },
    "B": {
        "X": {
            "RESULT": "LOSE",
            "VALUE": 0,
        },
        "Y": {
            "RESULT": "DRAW",
            "VALUE": 3,
        },
        "Z": {
            "RESULT": "WIN",
            "VALUE": 6,
        }
    },
    "C": {

        "X": {
            "RESULT": "WIN",
            "VALUE": 6,
        },
        "Y": {

            "RESULT": "LOSE",
            "VALUE": 0,
        },
        "Z": {
            "RESULT": "DRAW",
            "VALUE": 3
        }
    }
}

TOTAL_SCORE = 0

with open("input.txt") as f:
    lines = f.readlines()

    for line in lines:
        plays = line.split(" ")

        opponent_play = plays[0].strip()
        your_play = plays[1].strip()

        result = OUTCOMES[opponent_play][your_play]
        game_score = OUTCOMES[opponent_play][your_play]["VALUE"]

        point_value_of_play = YOUR_PLAYS[your_play]["VALUE"]
        composite_score = game_score + point_value_of_play

        TOTAL_SCORE += composite_score

        print(
            f"opponent played: {OPPONENT_PLAYS[opponent_play]['NAME']}, you played: {YOUR_PLAYS[your_play]['NAME']}, result: {OUTCOMES[opponent_play][your_play]['RESULT']} {game_score}")

print(TOTAL_SCORE)
