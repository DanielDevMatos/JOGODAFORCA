import random


def word_type(choice):
    if choice == 'animal':
        animals = [
            'abelha', 'abutre', 'acaro', 'bem-te-vi', 'barracuda', 'barbo', 'caranguejo',
            'cavalo-marinho', 'diabo-da-tasmania', 'doninha', 'ema'
        ]
        return random.choice(animals)
    elif choice == 'object':
        objects = [
            'banco', 'bandeira', 'boneca', 'camisa', 'chicote', 'Dado', 'dinamite', 'espremedor', 'quebra-cabeça',
            'tesoura', 'Walkie-talkie', 'Xadrez', 'guarda-chuva'
        ]
        return random.choice(objects)
    elif choice == 'city':
        cities = [
            'New-York', 'Sao-Paulo', 'Boston', 'Tokyo', 'Londres', 'porto-rico', 'Moscou',
            'Salvador', 'Buenos-aries', 'Pequin'
        ]
        return random.choice(cities)
    else:
        leisure = [
            'Dormi', 'Correr', 'Jogar', 'Cantar', 'nadar', 'Futebol', 'Volei', 'Basquete',
            'Passear', 'Beijar', 'cavalgar', 'Maratonar'
        ]
        return random.choice(leisure)

