class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                value = file.read().lower()
                for sym in[',', '.', '=', '!', '?', ';', ':', ' - ']:
                    value = value.replace(sym, '')
                all_words[file_name] = value.split()
        return all_words

    def find(self,word):
        num_found = {}
        for file_name in self.file_names:
            all_words = self.get_all_words()
            for key, value in all_words.items():
                word = word.upper()
                # print(f'{key},  {word}, {value}')
                for i in value:
                    if word in i.upper():
                        num_found[key] = (value.index(word.lower()) + 1)
            return num_found
    def count(self, word):
        counted_value = {}
        for file_name in self.file_names:
            all_words = self.get_all_words()
            for key, value in all_words.items():
                word = word.upper()
                # print(f'{key},  {word}, {value}')
                for i in value:
                    if word in i.upper():
                        counted_value[key] = value.count(word.lower())
            return counted_value


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))