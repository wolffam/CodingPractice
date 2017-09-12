# Create Rock, Paper, Scissors game


def request_input(player_num):
    print('Player {}....'.format(player_num))
    action = input('Rock, Paper, or Scissors???').upper()
    return action


def main():
    valid_inputs = ['ROCK','PAPER','SCISSORS']
    decided = False
    winner = None
    while not decided:
        act_1 = request_input(1)
        act_2 = request_input(2)
        if not {act_1,act_2}.issubset(valid_inputs):
            print('\nRequiring proper inputs...')
        elif act_1 == act_2:
            print('\nRESULT IS A TIE!!!  Replaying...')
        elif act_1 == 'ROCK':
            if act_2 == 'PAPER':
                winner = 2
                break
            elif act_2 == 'SCISSORS':
                winner = 1
                break
        elif act_1 == 'PAPER':
            if act_2 == 'SCISSORS':
                winner = 2
                break
            elif act_2 == 'ROCK':
                winner = 1
                break
        elif act_1 == 'SCISSORS':
            if act_2 == 'ROCK':
                winner = 2
                break
            elif act_2 == 'PAPER':
                winner = 1
                break
    print('\nPlayer {} is the winner!!!'.format(winner))


if __name__ == '__main__':
    main()