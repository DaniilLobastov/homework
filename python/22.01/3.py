class Country:
    def __init__(self):
        self.name = ''
        self.continent = ''
        self.population = 0
        self.phone_code = ''
        self.capital = ''
        self.cities = []
    
    def input_data(self):
        self.name = input('Введите название страны: ')
        self.continent = input('Введите название континента: ')
        self.population = int(input('Введите количество жителей: '))
        self.phone_code = input('Введите телефонный код: ')
        self.capital = input('Введите название столицы: ')
        
        n = int(input('Сколько городов ввести? '))
        self.cities = []
        for i in range(n):
            city = input(f'Введите название города {i+1}: ')
            self.cities.append(city)
    
    def output_data(self):
        print(f'Страна: {self.name}')
        print(f'Континент: {self.continent}')
        print(f'Население: {self.population}')
        print(f'Телефонный код: {self.phone_code}')
        print(f'Столица: {self.capital}')
        print(f'Города: {', '.join(self.cities)}')
    
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    
    def get_continent(self): return self.continent
    def set_continent(self, continent): self.continent = continent
    
    def get_population(self): return self.population
    def set_population(self, population): self.population = population
    
    def get_phone_code(self): return self.phone_code
    def set_phone_code(self, code): self.phone_code = code
    
    def get_capital(self): return self.capital
    def set_capital(self, capital): self.capital = capital
    
    def get_cities(self): return self.cities
    def set_cities(self, cities): self.cities = cities
    def add_city(self, city): self.cities.append(city)

if __name__ == '__main__':
    print('Класс Страна')
    c = Country()
    c.input_data()
    print('\nВведенные данные:')
    c.output_data()