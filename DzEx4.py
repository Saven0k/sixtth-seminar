'''
3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
*Пример*
- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]
'''


def one_of_all():
    lst = list(input("Enter some numbers of 0 to 9: ").replace(',', ''))
    result = [ i  for i in range(1 , 10) if lst.count(f'{i}') == 1]
    print(result)
one_of_all()