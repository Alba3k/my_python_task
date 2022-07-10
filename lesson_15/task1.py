import json


def main():
    name_product = input('Введите название покупки: ')
    price_product = input('Введите цену покупки: ')

    checkout = {}
    lst_store = []

    checkout['Naming'] = name_product
    checkout['Price'] = price_product
    lst_store.append(checkout)

    another = input('Добавить еще покупки (yes / stop): ')

    while another != 'stop':
        checkout = {}

        name_product = input('Введите название покупки: ')
        price_product = input('Введите цену покупки: ')

        checkout['Naming'] = name_product
        checkout['Price'] = price_product
        lst_store.append(checkout)

        another = input('Добавить еще покупки (yes / stop): ')

    print('У Вас в корзине: ', len(lst_store), ' покупок')
    [print(i['Naming'] + ' по цене: ' + i['Price']) for i in lst_store]

    export_json = json.dumps(lst_store)

    f = open('store.json', 'w')
    f.write(export_json)
    f.close()


main()
