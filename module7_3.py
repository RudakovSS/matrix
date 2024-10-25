
class WordsFinder():
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = ",.!?;:-"
        for file_name in self.file_names:
            words = []
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for char in punctuation:
                        line = line.replace(char, '')
                    line = line.replace(' -', '').replace('- ', '')
                    words += line.split()
            all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name in all_words:
            words = all_words[file_name]
            if word in words:
                result[file_name] = words.index(word)
            else:
                result[file_name] = 0
        return result

    def count(self,word):
        result = {}
        all_words = self.get_all_words()
        for file_name in all_words:
            words = all_words[file_name]
            result[file_name] = words.count(word)
        return result




finder = WordsFinder('test_file.txt',)
print(finder.get_all_words()) # Все слова
print(finder.find('в')) # 3 слово по счёту
print(finder.count('text'))