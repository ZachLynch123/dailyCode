import random


def get_roll(num_of_dice, num_of_sides):
    solution = 0
    breakdown = []
    for i in range(0, int(num_of_dice)):
        x = random.randint(0, int(num_of_sides))
        breakdown.append(x)
        solution += x
    print(solution)
    print(breakdown)

print("Enter dice to roll")
dice = input().split('d')

get_roll(dice[0], dice[1])