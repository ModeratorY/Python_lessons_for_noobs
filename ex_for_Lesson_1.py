# Задачи для Lesson_1

print("\nЗадача 1: Поэкспериментируйте с переводом в различные типы данных\n")

a = 10.45
A = int(a)
print("A =", A, end = '\n\n')

b1 = input("Введите какое-нибудь число: ")
b2 = input("Введите какое-нибудь ещё число: ")
print("Итог сложения:", b1 + b2)

c1 = int(b1)
c2 = int(b2)

print("Итог сложения после приведения типов:", c1 + c2)



print("\nЗадача 2: Пользователь вводит свое имя и фамилию. Выведите: Hello, имя фамилия\n")

name_and_surname = input("Введи своё ИФ: ")
print("Hello,", name_and_surname)




print("\nЗадача 3: Посчитайте сумму трех введенных целых чисел\n")

num1 = int(input("Введи 1-ое число:"))
num2 = int(input("Введи 2-ое число:"))
num3 = int(input("Введи 3-ье число:"))

print("Сумма =", num1 + num2 + num3)



print("\nЗадача 4: Посчитайте сумму трех введенных дробных чисел\n")

num_1 = float(input("Введи 1-ое число:"))
num_2 = float(input("Введи 2-ое число:"))
num_3 = float(input("Введи 3-ье число:"))

print("Сумма =", num_1 + num_2 + num_3)



print("\nЗадача 5: Дано число, выведите предыдущее и следущее за ним числа\n")

number = int(input("Введи одно целое число:"))
print("Число предшествующее числу", number, "равно", (number-1))
print("Число следующее за числом", number, "равно", (number+1))



print("\nЗадача 6: Вводятся имя и возраст. Вывести шаблоном: Привет, Макс! Ваш возраст равен 20!\n")

Name = input("Введите своё имя:")
age  = input("Введите свой возраст:")

print("Привет, " + Name + "! Ваш возраст равен " + age + "!")
