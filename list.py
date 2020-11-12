ПРЕОБРАЗОВАНИЕ В СПИСОК
первый вариант
# numbers1 = []
# numbers2 = list()
# print(type(numbers2))

второй вариант
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers2 = list(numbers)

ОБРАЩЕНИЕ ПО ИНДЕКСУ И ПО КЛЮЧУ
# numbers = [1, 2, 3, 4, {'A' : 15, 'B': [1, 2, {'ithub': True}, 'qwe']}, 'test']
# print(numbers)
# print(numbers[-2])
# print(numbers[-2]['B'])
# print(numbers[-2]['B'][-2])
# print(numbers[-2]['B'][-2]['ithub'])


ЗАМЕНА ЭЛЕМЕНТА
# numbers[0] = 125  # изменяем первый элемент списка
# print(numbers)


ДУБЛИРОВАНИЕ СПИСКА
# numbers = [5] * 6
# print(numbers)


ФУНКЦИЯ RANGE
# numbers = list(range(10))
# print(numbers)    
# numbers = list(range(1, 10 + 1))
# print(numbers)    
# numbers = list(range(10, 1, -2))
# print(numbers)  

В ДАННОМ СЛУЧАЕ ОБА СПИСКА АНАЛОГИЧНЫ, НО С ПОМОЩЬЮ RANGE МЫ СОКРАЩАЕМ КОД
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers)
# numbers2 = list(range(1, 10000))
# print(numbers2)



ПЕРЕБОР ЭЛЕМЕНТОВ С ПОМОЩЬЮ ЦИКЛА FOR
# companies = ["Microsoft", "Google", "Oracle", "Apple"]
# for x in companies:
#     print(x)



ПЕРЕБОР ЭЛЕМЕНТОВ С ПОМОЩЬЮ ЦИКЛА WHILE
# companies = ["Microsoft", "Google", "Oracle", "Apple"]
# i = 0
# while i < len(companies):
#     print(companies[i])
#     i += 1




СРАВНИВАНИЕ ДВУХ СПИСКОВ
# numbers = [1, 2, 3, 5, 4, 6, 7, 8, 9]
# numbers2 = list(range(1,10))
# if numbers is numbers2:
#     print("numbers equal to numbers2")
# else:
#     print("numbers is not equal to numbers2")




ПРОВЕРКА НА НАЛИЧИЕ ЭЛЕМЕНТА
# companies = ["Microsoft", "Google", "Oracle", "Apple"]
# item = "Oracle"  # элемент для удаления
# if item in companies:
#     companies.remove(item)
# print(companies)


ПОДСЧЕТ СИМВОЛОВ
# users = ["Tom", "Bob", "Alice", "Tom", "Bill", "Tom"]
# users_count = users.count("Tom")
# print(users_count) 


СОРТИРОВКА ПО ВОЗРАСТАНИЮ
# users = ["Tom", "Bob", "Alice", "Sam", "Bill"]
# users.sort()
# print(users)


СОРТИРОВКА В ОБРАТНОМ ПОРЯДКЕ
# users = ["Tom", "Bob", "Alice", "Sam", "Bill"]
# users.sort()
# users.reverse()
# print(users)  



# users = ["Tom", "bob", "alice", "Sam", "Bill"]
# users.sort(key=str.lower)
# print(users) ??????????????????



# users = ["Tom", "bob", "alice", "Sam", "Bill"]
# sorted_users = sorted(users, key=str.lower)
# print(users)
# print(sorted_users) ???????????????????????????


МИНИМАЛЬНЫЕ И МАКСИМАЛЬНЫЕ ЗНАЧЕНИЯ
# numbers = [9, 21, 12, 1, 3, 15, 18]
# print('Minimum numnber is: ', min(numbers))
# print('Maximum number is: ', max(numbers))  


КОПИРОВАНИЕ ЧАСТИ СПИСКА
# users = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
# slice_users1 = users[:3]   # с 0 по 3
# print(slice_users1) #[Tom, Bob, Alice]



 СОЕДИНЕНИЕ ДВУХ СПИСКОВ С +
# users1 = ["Tom", "Bob", "Alice"]
# users2 = ["Tom", "Sam", "Tim", "Bill"]
# users3 = users1 + users2
# print(users3)   # ["Tom", "Bob", "Alice", "Tom", "Sam", "Tim", "Bill"]


СПИСОК В СПИСКЕ (ОБРАЩЕНИЕ К ЭЛЕМЕНТАМ)
# users = [
#   [1, 2, 3],
#   {
#     'A': 'ABC',
#     'B' : 3,
#     'C': True,
#     'List' : [
#       1,
#       2,
#       3,
#       ['A', 'B', 'C']
#     ]
#   }
# ]
 
# print(users[1]['List'][1])
# print(users[-1]['List'][-3])




 
# users = [
#     ["Tom", 29],
#     ["Alice", 33],
#     ["Bob", 27] ]

# # # создание вложенного списка
# user = list()
# user.append("Bill")
# user.append(41)
# print(user)
# # # добавление вложенного списка
# users.append(user)
# print(users[-1])         # ["Bill", 41]
# # # добавление во вложенный список
# users[-1].append("+79876543210")
# print(users[-1])         # ["Bill", 41, "+79876543210"]
# # удаление последнего элемента из вложенного списка
# users[-1].pop()
# print(users[-1])         # ["Bill", 41]
# # удаление всего последнего вложенного списка
# users.pop(-1)
# # изменение первого элемента
# users[0] = ["Sam", 18]
# print(users)       # [ ["Sam", 18], ["Alice", 33], ["Bob", 27]]






ПЕРЕБОР ВЛОЖЕННЫХ СПИСКОВ 
# users = [
#     ["Tom", 29],
#     ["Alice", 33],
#     ["Bob", 27]
# ]
# for user in users:
#     for item in user:
#         print(item, end=" | ")




 МЕТОДЫ СПИСКА
#     append(item): добавляет элемент item в конец списка
 
#     insert(index, item): добавляет элемент item в список по индексу index
 
#     remove(item): удаляет элемент item. Удаляется только первое вхождение элемента. Если элемент не найден, генерирует исключение ValueError
 
#     clear(): удаление всех элементов из списка
 
#     index(item): возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError
 
#     pop([index]): удаляет и возвращает элемент по индексу index. Если индекс не передан, то просто удаляет последний элемент.
 
#     count(item): возвращает количество вхождений элемента item в список
 
#     sort([key]): сортирует элементы. По умолчанию сортирует по возрастанию. Но с помощью параметра key мы можем передать функцию сортировки.
 
#     reverse(): расставляет все элементы в списке в обратном порядке
 
#     len(list): возвращает длину списка
 
#     sorted(list, [key]): возвращает отсортированный список
 
#     min(list): возвращает наименьший элемент списка
 
#     max(list): возвращает наибольший элемент списка

#lambda () Эта функция может иметь любое количество аргументов, но только одно выражение, которое вычисляется и возвращается.

#map () возвращает список результатов после применения данной функции к каждому элементу данной итерации
 
# reduce () применяет конкретную функцию, переданную в ее аргументе, ко всем элементам списка, сохраняет промежуточный результат и возвращает только окончательное значение суммирования

# sum () Суммирует числа в списке

# ord () Возвращает целое число, представляющее кодовую точку Unicode данного символа Unicode

# cmp () Эта функция возвращает 1, если первый список «больше» второго списка

# all () Возвращает истину, если все элементы верны или список пуст

# any () вернет истину, если любой элемент списка верен. если список пуст, вернуть false

# enumerate () Возвращает перечислить объект списка

# accumulate () применить конкретную функцию, переданную в ее аргументе, ко всем элементам списка, возвращает список, содержащий промежуточные результаты

# filter () проверяет, является ли каждый элемент списка истинным или нет
 
 
