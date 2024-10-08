from random import randint

number = randint(1, 100)
print('Угадайте число от 1 до 100')


def main():
    while True:
        i = int(input('Введите Ваше число \n'))

        if i < number:
            print('Ваше число меньше загаданного')
        
        elif i > number:
            print('Ваше число больше загаданного')

        elif i == number:
            break

main()

print('Вы угадали!')
