class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
    
    def input_data(self):
        self.numerator = int(input('Введите числитель: '))
        self.denominator = int(input('Введите знаменатель: '))
        if self.denominator == 0:
            print('Знаменатель не может быть 0! Установлено значение 1.')
            self.denominator = 1
    
    def output_data(self):
        print(f'{self.numerator}/{self.denominator}')
    
    def get_numerator(self): return self.numerator
    def set_numerator(self, num): self.numerator = num
    
    def get_denominator(self): return self.denominator
    def set_denominator(self, den): 
        if den != 0:
            self.denominator = den
        else:
            print('Знаменатель не может быть 0!')
    
    def add(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)
    
    def subtract(self, other):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)
    
    def multiply(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)
    
    def divide(self, other):
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)
    
if __name__ == '__main__':
    print('Класс Дробь')
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    print('Дробь 1:', end=' ')
    f1.output_data()
    print('Дробь 2:', end=' ')
    f2.output_data()
    
    print('Сложение:', end=' ')
    f1.add(f2).output_data()
    
    print('Вычитание:', end=' ')
    f1.subtract(f2).output_data()
    
    print('Умножение:', end=' ')
    f1.multiply(f2).output_data()
    
    print('Деление:', end=' ')
    f1.divide(f2).output_data()