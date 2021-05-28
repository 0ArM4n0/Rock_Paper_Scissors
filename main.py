import random

def Play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors ?")
    computer = random.choice(['r', 'p', 's'])

    if user == computer :
         return 'That Looks like a tie to me'


    if win(user, computer):
         return 'You Won'

    return 'You Lost'

def win (player , opponent):
    if (player == 's' and opponent == 'p') or (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r'):
        return True

print(Play())