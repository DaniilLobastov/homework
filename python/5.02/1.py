class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hungry = True
    
    def eat(self):
        if self.hungry:
            print(f'{self.name} покушает и стал сытым!')
            self.hungry = False
        else:
            print(f'{self.name} не голоден')
    
    def make_sound(self):
        print(f'{self.name} издает звук')
    
    def play(self):
        if not self.hungry:
            print(f'{self.name} весело играет!')
            self.hungry = True
        else:
            print(f'{self.name} сначала хочет кушать')
    
    def info(self):
        hungry_status = 'голоден' if self.hungry else 'сыт'
        print(f'Это {self.name}, возраст: {self.age}, {hungry_status}')


class Lion(Animal):
    def make_sound(self):
        print(f'{self.name} громко РЫЧИТ: РРРРР!')
    
    def play(self):
        print(f'{self.name} опасно играет - лучше не подходить!')


class Monkey(Animal):
    def make_sound(self):
        print(f'{self.name} кричит: У-у-у-у!')
    
    def play(self):
        super().play()
        print(f'    {self.name} весело прыгает по веткам!')


class Elephant(Animal):
    def make_sound(self):
        print(f'{self.name} трубит: ТУ-ТУ-У-У!')
    
    def eat(self):
        super().eat()
        print(f'    {self.name} съел целое ведро фруктов!')


class Penguin(Animal):
    def make_sound(self):
        print(f'{self.name} крякает: Кря-кря!')
    
    def play(self):
        super().play()
        print(f'    {self.name} скользит на животе по льду!')


def play_zoo():
    print('Добро пожаловать в зоопарк!\n')
    
    zoo = [
        Lion('Симба', 3),
        Monkey('Чита', 2),
        Elephant('Дамбо', 5),
        Penguin('Пинг', 1)
    ]
    
    while True:
        print('1 - Покормить животных')
        print('2 - Поиграть с животными')
        print('3 - Послушать животных')
        print('4 - Показать информацию')
        print('0 - Выйти из зоопарка')
        
        choice = input('\nВыбери действие: ')
        
        if choice == '0':
            print('Спасибо за посещение зоопарка!')
            break
        
        elif choice == '1':
            print('\nКормим животных:')
            for animal in zoo:
                animal.eat()
        
        elif choice == '2':
            print('\nИграем с животными:')
            for animal in zoo:
                animal.play()
        
        elif choice == '3':
            print('\nСлушаем животных:')
            for animal in zoo:
                animal.make_sound()
        
        elif choice == '4':
            print('\nИнформация о животных:')
            for animal in zoo:
                animal.info()
        
        else:
            print('Неверный выбор!')


if __name__ == '__main__':
    play_zoo()