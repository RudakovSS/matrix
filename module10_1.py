from time import time, sleep
import threading
def write_words(word_count, file_name):
    with open(file_name,'w') as file:
        for i in range(1, word_count + 1):
            file.write(f'какое то слово №{i}\n')
            sleep(0.1)
    print(f'завершилась запись в файл {file_name}')

start_time = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time()
print(f'время выполнения функций: {end_time - start_time:} секунд')

def thread_target(word_count, file_name):
    write_words(word_count, file_name)

start_thread_time = time()

threads = []
args = [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]

for arg in args:
    t = threading.Thread(target=thread_target, args=arg)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_thread_time = time()
print(f"Время выполнения потоков: {end_thread_time - start_thread_time:} секунд")