# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

week_day = int(input("Введите число : "))

if 6 <= week_day <= 7 :
    print ("Это выходной!")
elif 0 < week_day < 7 :
    print ("Это будний день!")
else:
    print ("Число не соответстует дню недели!")