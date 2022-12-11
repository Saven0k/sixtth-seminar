'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
Негафибоначчи
F−n = (−1)n+1Fn.

number = int(input("Enter number: "))

def fibonaci(n):
    if n in {0, 1}:
        return n
    else:
        return fibonaci(n - 1) + fibonaci(n - 2)


def negafibonachi(n):
    result = []
    for i in range(-n, 0):
        result.append(int(((-1) ** (i + 1)) * fibonaci(-i)))
    for i in range(-number + 1):
        result.append(fibonaci(i))
    print(result)

negafibonachi(number)


'''

fib = (lambda n : n if n in {0 , 1} else fib(n - 1) + fib(n - 2))
result = [(int(((-1) ** (i + 1)) * fib(-i))) for i in range(-number, 0)] + [fib(g) for g in range(-number + 1)]
print(result)
