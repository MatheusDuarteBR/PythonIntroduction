import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Adivinhe um numero entre 1 e {x}: '))
        if guess < random_number:
            print('Desculpa, tente novamente. Muito baixo.')
        elif guess > random_number:
            print('Desculpa, tente novamente. Muito alto.')

    print(f'Yay, parabens. Voce adivinhou o numero {random_number} corretamente')

def computer_guess (x):
    low = 1
    high = x 
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'O {guess} muito alto (H), muito baixo (L), ou certo (C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! O computador acertou o numero, {guess}, certamente! ')
    
computer_guess(100)