class Human:
    def __init__(self):
        self.full_name = ''
        self.birth_date = ''
        self.phone = ''
        self.city = ''
        self.country = ''
        self.address = ''
    
    def input_data(self):
        self.full_name = input('Введите ФИО: ')
        self.birth_date = input('Введите дату рождения: ')
        self.phone = input('Введите телефон: ')
        self.city = input('Введите город: ')
        self.country = input('Введите страну: ')
        self.address = input('Введите адрес: ')
    
    def output_data(self):
        print(f'ФИО: {self.full_name}')
        print(f'Дата рождения: {self.birth_date}')
        print(f'Телефон: {self.phone}')
        print(f'Город: {self.city}')
        print(f'Страна: {self.country}')
        print(f'Адрес: {self.address}')
    
    def get_full_name(self): return self.full_name
    def set_full_name(self, name): self.full_name = name
    
    def get_birth_date(self): return self.birth_date
    def set_birth_date(self, date): self.birth_date = date
    
    def get_phone(self): return self.phone
    def set_phone(self, phone): self.phone = phone
    
    def get_city(self): return self.city
    def set_city(self, city): self.city = city
    
    def get_country(self): return self.country
    def set_country(self, country): self.country = country
    
    def get_address(self): return self.address
    def set_address(self, address): self.address = address

if __name__ == '__main__':
    print('Класс Человек')
    h = Human()
    h.input_data()
    print('\nВведенные данные:')
    h.output_data()