# yandex_test_interview
Задачи для подготовки к предварительному интервью с Яндекс
--

B. Последовательно идущие единицы

Ограничение времени	1 секунда

Ограничение памяти	64Mb

Ввод	стандартный ввод или input.txt

Вывод	стандартный вывод или output.txt

Требуется найти в бинарном векторе самую длинную последовательность единиц и вывести её длину.

Желательно получить решение, работающее за линейное время и при этом проходящее по входному массиву только один раз.

Формат ввода

Первая строка входного файла содержит одно число n, n ≤ 10000. Каждая из следующих n строк содержит ровно одно число —
очередной элемент массива.

Формат вывода

Выходной файл должен содержать единственное число — длину самой длинной последовательности единиц во входном массиве.


Пример

Ввод	
5
1
0
1
0
1          

Вывод 1

--


C. Удаление дубликатов

Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод

Все языки	1 секунда	10Mb	стандартный ввод или input.txt	стандартный вывод или output.txt

Oracle Java 7	1 секунда	20Mb

Node JS 8.9.4	1 секунда	20Mb

Oracle Java 8	1 секунда	20Mb

Kotlin	1 секунда	20Mb

Дан упорядоченный по неубыванию массив целых 32-разрядных чисел. Требуется удалить из него все повторения.

Желательно получить решение, которое не считывает входной файл целиком в память, т.е., использует лишь константный объем памяти в процессе работы.

Формат ввода

Первая строка входного файла содержит единственное число n, n ≤ 1000000.

На следующих n строк расположены числа — элементы массива, по одному на строку. Числа отсортированы по неубыванию.

Формат вывода

Выходной файл должен содержать следующие в порядке возрастания уникальные элементы входного массива.

Пример 1

Ввод	
5         
2         
4         
8
8
8

Вывод 2 4 8

Пример 2

Ввод	
5       
2       
2
2
8
8

Вывод 2 8

--
D. Генерация скобочных последовательностей

Ограничение времени	1 секунда

Ограничение памяти	20Mb

Ввод	стандартный ввод или input.txt

Вывод	стандартный вывод или output.txt

Дано целое число n. Требуется вывести все правильные скобочные последовательности длины 2 ⋅ n, упорядоченные лексикографически (см. https://ru.wikipedia.org/wiki/Лексикографический_порядок).

В задаче используются только круглые скобки.

Желательно получить решение, которое работает за время, пропорциональное общему количеству правильных скобочных последовательностей в ответе, и при этом использует объём памяти, пропорциональный n.

Формат ввода

Единственная строка входного файла содержит целое число n, 0 ≤ n ≤ 11

Формат вывода

Выходной файл содержит сгенерированные правильные скобочные последовательности, упорядоченные лексикографически.

Пример 1

Ввод	
2

Вывод   (())
        ()()    
        
Пример 2 

Ввод	 3

Вывод   ((()))
        (()())
        (())()
        ()(())
        ()()()
        
--


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

Ввод	
qiu
iuq       

Вывод 1

Пример 2

Ввод	
zprl
zprc      

Вывод 0

--


F. Слияние k сортированных списков

Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод

Все языки	1 секунда	10Mb	стандартный ввод или input.txt	стандартный вывод или output.txt

Oracle Java 7	1 секунда	20Mb

Node JS 8.9.4	1 секунда	20Mb

Oracle Java 8	1 секунда	20Mb

Kotlin	1 секунда	20Mb

Даны k отсортированных в порядке неубывания массивов неотрицательных целых чисел, каждое из которых не превосходит 100. Требуется построить результат их слияния: отсортированный в порядке неубывания массив, содержащий все элементы исходных k массивов.

Длина каждого массива не превосходит 10 ⋅ k.

Постарайтесь, чтобы решение работало за время k ⋅ log(k) ⋅ n, если считать, что входные массивы имеют длину n.

Формат ввода

Первая строка входного файла содержит единственное число k, k ≤ 1024.

Каждая из следующих k строк описывает по одному массиву. Первое число каждой строки равняется длине соответствующего массива, оставшиеся числа этой строки описывают значения элементов этого же массива. Элементы массивов являются неотрицательными целыми числами и не превосходят 100.

Формат вывода

Выходной файл должен содержать отсортированный в порядке неубывания массив, содержащий все элементы исходных массивов.

Пример

Ввод	

4
6 2 26 64 88 96 96
4 8 20 65 86
7 1 4 16 42 58 61 69
1 84

Вывод

1 2 4 8 16 20 26 42
58 61 64 65 69 84 86
88 96 96 
