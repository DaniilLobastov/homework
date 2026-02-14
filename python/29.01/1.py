class Weapon:
    def __init__(self, damage, modifier):
        self.damage = damage
        self._modifier = modifier
    
    def __apply_modifier(self):
        return self.damage * self._modifier
    
    def get_final_damage(self):
        return self.__apply_modifier()


class GameBank:
    def __init__(self, start_balance=0):
        self._balance = start_balance
    
    def __log_transaction(self, amount, operation):
        print(f'{operation}: {amount} монет. Баланс: {self._balance}')
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.__log_transaction(amount, 'Депозит')
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.__log_transaction(amount, 'Снятие')
            return True
        return False
    
    def get_balance(self):
        return self._balance


if __name__ == '__main__':
    sword = Weapon(10, 1.5)
    print(f'Базовый урон: {sword.damage}')
    print(f'Итоговый урон: {sword.get_final_damage()}')
    
    bank = GameBank(100)
    bank.deposit(50)
    bank.withdraw(30)
    print(f'Текущий баланс: {bank.get_balance()}')