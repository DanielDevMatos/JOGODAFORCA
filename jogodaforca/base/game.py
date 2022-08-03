import random

from jogodaforca.base.words import word_type

options = random.choice(['animal', 'object', 'city', 'leisure'])

print(options)

word = word_type(options).upper()

print('JOGO DA FORCA')
print('Adivinhe a palavra: ', end='')

for letter in word:
    if letter == '-':
        print(letter, end='')
    print('_ ', end='')

hidden_word = set(word)
guess_word = set()
try_guess = 7


while not(hidden_word.issubset(guess_word)) and try_guess > 0:
    print('')
    print('')

    guess = input('Digite uma letra: ').upper()
    guess_word.add(guess)
    print(guess_word)
    if guess in hidden_word:
        for letter in word:
            if letter == '-':    # condição para poder utilizar palavras com hifen
                print(letter, end='')
                guess_word.add(letter)
            elif letter in guess_word:
                print(f'{letter} ', end='')
            else:
                print('_ ', end='')
    else:
        print('Não existe essa letra na palavra, tente de novo ')
        try_guess -= 1

print('')
if try_guess == 0:
    print('Você perdeu!')
    print(word)
else:
    print(f'Parabens você acertou a palavra secreta: {word}')

