def str_parsing(string_data):

	# (1) вывод третьего символа строки
	print(string_data[2])

	# (2) предпоследний символ строки, т.к. последний -1, предпоследний -2
	print(string_data[-2])

	# (3) первые пять символов строки
	print(string_data[0:5])

	# (4) вся строка кроме последних двух символов. Для этого с len узнаем длину
	# строки и (-2) символа и выводим новую строку с учетом этой инфы
	new_str_2 = len(string_data) - 2
	print(string_data[0:new_str_2])

	# (5) все символы с четными индексами
	print(string_data[::2])

	# (6) все символы с нечетными индексами, начиная с 2 символа
	print(string_data[1::2])

	# (7) все символы в обратном порядке
	print(string_data[-1::-1])

	# (8) все символы через один в обратном порядке с последнего
	print(string_data[-1::-2])

	# (9) длина строки
	print(len(string_data))

if __name__ == '__main__':

	string_data = input('Введите строку: ')
	str_parsing(string_data)