# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

numbers = list(map(int,input('Введите числа через пробел: ').split()))
print(numbers)
sum = 0
for i in range(numbers[1], numbers[-1]+1, 2):  # считаем нечетные позиции 1,3,5 от индекса 0
    print(i)
    sum += i
print(f'Сумма элементов на нечетных позициях = {sum}')

# print(f'Сумма элементов на нечетных позициях = {sum(numbers[1::2])}')