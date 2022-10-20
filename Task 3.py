# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

from random import uniform    
list = []
number = int(input('Введите размер списка: '))
for i in range(number):
    list.append(uniform(0,11))    
list = [round(i % 1, 2) for i in list]
print(list)

result = max(list) - min(list)
print(f'Разница между max и min значением дробной части элементов = {result}')