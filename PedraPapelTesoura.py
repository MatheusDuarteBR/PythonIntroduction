import random

def play():
    user = input("Qual a sua escolha? 'r' para pedra, 'p' para papel, 't' para tesoura\n ")
    computer = random.choice (['r', 'p', 't'])

    if user == computer:
        return 'Um empate '

    if is_win(user, computer):
        return 'Voce ganhou! '

    return 'Voce perdeu! '

def is_win (player, opponent):
    if (player == 'r' and opponent == 'p') or (player == 't' and opponent == 'p') \
        or (player == 'p' and opponent == 'p'):
        return True

print(play())