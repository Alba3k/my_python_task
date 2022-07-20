import re
import os

file_dict = {}

def my_decorator(func):
    def wrapper():
        name_file = file_name
        size_file = os.path.getsize(file_name)
        url = os.path.abspath(file_name)
        extension = url.split('.')[-1]
        file_dict[name_file] = (size_file, url, extension)
        lens = len(file_dict)
        print(f'Словарь содержит информацию о {lens} файлах')
        func()
    return wrapper

@my_decorator
def file_read():
	sample_text = ' '.join(lines)	
	pattern_1 = '\d{3}'
	pattern_2 = '\w*@\w*.\w*'
	res_num = re.findall(pattern_1, sample_text)
	res_email = re.findall(pattern_2, sample_text)
	print(res_num)
	print(f'{res_email}\n')
	return res_num, res_email

while True:
	try:
		file_name = input('Введите имя файла: ')
		with open(file_name) as file_object:
			lines = file_object.readlines()
			file_read()
	except FileNotFoundError:
		print('Такой файл не найден, укажите правильное имя')
		continue

file_read()
