
# ЗАДАНИЕ 1



msg = "Helloy world""\n"
print(msg)



# ЗАДАНИЕ 2



none_var = None
int_var = 42
float_var = 3.14
str_var = "Hello, World!"
list_var = [1, 2, 3, 4, 5]
tuple_var = (6, 7, 8, 9, 10)
dict_var = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
set_var = {11, 12, 13, 14, 15}

# Печать типа каждой переменной
variables = [none_var, int_var, float_var, str_var, list_var, tuple_var, dict_var, set_var]
for var in variables:
    type_name = type(var).__name__
    print(f"Тип переменной: {type_name}")

# Изменение типов для int и float
int_var = float(int_var)
float_var = str(float_var)

# Печать размера и данных для str, list, tuple, dict, set
for var in variables:
    if isinstance(var, str) or isinstance(var, list) or isinstance(var, tuple):
        print(f"Размер переменной: {len(var)}")
        if isinstance(var, str) or isinstance(var, tuple):
            print(f"Первый эллемент: {var[0]}")
            print(f"Последний эллемент: {var[-1]}")
            print(f"Эллемент кроме первого и последнего: {var[1:-1]}")

    if isinstance(var, dict):
        key = next(iter(var))
        print(f"Значение для ключа '{key}': {var[key]}""\n")
        




        # ЗАДАНИЕ 3




# создаем две переменные типа bool
var1 = True
var2 = False

# печатаем тип каждой переменной
print(f"Тип переменной var1: {type(var1)}")
print(f"Тип переменной var2: {type(var2)}")

# логические операции
print(f"Результат конъюнкции: {var1 and var2}")
print(f"Результат дизъюнкции: {var1 or var2}")
print(f"Результат инверсии var1: {not var1}")
print(f"Результат инверсии var2: {not var2}")

# создаем две переменные типа int с неравными значениями
int1 = 10
int2 = 5

# операции сравнения
print(f"Равны ли две переменные: {int1 == int2}")
print(f"Не равны ли две переменные: {int1 != int2}")
print(f"Первая переменная больше второй: {int1 > int2}")
print(f"Первая переменная меньше второй: {int1 < int2}")
print(f"Вторая переменная больше или равно первой: {int2 >= int1}")
print(f"Вторая переменная меньше или равно первой: {int2 <= int1}")

# арифметические операции
print(f"Сложение: {int1 + int2}")
print(f"Вычитание: {int1 - int2}")
print(f"Умножение: {int1 * int2}")
print(f"Деление: {int1 / int2}")
print(f"Возведение в степень: {int1 ** int2}")
print(f"Деление по модулю: {int1 % int2}")
print(f"Целочисленное деление: {int1 // int2}""\n")





# ЗАДАНИЕ 4




# Просим пользователя ввести число
num = int(input("Введите число на интервале от -100 до 100: "))

# Проверяем число и выводим соответствующее сообщение
if num < -100 or num > 100:
    print("Число не входит в диапазон [-100; 100]")
elif num < -50:
    print("Число меньше -50")
elif num == -50:
    print("Число равно -50")
elif num < 0:
    print("Число меньше 0, но больше -50")
elif num == 0:
    print("Число равно 0")
elif num < 50:
    print("Число больше 0, но меньше 50")
elif num == 50:
    print("Число равно 50")
else:
    print("Число больше 50""\n")
    





    # ЗАДАНИЕ 5





# Числа от 0 до 10 с помощью цикла for
print("Числа от 0 до 10 с помощью цикла for:")
for i in range(11):
    print(i)

# Числа от 0 до 10 с помощью цикла while
print("\nЧисла от 0 до 10 с помощью цикла while:")
num = 0
while num <= 10:
    print(num)
    num += 1

# Мое ФИО
full_name = "Иванов Иван Иванович"

# Печать каждой буквы ФИО через цикл for
print("\nБуквы моего ФИО:")
for letter in full_name:
    print(letter)

# Имена друзей
friends = ["Алексей", "Мария", "Екатерина"]

# Печать имен друзей через цикл for
print("\nИмена моих друзей:")
for friend in friends:
    print(friend)

# Словарь с датами рождения друзей
birthdays = {
    "Алексей": "15.03.1990",
    "Мария": "20.06.1985",
    "Екатерина": "05.12.1992"
}

# Печать имен и дат рождения друзей только летом или зимой
print("\nИмена и даты рождения друзей, родившихся летом или зимой:")
for friend, birthday in birthdays.items():
    month = int(birthday.split(".")[1])
    if month in [6, 7, 8, 12, 1, 2]:
        print(friend, "-", birthday)