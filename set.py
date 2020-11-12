Creating a Set with the use of a String
# set1 = set("ItHub")
# print(set1)


Creating a Set with the use of Constructor (Using object to Store String)
# String = 15
# set1 = set(String)
# print(set1)


Creating a Set with the use of a List
# set1 = set(["ItHub", "Coding", "Is", "ItHub", 'is', 'ithub'])
# print(set1)


Creating a Set with a List of Numbers
 # set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
# print(set1)
# print(type(set1))



Creating a Set with a mixed type of values
# set1 = set([3,0,2,1, 'ItHub', 4, 'Coding', 6, 'Easy', True, False])
# print(set1)



определяем длину списка
# users = {"Tom","Bob","Alice", 'Tom'}
# print(len(users))



добавляем элементы
# users = set()
# users.add("Sam")
# users.add('dastan')
# users.add('Ulan')
# users.add('Feis')
# users.add('Feis')
# print(users)



удаление элемента по значению
# users = {"Tom", "Bob", "Alice"}
# user = "Tom"
# if user in users:
#     users.remove(user)
# # users.remove('Tom')
# print(users)  



 удаление всех элементов
# users.clear()
# print(users)



перебор элементов через цикл
# users = {"Tom","Bob","Alice"}
# for user in users:
#     print(user, end=' ')



 
Метод union() объединяет два множества и возвращает новое множество:
# a = 'Hello' + ', world'
# print(a)
 
# users = {"Tom","Bob","Alice"}
# users2 = {"Sam","Kate", "Bob"}
# users3 = users.union(users2)
# print(users3)   # {"Bob", "Alice", "Sam", "Kate", "Tom"}



intersection() Пересечение множеств позволяет получить только те элементы,
которые есть одновременно в обоих множествах. Метод intersection() производит операцию пересечения множеств и возвращает новое множество
# users = {"Tom","Bob","Alice"}
# users2 = {"Sam","Kate", "Bob"}
# users3 = users.intersection(users2)
# print(users3)   # {"Bob"}


 Вместо метода intersection мы могли бы использовать операцию логического умножения:
# users = {"Tom","Bob","Alice", 'Hello'}
# users2 = {"Sam","Kate", "Bob", 'Hello'}
# print(users & users2)   # {"Bob"}




 
difference() Еще одна операция - разность множеств возвращает те элементы, 
# которые есть в первом множестве, но отсутствуют во втором. Для получения разности множеств можно использовать метод difference или операцию вычитания:
# users = {"Tom","Bob","Alice"}
# users2 = {"Sam","Kate", "Bob"}
# users3 = users.difference(users2)
# print(users3)           # {"Tom", "Alice"}
# print(users - users2)   # {"Tom", "Alice"}



 
Метод issubset позволяет выяснить, является ли текущее множество подмножеством (то есть частью) другого множества:
# users = {"Tom", "Bob", "Alice"}
# superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
# print(users.issubset(superusers))
# print(superusers.issubset(users))



 
Метод issuperset, наоборот, возвращает True, если текущее множество является надмножеством (то есть содержит) для другого множества:
# users = {"Tom", "Bob", "Alice"}
# superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
# print(users.issuperset(superusers))
# print(superusers.issuperset(users))




 FROZEN SET
 
Тип frozen set является видом множеств, которое не может быть изменено. Для его создания используется функция frozenset:
 
# users = frozenset({"Tom", "Bob", "Alice"})
# users.remove("Tom")
# print(users)
 
В функцию frozenset передается набор элементов - список, кортеж, другое множество.
В такое множество мы не можем добавить новые элементы, как и удалить из него уже имеющиеся. Собственно поэтому frozen set поддерживает ограниченный набор операций:
 
#     len(s): возвращает длину множества
 
#     x in s: возвращает True, если элемент x присутствует в множестве s
 
#     x not in s: возвращает True, если элемент x отсутствует в множестве s
 
#     s.issubset(t): возвращает True, если t содержит множество s
 
#     s.issuperset(t): возвращает True, если t содержится в множестве s
 
#     s.union(t)
#     : возвращает объединение множеств s и t
 
#     s.intersection(t): возвращает пересечение множеств s и t
 
#     s.difference(t): возвращает разность множеств s и t
 
#     s.copy(): возвращает копию множества s
 




SET METHODS 
# add()           Adds an element to a set
 
# remove()      Removes an element from a set. If the element is not present in the set, raise a KeyError
 
# clear()       Removes all elements form a set
 
# copy()          Returns a shallow copy of a set
 
# pop()           Removes and returns an arbitary set element. Raise KeyError if the set is empty
 
# update()      Updates a set with the union of itself and others
 
# union()       Returns the union of sets in a new set
 
# difference()    Returns the difference of two or more sets as a new set
 
# difference_update()   Removes all elements of another set from this set
 


























