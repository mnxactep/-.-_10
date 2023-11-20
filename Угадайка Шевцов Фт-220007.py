import random
import logging
from datetime import datetime

# Настраиваем логгер
logging.basicConfig(filename='number_guessing.log', level=logging.INFO)

# Функция для регистрации информации
def log_info(message):
    logging.info(f'{datetime.now()}: {message}')

# Функция для игры в угадайку чисел
def number_guessing_game(N, k):
    log_info(f'Игра началась с N={N} and k={k}')
    target_number = random.randint(1, N)
    log_info(f'Загаданное число {target_number}')

    attempts = 0
    while attempts < k:
        try:
            guess = int(input(f'Угадайте число от 1 до {N}: '))
            log_info(f'Пользователь выбрал {guess}')
            if guess < target_number:
                print('Загаданное число больше')
                log_info('Загаданное число больше')
            elif guess > target_number:
                print('Загаданное число меньше')
                log_info('Загаданное число меньше')
            else:
                print('Вы угадали!')
                log_info('Пользователь угадал число')
                return
            attempts += 1
        except ValueError:
            print('Введите целое число')
            log_info('Введите целое число')

    print('Попытки закончились')
    log_info('Попытки закончились')

# Получение ввода от пользователя для N
while True:
    try:
        N = int(input("Введите верхнюю границу для загаданного числа: "))
        if N <= 0:
            print("Введите положительное натуральное число")
            continue
        break
    except ValueError:
        print("Введите целое число")

# Получение ввода от пользователя для k
while True:
    try:
        k = int(input("Введите количество попыток: "))
        if k <= 0:
            print("Введите положительное натуральное число")
            continue
        break
    except ValueError:
        print("Введите целое число")

# Calling the number guessing game function
number_guessing_game(N, k)


