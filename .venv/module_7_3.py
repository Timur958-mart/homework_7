import re


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                    list_words = [re.sub(r'[^\w\s]', '', line).lower() for line in file.read().split()]
                    all_words[file_name] = list_words
        return all_words

    def find(self, word):
        fined_word = {}
        for file_name, words in self.get_all_words().items():
            if word.lower() in words:
                fined_word[file_name] = words.index(word.lower()) + 1
            else:
                print('Совпадений не найдено')
        return fined_word

    def count(self, word):
        count_word = {}
        for file_name, words in self.get_all_words().items():
            count_word[file_name] = words.count(word.lower())
        return count_word

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))
