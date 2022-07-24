# создаем справочник карточных мастей
SUITS = ['Пики', 'Бубны', 'Черви', 'Крести']

# создаем справочник номиналов карт
RANKS_N = list(range(2,11))
RANKS_A = ['Валет', 'Дама', 'Король', 'Туз']
RANKS_ALL = RANKS_N + RANKS_A

# инициализируем пустую колоду
card_deck = []

# заполняем колоду картами всех мастей и рангов
for i in RANKS_ALL:
    for j in SUITS:
        card = str(i) + ' ' + j
        card_deck.append(card)

# создаем объект итератора
card_deck_iterator = iter(card_deck)

# запускаем цикл while
while True:
    print(next(card_deck_iterator))



