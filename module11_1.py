"""1"""
import requests
from numpy.ma.core import array


def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f'ошибка {response.status_code}')

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/posts'

fetch_data(url)

print('\n')

"""2"""
import numpy as np

array = np.array([1, 2, 3, 4, 5, 6])
print('исходный массив:', array)
array_squared = array ** 2
array_sum = np.sum(array)
array_mean = np.mean(array)

print('квадраты чисел:', array_squared)
print('сумма чисел:', array_sum)
print('среднее значение чисел:', array_mean)

