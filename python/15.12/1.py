math_students = {"Анна","Борис","Виктор","Дарья","Елена"}
physics_students = {"Виктор","Георгий","Дарья","Иван","Ксения"}
cs_students = {"Анна","Виктор","Елена","Иван","Мария"}

all_3 = math_students & physics_students & cs_students
print(f"1. Студенты, которые посещают все три курса: {all_3}")

only_math = math_students - physics_students - cs_students
print(f"\n2. Студенты, которые посещают только математику: {only_math}")

all_unique = math_students | physics_students | cs_students
print(f"\n3. Все уникальные студенты: {all_unique}")

math_physics = math_students & physics_students
math_cs = math_students & cs_students
physics_cs = physics_students & cs_students

courses_2 = math_physics | math_cs | physics_cs
two = courses_2 - all_3

print(f"\n4. Студенты, которые посещают ровно два курса: {two}")
