def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    for item in strings:
        file.write(item + '\n')
    file.close()

    strings_positions = {}
    file = open(file_name, 'rb')
    line_number = 0
    for line in file:
        position = file.tell() - len(line)
        decoded_line = line.decode('utf-8').strip()
        strings_positions[(line_number + 1, position)] = decoded_line
        line_number += 1
    file.close()

    return strings_positions



result = custom_write('text.txt', ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!'])

print(result)