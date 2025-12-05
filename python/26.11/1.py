days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
hours_day = [0] * 7 

def input_hours(index):
    while True:
        try:
            print(f"Сейчас для {days[index]} введено: {hours_day[index]} часов.")
            hours = int(input(f"Введите новое количество часов для {days[index]}: "))
            if hours >= 0:
                hours_day[index] = hours
                break
            else:
                print("Часы не могут быть отрицательными.")
        except ValueError:
            print("Введите число!")

def automatic():
    while True:
        try:
            n_days = int(input("Сколько учебных дней на этой неделе? (1-7): "))
            if 1 <= n_days <= 7:
                break
            else:
                print("Введите число от 1 до 7.")
        except ValueError:
            print("Введите число!")
    for i in range(n_days):
        input_hours(i)
    print(f"Общее количество часов: {sum(hours_day[:n_days])}")

def default():
    while True:
        try:
            choice = int(input("Выберите день (1-Пн, 2-Вт, ..., 7-Вс): "))
            if 1 <= choice <= 7:
                input_hours(choice - 1) 
                break
            else:
                print("Введите число от 1 до 7.")
        except ValueError:
            print("Введите число!")
    print(f"Общее количество часов: {sum(hours_day)}")

def menu():
    while True:
        try:
            choice = int(input("Меню:\n1. Автоматический режим\n2. Ручной режим\n3. Выход\nВыбор: "))
            if choice == 1:
                automatic()
            elif choice == 2:
                default()
            elif choice == 3:
                print("Выход.")
                break
            else:
                print("Введите 1, 2 или 3.")
        except ValueError:
            print("Введите число!")

menu()
