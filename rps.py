import random


def rps(my_move):
    moves = {0: "rock", 1: "scissor", 2: "paper"}

    random_move = random.randrange(0, 3)

    print("0 = rock, 1 = scissor, 2 = paper")

    # my_move = int(input("Enter your choice (number): "))
    if my_move < 0 or my_move > 2:
        print("Your choice is wrong!, Try agian.")
    else:
        print(f"Your move is ({moves[my_move]})")
        print(f"Your opponent move is ({moves[random_move]})\n")
        if my_move == 0:  # rock
            if random_move == 0:  # rock
                res = "Draw"
            elif random_move == 1:  # scissor
                res = "You Win!!"
            else:  # paper
                res = "You lose."
        if my_move == 1:  # scissor
            if random_move == 0:  # rock
                res = "You Win!!"
            elif random_move == 1:  # scissor
                res = "Draw"
            else:  # paper
                print("You lose.")
        if my_move == 2:  # paper
            if random_move == 0:  # rock
                res = "You Win!!"
            elif random_move == 1:  # scissor
                res = "You lose."
            else:  # paper
                res = "Draw"
    return res
