Перебор кортежей
 
Для перебора кортежа можно использовать стандартные циклы for и while. С помощью цикла for
 # user = ("Tom", 22, False)
# for item in user:
#     print(item)
 
 
С помощью цикла while:
 # user = ("Tom", 22, False)
# i = 0
# while i < len(user):
#     print(user[i])
#     i += 1


проверяем на наличие элемента
# user = ("Tom", 22, False)
# name = "Tom"
# if name in user:
#     print("Пользователя зовут Tom")
# else:
#     print("Пользователь имеет другое имя")



Сложные кортежи
 
Один кортеж может содержать другие кортежи в виде элементов. Например:

# countries = (
#     ("Germany", 80.2, (("Berlin",3.326), ("Hamburg", 1.718))),
#     ("France", 66, (("Paris", 2.2),("Marsel", 1.6)))
# )
# for country in countries:
#     countryName, countryPopulation, cities = country
#     print("\nCountry: {}  population: {}".format(countryName, countryPopulation))
#     for city in cities:
#         cityName, cityPopulation = city
#         print("City: {}  population: {}".format(cityName, cityPopulation))




Deleting a Tuple
 # tuple1 = (0, 1, 2, 3, 4)
# del tuple1
 # print(tuple1)





# all()     Returns true if all element are true or if tuple is empty

# any()       return true if any element of the tuple is true. if tuple is empty,              return false

# len()       Returns length of the tuple or size of the tuple

# enumerate() Returns enumerate object of tuple

# max()       return maximum element of given tuple

# min()       return minimum element of given tuple

# sum()       Sums up the numbers in the tuple

# sorted()  input elements in the tuple and return a new sorted list

# tuple()   Convert an iterable to a tuple.
 
 










