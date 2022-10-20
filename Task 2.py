# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint    
list = []
number = int(input('Введите размер списка: '))   
for i in range(number):
    list.append(randint(0,21))    
print(list)

product_pairs_numbers = []  
for i, item in enumerate(list):
    if i <= (len(list)-1)/2:
        product_pairs_numbers.append(item * list[-1-i])
print(product_pairs_numbers)