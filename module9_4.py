import random
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x: x[0] == x[1], zip(first, second)))
print(result)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')
    return write_everything
writing = get_advanced_writer('txt')
writing('jdddjjdjd', 232, {'yes': 'no'})

class MysticBall:
    def __init__(self):
        self.words = {"Да", "Нет", "Возможно", "Определенно да", "Определенно нет"}
    def __call__(self):
        return random.choice(list(self.words))


ball = MysticBall()
print(ball())



