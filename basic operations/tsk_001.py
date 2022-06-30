import random

def main():
	number_rnd = random.randint(100, 999)
	number_lst = list(str(number_rnd))
	number_summ = 0

	for i in number_lst:
		number_summ = number_summ + int(i)
	print(f'Сумма всех цифр числа {number_rnd}, равна: {number_summ}')

	# return number_rnd, number_summ

if __name__ == '__main__':
	main()