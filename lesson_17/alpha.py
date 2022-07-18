import string

# Создание класса Алфавит
class Alphabet:

    def __init__(self, language, letters_str):
        self.lang = language
        self.letters = list(letters_str)

    def print(self):
        print(self.letters)

    def letters_num(self):
        len(self.letters)



# Создание класса Английский алфавит на базе класса Алфавит
class EngAlphabet(Alphabet):

    __letters_num = 26
    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

# Проверка отношения буквы к английскому алфавиту
    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            print(f'Буква {letter}, существует в английском алфавите')
            return True

        print(f'Буква {letter}, отсутствует в английском алфавите')
        return False

# Количество букв в английском алфавите
    def letters_num(self):
        return EngAlphabet.__letters_num

# Пример текста на английском
    @staticmethod
    def example():
        print('Taking care of business, one python script at a time.')



if __name__ == '__main__':

# Создали экземпляр класса
    eng_alphabet = EngAlphabet()
# Напечатали весь алфавит
    eng_alphabet.print()
# Напечатали количество букв алфавита
    print(eng_alphabet.letters_num())
# Проверка является ли символ Y, буквой английского алфавита
    print(eng_alphabet.is_en_letter('Y'))
# Проверка является ли символ У, буквой английского алфавита
    print(eng_alphabet.is_en_letter('У'))
# Пример текста на английском языке
    EngAlphabet.example()