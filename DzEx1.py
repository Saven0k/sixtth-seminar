'''
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



def sum_numbers():
    lst = []
    n = int(input("Enter size list: "))
    for i in range(n):
        lst.append(int(input("Enter some number: ")))
    print(lst)
    result = 0
    for i in range(1 , len(lst), 2):
        result += lst[i]
    print(result)
sum_numbers()

Было так

'''

'''
1 предложить улучшения кода для четырёх уже решённых задач:

С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension


Начиная с 3 семинара.

def sum_numbers():
    lst = []
    n = int(input("Enter size list: "))
    for i in range(n):
        lst.append(int(input("Enter some number: ")))
    print(lst)
    result = 0
    for i in range(1 , len(lst), 2):
        result += lst[i]
    print(result)
'''
def sum_numbers_new():
    n = int(input("Enter size list: "))
    lst = [int(input("Enter some number: ")) for i in range(n)]
    print(lst)
    result = 0
    for i in range(1, len(lst), 2):
        result += lst[i]
    print(result)

sum_numbers_new()