'''
1. Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.

*Пример:*

2+2 => 4;
7-8+3*5+1+1+2*3 => 22;

a = '7-82+3*5+13+1+25*3'

b = ['7', '-', '82', '+', '3', '*', '5', '+', '13', '+', '1', '+', '25', '*', '3']

7, -8, 15, 1, 1, 6


1-2*3 => -5;

2. Добавьте возможность использования скобок, меняющих приоритет операций.

1+2*3 => 7;
(1+2)*3 => 9;
'''
a = "2 - 2 * 2 + 10"



def myeval(s):
    lst = s.split()
    res = []
    j = 0
    for key, item in enumerate(lst):
        if item.isdigit():
            if key == 0:
                res.append(int(item))
                j += 1
            else:
                if lst[key - 1] == "*":
                    res.remove(res[j - 1])
                    if key - 3 >= 0:
                        res.append(int(f"{lst[key - 3]}{lst[key - 2]}") * int(item))
                    else:
                        res.append(int(f"{lst[key - 3]}{lst[key - 2]}") * int(item))
                    j += 1
                else:
                    res.append(int(f"{lst[key - 1]}{item}"))
                    j += 1
    print(res)
    print(sum(res))
myeval(a)







a = ' 2 -3 -4 -5 - (4   * 5) '