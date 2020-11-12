функция с параметрами:
# def say_hello(name, age):
#     print("Привет,", ', Тому ', 'лет')
# say_hello("Tom", 22) # Том, Bob, Alice- это аргумент
# say_hello("Bob", 32)
# say_hello("Alice", 12)
# say_hello()




код с помощью условий
# figure = input("1-прямоугольник, 2-треугольник, 3-круг: ")
# if figure == '1':
#   width = float(input("Ширина: "))
#   hight = float(input("Высота: "))
#   print("Площадь: %.2f" % (width*hight))
# elif figure == '2':
#   length = float(input("Основание: "))
#   hight = float(input("Высота: "))
#   print("Площадь: %.2f" % (0.5 * length * hight))
# elif figure == '3':
#   radius = float(input("Радиус: "))
#   print(f"Площадь: {3.14 * radius**2}")
# else:
#   print("Ошибка ввода")

И пропишем логику с помощью функции
# def rectangle():
#     width = float(input("Ширина: "))
#     hight = float(input("Высота: "))
#     print("Площадь: %.2f" % (width*hight))
# def triangle():
#     length = float(input("Основание: "))
#     hight = float(input("Высота: "))
#     print("Площадь: %.2f" % (0.5 * length * hight))
# def circle():
#     radius = float(input("Радиус: "))
#     print("Площадь: %.2f" % (3.14 * radius**2))
# figure = input("1-прямоугольник, 2-треугольник, 3-круг: ")
# if figure == '1':
#   rectangle()
# elif figure == '2':
#   triangle()
# elif figure == '3':
#   circle()
# else:
#   print("Ошибка ввода")







Значения по умолчанию
Некоторые параметры функции мы можем сделать необязательными, указав для них значения по умолчанию при определении функции. 
Например:
# def say_hello(name="Tom"):
#     print("Hello,", name)
   
# say_hello()
# say_hello("Bob")






Именованные параметры  
# def display_info(name, age):
#     print("Name:", name, "\t", "Age:", age)
   
# display_info("Tom", 22)




# def display_info(name, age):
#     print("Name:", name, "\t", "Age:", age)
   
# display_info(age=22, name="Tom")








Неопределенное количество параметров 
С помощью символа звездочки можно определить неопределенное количество параметров:
# def sum(*args):# unpacking
#     result = 0
#     for n in args:
#         result += n
#     return result
# sumOfNumbers1 = sum(1, 2, 3, 4, 5)      # 15
# sumOfNumbers2 = sum(3, 4, 5, 6)         # 18
# print(sumOfNumbers1)
# print(sumOfNumbers2)







ключ значение
# def myFun(**kwargs): 
#     for key, value in kwargs.items():
#         print (f"{key} == {value}")




# # # Driver code
# myFun(first ='Makers', mid ='Coding', last='Easy')    

# def test_args_kwargs(arg1, arg2, arg3):
#     print("arg1:", arg1)
#     print("arg2:", arg2)
#     print("arg3:", arg3)


# kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
# test_args_kwargs(**kwargs)











Возвращение результата   
Функция может возвращать результат. Для этого в функции используется оператор return,
 после которого указывается возвращаемое значение:
# def exchange(usd_rate, money):
#     result = round(money/usd_rate, 2)
#     return result
# result1 = exchange(60, 30000)
# print(result1)

# result2 = exchange(56, 30000)
# print(result2)

# result3 = exchange(65, 30000)
# print(result3)



# def create_default_user():
#     name = "Tom"
#     age = 33
#     return name, age
# user_name, user_age = create_default_user()
# print("Name:", user_name, "\t Age:", user_age)










Функция main  
В программе может быть определено множество функций. И чтобы всех их упорядочить, 
хорошей практикой считается добавление специальной функции main, в которой потом уже вызываются другие функции:
# def main():
#     say_hello("Tom")
#     usd_rate = 56
#     money = 30000
#     result = exchange(usd_rate, money)
#     print("К выдаче", result, "долларов")

# def say_hello(name):
#     print("Hello,", name)
   
   
# def exchange(usd_rate, money):
#     result = round(money/usd_rate, 2)
#     return result
# # # Вызов функции main
# main()














# ################ ОБЛАСТЬ ВИДИМОСТИ  #############
# '''
# Область видимости или scope определяет контекст переменной, в рамках которого ее можно использовать. В Python есть два типа контекста: глобальный и локальный.

# Глобальный контекст подразумевает, что переменная является глобальной, она определена вне любой из функций и доступна любой функции в программе. Например:
# '''

# name = "Tom"
# def say_hi():
#     print("Hello", name)
# def say_bye():
#     print("Good bye", name)
# say_hi()
# say_bye()

# '''
# Здесь переменная name является глобальной и имеет глобальную область видимости. И обе определенные здесь функции могут свободно ее использовать.

# В отличие от глобальных переменных локальная переменная определяется внутри функции и доступна только из этой функции, то есть имеет локальную область видимости:
# '''

# name='Hello world'

# def say_hi():
#     name = "Sam"
#     surname = "Johnson"
#     print("Hello", name, surname)
# def say_bye():
#     name = "Tom"
#     print("Good bye", name)


# # say_hi()
# say_bye()


# '''
# В данном случае в каждой из двух функций определяется локальная переменная name. И хотя эти переменные называются одинаково, но тем не менее это дву разных переменных, каждая из которых доступна только в рамках своей функции. Также в функции say_hi определена переменная surname, которая также является локальной, поэтому в функции say_bye мы ее использовать не сможем.

# Есть еще один вариант определения переменной, когда локальная переменная скрывают глобальную с тем же именем:
# '''

name = "Tom"
# def say_hi():
#     print("Hello", name)
# def say_bye():
#     name = "Bob"
#     print("Good bye", name)
# say_hi()  # Hello Tom
# say_bye()  # Good bye Bob


# '''
# Здесь определена глобальная переменная name. Однако в функции say_bye определена локальная переменная с тем же именем name. И если функция say_hi использует глобальную переменную, то функция say_bye использует локальную переменную, которая скрывает глобальную.

# Если же мы хотим изменить в локальной функции глобальную переменную, а не определить локальную, то необходимо использовать ключевое слово global:
# '''

# def say_bye():
#     global name
#     print(name)
#     name = "Bob"
#     return name


# print(say_bye())
# print(name)
# say_bye()
# print(name)

# '''
# В Python, как и во многих других языках программирования, не рекомендуется использовать глобальные переменные. Единственной допустимой практикой является определение небольшого числа глобальных констант, которые не изменяются в процессе работы программы.
# '''

# PI = 3.14

# # # вычисление площади круга
# def get_circle_square(radius):
#     print("Площадь круга с радиусом", radius, "равна", PI * radius * radius)
# get_circle_square(50)

# '''
# В данном случае число 3.14 представлено константой PI. Понятно, что это значение в принципе не изменится, поэтому его можно вынести из функций и определить в виде константы. Как правило, имя константы определяется заглавными буквами.
# '''


# ###### Анонимная функция   ######

# '''
# Оператор lambda это анонимная, или несвязанная функция, при этом довольно ограниченная. Давайте взглянем на несколько базовых примеров, и взглянем, можем ли мы найти применение данной функции. Обычно в таких примерах показывают унылые операции с дублированием. Чтобы сделать обучение интереснее, в нашем примере мы рассмотрим, как найти квадратный корень. Для начала, мы покажем обычную функцию, потом аналогичный с лямбдой-функцией:
# '''


# def sqroot(x):
#     """
#     Находим квадратный корень.
#     """
#     return x ** 2
# square_rt = lambda x: x ** 2

# print(sqroot(2))
# print(square_rt(2))

# Python code to illustrate cube of a number using labmda function 
  

# cube = lambda x, y: x+y
# print(cube(7, 3)) 














