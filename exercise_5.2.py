string_1 = input(f'Введите строку 1: ')
string_2 = input(f'Введите строку 2: ')


def solution_1(str_1: str, str_2: str) -> int:
    """
    Банальное решение с перебором каждого символа в каждой строке и сравнение их.
    Однако при больших размеров строки и подстроки решение очень затратное по времени
    :param str_1: Строка
    :param str_2: Подстрока
    :return: Количество повторений подстроки в строке
    """
    result = 0
    i = 0
    while i < len(str_1):
        j = 0
        while j <= len(str_2):
            if j == len(str_2):
                result += 1
                break
            elif str_1[i + j] != str_2[j]:
                break
            else:
                j += 1
        i += 1
    return result


def solution_2(str_1: str, str_2: str) -> int:
    """
    Читал до этого про алгоритмы и там есть КМП-алгоритм, как раз для нахождения совпадений
    Но если длинна подстроки ровна единице то проще использовать первый метод
    :param str_1: Строка
    :param str_2: Подстрока
    :return: Количество повторений подстроки в строке
    """
    result = 0
    if len(str_2) == 1:
        result = solution_1(str_1, str_2)
    else:
        p = [0] * len(str_2)
        j = 0
        i = 1
        while i < len(str_2):
            if str_2[j] == str_2[i]:
                p[i] = j + 1
                i += 1
                j += 1
            else:
                if j == 0:
                    p[i] = 0
                    i += 1
                else:
                    j = p[j-1]
        n = len(str_1)
        m = len(str_2)
        i = 0
        j = 0
        while i < n:
            if str_1[i] == str_2[j]:
                i += 1
                j += 1
                if j == m:
                    result += 1
                    j = 0
            else:
                if j > 0:
                    j = p[j-1]
                else:
                    i += 1
    return result


print(solution_2(string_1, string_2))
