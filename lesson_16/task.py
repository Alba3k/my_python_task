class Example():
    def __init__(self, message):
        self.message = message

    def func_2_len(self):
        if (self.message.isdigit()) == True:
            message = int(self.message)
            if message == 0:
                return 1
            len_mes_n = 0
            while message:
                message //= 10
                len_mes_n  += 1
            print('Числовое значение. Длина: ', len_mes_n)
            return len_mes_n

        elif type(self.message.isdigit()) != True:
            len_mes = len(self.message)
            print('Строковое значение. Длина: ', len_mes)
            return len_mes

    def func_1(self):
        CONS = ['b','c','d','f','g','j','k','l','m',
        'n','p','q','s','t','v','x','z','h','r','w','y']
        VOWELS = ['e','u','i','o','a']
        counts_con = ''
        counts_vow = ''

        if isinstance(self.message, (int)) == True:
            message = self.message    
            even = 0
            for i in message:
                i = int(i)
                if i % 2 == 0:
                    even = even + i
                result = even * len_message
            print(f'Произведение суммы четных на длину строки: {result}')

        elif isinstance(self.message, (str)) == True:
            message = self.message.lower()
            for letter in self.message:
                if letter in CONS:
                    counts_con = counts_con + letter
                elif letter in VOWELS:
                    counts_vow = counts_vow + letter
            if (len(counts_con) * len(counts_vow)) <= (self.func_2_len()):
                print(counts_vow)
            else:
                print(counts_con)


if __name__ == '__main__':
    message = input('Введите строковое значение или число >>> ')
    demo_str = Example(message)
    demo_str.func_1()


