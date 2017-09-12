# Create Rock, Paper, Scissors game
import random


def request_input(name):
    print('\n{}....'.format(name))
    action = input('Rock, Paper, or Scissors???').upper()
    return action


def main():
    valid_inputs = ['ROCK','PAPER','SCISSORS']
    name = input('What is your name???')
    while True:
        act_1 = request_input(name)
        act_2 = random.choice(valid_inputs)
        print('MCP chose {}!!!'.format(act_2))
        if not {act_1,act_2}.issubset(valid_inputs):
            print('\nRequiring proper inputs...')
        elif act_1 == act_2:
            print('\nRESULT IS A TIE!!!  Replaying...')
        elif act_1 == 'ROCK':
            if act_2 == 'PAPER':
                winner = 'MCP'
                break
            elif act_2 == 'SCISSORS':
                winner = name
                break
        elif act_1 == 'PAPER':
            if act_2 == 'SCISSORS':
                winner = 'MCP'
                break
            elif act_2 == 'ROCK':
                winner = name
                break
        elif act_1 == 'SCISSORS':
            if act_2 == 'ROCK':
                winner = 'MCP'
                break
            elif act_2 == 'PAPER':
                winner = name
                break
    print('\n{} is the winner!!!'.format(winner))


if __name__ == '__main__':
    main()