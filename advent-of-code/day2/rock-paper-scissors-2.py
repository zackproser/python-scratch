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

DESIRED_OUTCOMES = {
    "X": {
        "NAME": "LOSE",
    },
    "Y": {
        "NAME": "DRAW",
    },
    "Z": {
        "NAME": "WIN",
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
        desired_outcome = DESIRED_OUTCOMES[plays[1].strip()]

        outcome = OUTCOMES[opponent_play]

        your_play = ""
        for key, value in outcome.items():
            if value["RESULT"] == desired_outcome["NAME"]:
                your_play = key

        game_score = OUTCOMES[opponent_play][your_play]["VALUE"]
        item_score = YOUR_PLAYS[your_play]["VALUE"]

        composite_score = game_score + item_score

        TOTAL_SCORE += composite_score

        print(
            f"opponent_play: {opponent_play}, desired_outcome: {desired_outcome} your_play: {your_play}")

print(TOTAL_SCORE)
