import random

moves = {0: "rock", 1: "scissor", 2: "paper"}
random_move = random.randrange(0, 3)

opponent_move = moves[random_move]

def rps_game(my_move):
    print("0 = rock, 1 = scissor, 2 = paper")
    me = moves[my_move]

    # my_move = int(input("Enter your choice (number): "))
    if my_move < 0 or my_move > 2:
        print("Your choice is wrong!, Try agian.")
    else:

        print(f"Your move is ({me})")
        print(f"Your opponent move is ({opponent_move})\n")
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
