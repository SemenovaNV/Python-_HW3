# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

number = int(input('Введите целое число: '))
# F(n) = F(n−1) + F(n− 2)

fibonacci_positive = []
for i in range(0, number+1):
    if i == 0:
        fibonacci_positive.insert(i, i)
    elif i == 1:
        fibonacci_positive.insert(i, i)
    else:
        fibonacci_positive.append(fibonacci_positive[i-1]+fibonacci_positive[i-2])
print (f'Для положительного индекса {number} список Фибоначчи {fibonacci_positive}')   

# Fn = F(n+2)−F(n+1)  F−n = (−1)**n+1Fn.
fibonacci_negative = []
for i in range(1, number+1):
    if i == 1:
        fibonacci_negative.insert(i, i)
    else:
        fibonacci_negative.append(((-1)**(i+1))*fibonacci_positive[i])
print (f'Для отрицательного индекса {number} список негаФибоначчи {fibonacci_negative}')   

fibonacci_negative.reverse()
fibonacci = fibonacci_negative + fibonacci_positive
print(f'Полный список фибоначчи {fibonacci}')