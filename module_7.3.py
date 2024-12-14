import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
                words = content.translate(str.maketrans('', '', string.punctuation)).split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            capitalized_words = [w for w in words if w[0].isupper()]
            if len(capitalized_words):
                third_word = capitalized_words[2]
                position = capitalized_words.index(third_word) + 1
                result[file_name] = position
            else:
                result[file_name] = None
        return result

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            result[file_name] = sum(1 for w in words if w.lower() == word)
        return result

if __name__ == "__main__":
    finder = WordsFinder('test_file.txt')
    print(finder.get_all_words())
    print(finder.find('TEXT'))
    print(finder.count('teXT'))
