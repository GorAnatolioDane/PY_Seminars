# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#  Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# (-0.56) -> 11

def Input_Number(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = abs(float(input(f"{inputText}")))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def sum_Numbers(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum
num = Input_Number("Введите число:")
print(f"Сумма цифр числа = {sum_Numbers(num)}")


# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

def Input_Number(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Нужно ввести целое число!")
    return number

def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)
num = Input_Number("Введите целое число: ")

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведение чисел от 1 до {num}: {list} ")



# 3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]


import random

num =  int(input("Введите размер массива: "))
numbers = []
for i in range(num):
    numbers.append(random.randint(-9, 10))
print(f"Исходный массив: {numbers}")

i = 0
for n in numbers:
    i += 1
    if n < 0:
        numbers.insert(i, 0)
print(f"Конечный массив: {numbers}")