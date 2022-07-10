import json


def main():
    cost_day = 0
    f = open('store.json',)
    data = json.load(f)

    for i in data:
        cost_day += float(i['Price'])

    print(f'Стоимость покупок за день: {cost_day}')
    f.close()


main()
