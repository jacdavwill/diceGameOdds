import random

def large_straight(dice):
    for i in range(1, 7):
        if i not in dice:
            return False
    return True


def ones_or_fives(dice):
    return 1 in dice or 5 in dice


def triples(dice):
    for i in range(1, 7):
        if dice.count(i) >= 3:
            return True
    return False


def three_pair(dice):
    return [dice.count(i) for i in range(1, 7)].count(2) == 3


ways_to_score = [
    large_straight,
    ones_or_fives,
    triples,
    three_pair
]

attempts = 100000
score_counts = [0, 0, 0, 0, 0, 0]
for i in range(attempts):
    roll = [
        random.randint(1, 6),
        random.randint(1, 6),
        random.randint(1, 6),
        random.randint(1, 6),
        random.randint(1, 6),
        random.randint(1, 6)
    ]
    for j in range(6):
        for way_to_score in ways_to_score:
            if way_to_score(roll[:j+1]):
                score_counts[j] += 1
                break

print('Results\n')
for i in range(6):
    print(f'{i+1}: {score_counts[i]/attempts}')