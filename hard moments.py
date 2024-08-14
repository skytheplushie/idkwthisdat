def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result = result + i
        except TypeError:
            incorrect_data = incorrect_data + 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return result, incorrect_data

def calculate_average(numbers):
    try:
        sum_num = personal_sum(numbers)
        num = []
        try:
            for i in numbers:
                if type(i) == int:
                    num.append(i)
            return sum_num[0] / len(num)
        except ZeroDivisionError:
            return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать