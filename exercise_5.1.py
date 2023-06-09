while True:
    number = int(input(f'Введите число: '))
    if number < 0:
        print(f'Число должно быть больше или равно 0')
        continue
    elif number == 0:
        print(f'Факториал числа {number} равен 1')
    else:
        result = 1
        for i in range(1, number+1):
            result *= i
        print(f'Факториал числа {number} равен {result}')
    break
