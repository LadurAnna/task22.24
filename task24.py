"""Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
Она растёт на круглой грядке, причём кусты высажены только по
окружности. Таким образом, у каждого куста есть ровно два соседних.
Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора
на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора
черники. Эта система состоит из управляющего модуля и нескольких
собирающих модулей. Собирающий модуль за один заход, находясь
непосредственно перед некоторым кустом, собирает ягоды с этого
куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод,
которое может собрать за один заход собирающий модуль, находясь
перед некоторым кустом заданной во входном файле грядки.
Сможешь подготовиться? что бы мы не тратили время на обдумывание решений
Если что можем начать попозже"""

# Из условий не ясно откуда брать файл грядки.
# Считываю "a" и "n" с консоли

a = int(input())
n = int(input())
if n<1:
    print(0)
if n==1:
    print(a)
if n==2:
    print(a+2*a)
if n >= 3:
    s = (n - 2) * a + (n - 1) * a + n * a
    print(s)