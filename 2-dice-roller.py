# Challenge #364 [Easy] Create a Dice Roller
import random


def dice_roller(input_code):
    """
    Creating a dice roller for DnD game.
    Parameter input is defined as: "NdM".
    Where: N - number of dices ([1, 100]),
           M - number of sides ([2, 100]),
           d - just a separator between two numbers
    Return is an integer which is a sum of results of all dices.
    :param input: str
    :return: int
    """
    N, M = [int(number) for number in input_code.split('d')]
    if N < 1 or N > 100:
        print("You have entered invalid value for parameter N. Your"
              " value needs to be inside of the range [1, 100]")
    if M < 2 or M > 100:
        print("You have entered invalid value for parameter M. Your"
              " value needs to be inside of the range [2, 100]")

    results_of_rolling = []
    for i in range(N):
        results_of_rolling.append(random.randint(1, M))

    return sum(results_of_rolling)


print(dice_roller("5d12"))
print(dice_roller("6d4"))
print(dice_roller("1d2"))
print(dice_roller("1d8"))
print(dice_roller("3d6"))
print(dice_roller("4d20"))
print(dice_roller("100d100"))