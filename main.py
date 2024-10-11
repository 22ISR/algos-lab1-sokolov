"""
 _____         _      __  
|_   _|       | |    /  | 
  | | __ _ ___| | __ `| | 
  | |/ _` / __| |/ /  | | 
  | | (_| \__ \   <  _| |_
  \_/\__,_|___/_|\_\ \___/

Напишите программу, которая выводит в консоль "Hello world"

hint: что такое print?
"""

#print("Hello world")

"""
 _____         _      _____ 
|_   _|       | |    / __  \
  | | __ _ ___| | __ `' / /'
  | |/ _` / __| |/ /   / /  
  | | (_| \__ \   <  ./ /___
  \_/\__,_|___/_|\_\ \_____/

Напишите рограмму, которая выводит числа от 1 до введенного пользователем. Для чисел, кратных 3, выводится "Fizz",'
для кратных 5 — "Buzz", а для чисел, кратных 3 и 5 — "FizzBuzz"

hint: цикл, если и "%"
"""

#x = int(input("Введите число")) + 1 
#for i in range(1,x):
#  if i % 3 == 0 and i % 5 == 0:
#    print("FizzBuzz")
#  elif i % 3 == 0:
#    print("Fizz")
#  elif i % 5 == 0:
#    print("Buzz")
#  else:
#    print(i)

"""
 _____         _      _____ 
|_   _|       | |    |____ |
  | | __ _ ___| | __     / /
  | |/ _` / __| |/ /     \ \
  | | (_| \__ \   <  .___/ /
  \_/\__,_|___/_|\_\ \____/ 

Напишите программу, которая проверяет, является ли введенный пользователем год високосным

hint: https://ru.wikihow.com/%D0%B2%D1%8B%D1%81%D1%87%D0%B8%D1%82%D1%8B%D0%B2%D0%B0%D1%82%D1%8C-%D0%B2%D0%B8%D1%81%D0%BE%D0%BA%D0%BE%D1%81%D0%BD%D1%8B%D0%B5-%D0%B3%D0%BE%D0%B4%D1%8B
"""

#x = int(input("Введите год.."))
#if x % 4 == 0 and x % 100 == 0:
#  print("Весокосный год")
#elif x % 100 == 0 and x % 400 == 0:
#  print("Весокосный год")
#else:
#  print(x, "Весокосный год")

"""
 _____         _        ___ 
|_   _|       | |      /   |
  | | __ _ ___| | __  / /| |
  | |/ _` / __| |/ / / /_| |
  | | (_| \__ \   <  \___  |
  \_/\__,_|___/_|\_\     |_/

Напишите программу, которая проверяет, является ли введенная пользователем строка или число палиндромом, то есть читается ли оно одинаково с обеих сторон

hint: https://letpy.com/handbook/builtins/reversed/
"""

# def is_palindrome(value):
#     value_str = str(value).replace(" ", "").lower()
#     return value_str == value_str[::-1]
# user_input = input("Введите строку или число: ")
# if is_palindrome(user_input):
#     print(f'"{user_input}" является палиндромом.')
# else:
#     print(f'"{user_input}" не является палиндромом.')

"""
 _____         _      _____ 
|_   _|       | |    |  ___|
  | | __ _ ___| | __ |___ \ 
  | |/ _` / __| |/ /     \ \
  | | (_| \__ \   <  /\__/ /
  \_/\__,_|___/_|\_\ \____/ 

Напишите программу, которая запрашивает число у пользователя и вычисляет факториал заданного числа, используя цикл или рекурсию

hint: https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%BA%D1%82%D0%BE%D1%80%D0%B8%D0%B0%D0%BB
"""
# def factorial_iterative(x):
#     if x < 0:
#         return "Факториал отрицательного числа не существует."
#     result = 1
#     for i in range(2, x + 1):
#         result *= i
#     return result

# number = int(input("Введите число для вычисления факториала: "))
# print(f"Факториал числа {number} равен {factorial_iterative(number)}")

# def factorial_recursive(x):
#     if x < 0:
#         return "Факториал отрицательного числа не существует."
#     if x == 0 or x == 1:
#         return 1
#     return x * factorial_recursive(x - 1)

# number = int(input("Введите число для вычисления факториала: "))
# print(f"Факториал числа {number} равен {factorial_recursive(number)}")


"""
 _____         _       ____ 
|_   _|       | |     / ___|
  | | __ _ ___| | __ / /___ 
  | |/ _` / __| |/ / | ___ \
  | | (_| \__ \   <  | \_/ |
  \_/\__,_|___/_|\_\ \_____/

Напишите программу, которая проверяет, является ли число простым (делится только на 1 и само на себя). Используйте перебор делителей.

hint: x <= 1 - не простые числа
hint 2: %
"""


# def is_prime(x):
#     if x <= 1:
#         return False
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % i == 0:
#             return False
#     return True

# user_input = int(input("Введите число: "))
# if is_prime(user_input):
#     print(f"{user_input} является простым числом.")
# else:
#     print(f"{user_input} не является простым числом.")

"""
 _____         _      ______
|_   _|       | |    |___  /
  | | __ _ ___| | __    / / 
  | |/ _` / __| |/ /   / /  
  | | (_| \__ \   <  ./ /   
  \_/\__,_|___/_|\_\ \_/    

Напишите программу, которая находит сумму всех цифр числа

hint: циклы
"""


# def sum_of_digits(number):
#     return sum(int(digit) for digit in str(number) if digit.isdigit())
# user_input = input("Введите число: ")
# result = sum_of_digits(user_input)
# print(f"Сумма всех цифр числа {user_input} равна {result}.")

"""
 _____         _      _____ 
|_   _|       | |    |  _  |
  | | __ _ ___| | __  \ V / 
  | |/ _` / __| |/ /  / _ \ 
  | | (_| \__ \   <  | |_| |
  \_/\__,_|___/_|\_\ \_____/

Напишите программу, которая генерирует последовательность Фибоначчи до указанного числа или количества элементов

hint: 1, 1, 2, 3 https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8
hint 2: попробуйте решить с помощью рекурсии
"""

# def fibonacci_up_to(max_value):
#     sequence = []
#     a, b = 0, 1
#     while a <= max_value:
#         sequence.append(a)
#         a, b = b, a + b
#     return sequence
# max_value = int(input("Введите максимальное значение для последовательности Фибоначчи: "))
# fibonacci_sequence = fibonacci_up_to(max_value)
# print("Последовательность Фибоначчи до", max_value, ":", fibonacci_sequence)




