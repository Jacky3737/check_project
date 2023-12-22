import numpy as np

def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое число в середине заданного интервала, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        
    Returns:
        int: Число попыток
    """
    count = 0
    
    #задаем первоначальное положение для значения функции
    min=1
    max=100
    predict=(min + max - 1)//2
    
    #ищем соответствие уменьшая интервал 
    while number!=predict:
        count += 1
        
        if number > predict:
            min = predict + 1
            predict = (min + max)//2
        elif number < predict:
            max = predict - 1 
            predict = (min + max)//2

    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    
    Args:
        random_predict ([type]): функция угадывания
        
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
#Run benchmarking to score effectiveness of all algorithms

print('Run benchmarking for game_core_v2: ', end='')
score_game(game_core_v2)