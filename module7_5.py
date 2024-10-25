import os


print("Текущая директория:", os.getcwd())
if os.path.exists('second'):
    os.chdir('second')
else:
    os.mkdir('second')
    os.chdir('second')

print('Текущая директория:', os.getcwd())

os.chdir(r'C:\Users\Stepan\PycharmProjects\pythonMainProject')
print('Текущая директория:', os.getcwd())

files = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]

for file in files:
    filepath = os.path.join(os.getcwd(), file)
    filetime = os.path.getmtime(filepath)
    filesize = os.path.getsize(filepath)
    parent_dir = os.path.dirname(filepath)

    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {filetime}, Родительская директория: {parent_dir}')