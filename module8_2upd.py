
def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    for i in numbers:
        try:
            result += i

        except TypeError:
            incorrect_data +=1
            print(f"Некорректный элемент: {i}")
    return result , incorrect_data


numbers_list = [2,5,76, 'erd']
print(personal_sum(numbers_list))

def calculate_average(numbers):
    try:
        total, incorrect_data = personal_sum(numbers)
        count = len(numbers) - incorrect_data
        if count == 0:
            return 0

        average = total / count
        return average
    except ZeroDivisionError:
        return 0

    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

print(calculate_average([2,6,8]))
print()
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')





