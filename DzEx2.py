'''
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''

'''
Было

def sum_numbers():
    lst = []
    result = []
    n = int(input("Enter size list: "))
    for i in range(n):
        lst.append(int(input("Enter some number: ")))
    print(lst)
    if n % 2 == 0:
        for i in range(0, ((len(lst) // 2))):
            result.append(lst[i] * lst[len(lst) - 1 - i])
    else:
        for i in range(0, ((len(lst) // 2) + 1)):
            result.append(lst[i] * lst[len(lst) - 1 - i])

    print(result)

Стало
'''


def sum_numbers2():
    n = int(input("Enter size list: "))
    lst = [int(input("Enter some number: ")) for i in range(n) ]
    print(lst)
    if n % 2 == 0:
        result = [(lst[i] * lst[len(lst) - 1 - i]) for i in range(0, ((len(lst) // 2)))]
    else:
        result = [(lst[i] * lst[len(lst) - 1 - i]) for i in range(0, ((len(lst) // 2) + 1))]
    return result
print(sum_numbers2())



#ля красивого вывода
def lst_to_str(lst):
    string_ = ' '.join(f'{i}' for i in lst)
    print(string_)

lst_to_str(sum_numbers2())