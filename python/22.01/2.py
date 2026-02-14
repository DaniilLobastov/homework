class City:
    def __init__(self):
        self.name = ''
        self.region = ''
        self.country = ''
        self.population = 0
        self.postal_code = ''
        self.phone_code = ''
    
    def input_data(self):
        self.name = input('Введите название города: ')
        self.region = input('Введите название региона: ')
        self.country = input('Введите название страны: ')
        self.population = int(input('Введите количество жителей: '))
        self.postal_code = input('Введите почтовый индекс: ')
        self.phone_code = input('Введите телефонный код: ')
    
    def output_data(self):
        print(f'Город: {self.name}')
        print(f'Регион: {self.region}')
        print(f'Страна: {self.country}')
        print(f'Население: {self.population}')
        print(f'Почтовый индекс: {self.postal_code}')
        print(f'Телефонный код: {self.phone_code}')
    
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    
    def get_region(self): return self.region
    def set_region(self, region): self.region = region
    
    def get_country(self): return self.country
    def set_country(self, country): self.country = country
    
    def get_population(self): return self.population
    def set_population(self, population): self.population = population
    
    def get_postal_code(self): return self.postal_code
    def set_postal_code(self, code): self.postal_code = code
    
    def get_phone_code(self): return self.phone_code
    def set_phone_code(self, code): self.phone_code = code

if __name__ == '__main__':
    print('Класс Город')
    c = City()
    c.input_data()
    print('\nВведенные данные:')
    c.output_data()