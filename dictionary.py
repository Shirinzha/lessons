ДОСТАЕМ ЗНАЧЕНИЕ ПО КЛЮЧУ
# users = {1: "Tom", 2: "Bob", 3: "Bill"}
# elements = {"Au": "Золото", "Fe": "Железо", "H": "Водород", "O": "Кислород"}
# print(elements['H'])


ПРЕБРАЗОВАНИЕ В СЛОВАРЬ
# objects = {}
# print(type(objects))
# objects = dict()
# print(type(objects))



СЛОВАРЬ С КЛЮЧОМ INTEGER
# Dict = {1: 'Makers', 2: 'For', 3: 'Makers'}

СЛОВАРЬ СО СМЕШЕННЫМИ КЛЮЧАМИ
# Dict = {'Name': 'Makers', 1: [1, 2, 3, 4]}

 
Creating a Dictionary with dict() method
# Dict = dict({1: 'Makers', 2: 'For', 3:'Makers'})


 
ИЗ СПИСКОВ МОЖНО ПРЕОБРАЗОВАТЬ СЛОВАРЬ ЕСЛИ В НЕМ ЕСТЬ ПАРА, Т.Е КЛЮЧ И ЗНАЧЕНИЕ
первый вариант
# Dict = dict([(1, 'Makers'), (2, 'For')])
второй вариант
# users_list = [
#     ["+111123455", "Tom"],
#     ["+384767557", "Bob"],
#     ["+958758767", "Alice"]
# ]
# users_dict = dict(users_list)
# print(users_dict)




 
ДОБАВЛЕНИЕ ЭЛЕМЕНТОВ В Dict  
# Dict = {}
# print("Empty Dictionary: ")
# print(Dict)
# Dict[0] = 'Makers'
# Dict[2] = 'For'
# Dict['3'] = 1
# Dict[0] = 'ithub'
# print(Dict)




 ИЗМЕНЕНИЕ ЗНАЧЕНИЯ ПО КЛЮЧУ
# users = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice" }
# users["+33333333"] = "Bob Smith"
# print(users["+33333333"]) # Bob Smith


УДАЛЕНИЕ ЗНАЧЕНИЯ ПО КЛЮЧУ МЕТОДОМ DEL()
# users = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
# del users["+55555555"]
# print(users)
ОЧИСТКА
# users.clear()
# print(users)



КОПИРУЕТ И ВСТАВЛЯЕТ В НОВУЮ ПЕРЕМЕННУЮ
# users = {"+1111111": "Tom","+3333333": "Bob","+5555555": "Alice"}
# users2 = users.copy()
# users['+1111111'] = 'Hello world'
 
# print(users)
# print(users2)



Метод update() объединяет два словаря:
 # users = {"+1111111": "Tom","+3333333": "Bob","+5555555": "Alice"}
# users2 = {"+2222222": "Sam","+6666666": "Kate"}
# users.update(users2)
# print(users)    # {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice", "+2222222": "Sam", "+6666666": "Kate"}
# print(users2)   # {"+2222222": "Sam", "+6666666": "Kate"}



Перебор словаря 
# users = {
#     "+11111111": "Tom",
#     "+33333333": "Bob",
#     "+55555555": "Alice"
# }
 
# for key in users:
#     print(key, " - ", users[key])


ПЕРЕБОР КЛЮЧЕЙ С ПОМОЩЬЮ МОТОДА KEYS()
# for key in users.keys():


ПЕРЕБОР ЗНАЧЕНИЙ ПО МЕТОДА VALUES()
# for value in users.values():



 КОМПЛЕКСНЫЕ СЛОВАРИ (ПЕРЕБОР КЛЮЧЕЙ И ЗНАЧЕНИЙ)
# users = {
#     "Tom": {
#         "phone": "+971478745",
#         "email": "tom12@gmail.com"
#     },
#     "Bob": {
#         "phone": "+876390444",
#         "email": "bob@gmail.com",
#         "skype": "bob123"
#     }
# }
 
 
# for key, value in users.items():
#   print(value['phone'])





# copy()      They copy() method returns a shallow copy of the dictionary.
# clear()   The clear() method removes all items from the dictionary.
# pop()       Removes and returns an element from a dictionary having the given key.
# popitem()   Removes the arbitrary key-value pair from the dictionary and returns it as tuple.
# get()       It is a conventional method to access a value for a key.
# dictionary_name.values()  returns a list of all the values available in a given dictionary.
# str()       Produces a printable string representation of a dictionary.
# update()  Adds dictionary dict2’s key-values pairs to dict
# setdefault()Set dict[key]=default if key is not already in dict
# keys()      Returns list of dictionary dict’s keys
# items()   Returns a list of dict’s (key, value) tuple pairs
# has_key()   Returns true if key in dictionary dict, false otherwise
# fromkeys()  Create a new dictionary with keys from seq and values set to value.
# type()      Returns the type of the passed variable.
# cmp()       Compares elements of both dict.
