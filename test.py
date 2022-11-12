from rps_file import rps_game
import rps_file

# values = 0
# # print(rps_game(0))


# def call():
#     return rps_game(int(1))

# call()

text = '0 = rock, 1 = scissor, 2 = paper\n'
text += f'Your opponent move is {rps_file.opponent_move}\n'
text += rps_game(1)
print(text)