import math

def main():
	print('''КАЛЬКУЛЯТОР ПЕРЕВОДА ГРАДУСОВ В РАДИАНЫ
Для перевода градусов в радианы нажмите R
Для перевода радиан в градусы нажмите G''')

	directions = input('\nНажмите соответствующую кнопку: ').lower()
	if directions == 'r':
		gradus = float(input('Количество градусов: '))
		print(f'{gradus} градусов равно: {math.radians(gradus)} радиан.')
	elif directions == 'g':
		rad = float(input('Количество радиан: '))
		print(f'{rad} радиан равно: {math.degrees(rad)} градусов.')
	else:
		print('Вы ввели неверную команду.')

if __name__ == '__main__':
	main()