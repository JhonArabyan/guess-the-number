import random
random_number = random.randint(1,20)
print('Угадай число от 1 до 20')
for i in range(1, 6):
    print('Попытка', i)
    play_number = int(input())
    if i < 6:
        if play_number == random_number:
            print('Молодец, ты угадал!')
            break
        elif play_number > random_number:
            print('Загаданное число меньше.')
        elif play_number < random_number:
            print('Загаданное число больше.')
    else:
        print('Попытки закончились. Было загадано число:', random_number)
