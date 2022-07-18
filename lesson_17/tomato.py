# Растение томата в своем онтогенезе проходят следующие фазы:
# появление всходов, первого настоящего листа, разрастание надземной массы и корней,
# образование бутонов, цветение, формирование и созревание плодов.

class Tomato:

# Перечень стадий созревания томатов в виде словаря
    states = {
        0: 'появление всходов', 1: 'первый настоящий лист', 2: 'разрастание надземной массы и корней',
        3: 'образование бутонов', 4: 'цветение', 5: 'формирование и созревание плодов'
    }

# Свойства томатов, индекс и стадии роста томатов
    def __init__(self, index):
        self._index = index
        self._state = 0

# Метод роста томатов, плюс + 1, от 0
    def grow(self):
        if self._state < 5:
            self._state = self._state + 1
        self.print_status()

# Метод для проверки на созревание томата, если стадия 5 то финиш
    def is_ripe(self):
        if self._state == 5:
            print('Томат созрел')
            return True
        print('Томат не созрел')
        return False

# Метод показывает текущий статус томата
    def print_status(self):
        print(f'Томат {self._index} в стадии: {Tomato.states[self._state]}')


#````````````````````````````````````````````````````````````````````
class TomatoBush:
# Создание списка объектов класса Tomato с использованием списка и циклов
    def __init__(self, numbers_tomato):
        lst_tomatos = [Tomato(i) for i in range(0, numbers_tomato)]
        self.tomatos = lst_tomatos
        
# Метод массового созревания томатов
    def grow_all(self):
        for tomato in self.tomatos:
            tomato.grow()

# Массовая проверка созревания томатов
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatos])

# Метод для массовой уборки урожая, и краткой информации об уборке
    def give_away_all(self):
        a = len(self.tomatos)
        print(f'Было посажено: {a} ')
        self.tomatos = []
        b = len(self.tomatos)
        print(f'Убрано: {a} томатов, сейчас: {b} томатов')


#````````````````````````````````````````````````````````````````````
# Создание класса садовник
class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

# Метод ухода за растениями из предыдущего класса
    def work(self):
        print('Садовник работает ... ')
        self._plant.grow_all()
        print('Садовник окончил работу')

# Метод уборки урожая, также вызываем два метода используя предыдущий класс
    def harvest(self):
        print('Садовник убирает урожай ... ')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Садовник убрал урожай')
        else:
            print('Слишком рано! Плантация томатов еще не созрела !!!')

# Статический метод. Небольшая справка по садоводству
    @staticmethod
    def knowledge_base():
        print('''Растение томата в своем онтогенезе проходят следующие фазы: 
появление всходов, первого настоящего листа, 
разрастание надземной массы и корней, образование бутонов, 
цветение, формирование и созревание плодов.''')


if __name__ == '__main__':
# Экземпляр класса томат
    tomato_by = Tomato(0)
    tomato_by.grow()
    tomato_by.grow()
    tomato_by.grow()
    tomato_by.grow()
    tomato_by.grow()
    tomato_by.is_ripe()
    tomato_by.print_status()

    print('``````````````````````````````````````')
    
# Создание плантации помидоров (томатов)
    big_farm_tomato_bush = TomatoBush(32)
# Запуск метода роста
    big_farm_tomato_bush.grow_all()
# Запуск метода проверки созревания
    big_farm_tomato_bush.all_are_ripe()
# Уборка урожая томатов, очистка списка
    big_farm_tomato_bush.give_away_all()

    big_farm_tomato_bush

    print('``````````````````````````````````````')

# Создание экземпляра класса садовника и передачи в него экземпляра класса TomatoBush
# для этого создадим новый экз класса new_farm из 8 элементов
# и несколько раз запустим садовника на работу с попыткой уборки урожая, когда
# будет возможность, произойдет уборка урожая

    new_farm = TomatoBush(8)
    farmer = Gardener('Piter', new_farm)
    farmer.work()
    farmer.harvest()
    farmer.work()
    farmer.work()
    farmer.harvest()
    farmer.work()
    farmer.work()
    farmer.harvest()
    Gardener.knowledge_base()

    print('``````````````````````````````````````')
