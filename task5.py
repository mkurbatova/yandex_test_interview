"""
E. Анаграммы
Ограничение времени	1 секунда
Ограничение памяти	20Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Даны две строки, состоящие из строчных латинских букв. Требуется определить, являются ли эти строки анаграммами, т. е. отличаются ли они только порядком следования символов.

Формат ввода
Входной файл содержит две строки строчных латинских символов, каждая не длиннее 100 000 символов. Строки разделяются символом перевода строки.

Формат вывода
Выходной файл должен содержать единицу, если строки являются анаграммами, и ноль в противном случае.

Пример 1
Ввод	Вывод
qiu
iuq       1
Пример 2
Ввод	Вывод
zprl
zprc      0

------------------------------------
реализация check - используем словари
реализация check2 - используем списки
"""
import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()


def check(str1, str2):
    if len(str1) != len(str2):
        return 0
    else:
        dict1 = dict()
        dict2 = dict()
        create_dict(s1, dict1)
        create_dict(s2, dict2)
        return int(dict1 == dict2)


def create_dict(string, dictionary):
    for c in string:
        if c in dictionary:
            dictionary[c] += 1
        else:
            dictionary[c] = 1


def check2(str1, str2):
    if len(str1) != len(str2):
        return 0
    else:
        list1 = list(str1)
        list2 = list(str2)
        list1.sort()
        list2.sort()
        return int(list1 == list2)


print(check(s1, s2))

