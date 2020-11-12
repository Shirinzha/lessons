# def shout(word='да'):
#   return word.capitalize()+'!'

# print(shout())
# # # # выведет: 'Да!'

# scream = shout

# print(scream())
# # # # выведет: 'Да!'

# del shout
# print(scream())
# # # выведет: 'Да!'









# def talk():
#     def whisper(word="ДА"):
#         return word.lower()+"...";

#     print(whisper())

# talk()
# # # # выведет: "да..."








# def getTalk(type="shout"):
#    # Мы определяем функции прямо здесь
#    def shout(word="да"):
#        return word.capitalize()+"!"
#    def whisper(word="ДА") :
#        return word.lower()+"...";
#    # Затем возвращаем необходимую
#    if type == "shout":
#        return shout
#    else:
#        return whisper
# talk = getTalk()
# print(talk())
# print(getTalk("whisper")())
# # # выведет: да...


# def doSomethingBefore(func):
#     print("Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал")
#     print(func())
# doSomethingBefore(scream)

# # #выведет:
# # # Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал
# # # Да!










def bread(func):
   def wrapper():
       print("</------\>")
       func()
       print("<\______/>")
   return wrapper
def ingredients(func):
   def wrapper():
       print("#помидоры#")
       func()
       print(" ~салат~")
   return wrapper
def sandwich(food=" --мясо--"):
   print(food)
# # #выведет: --ветчина--
sandwich = bread(ingredients(sandwich))
sandwich()


# @bread
# @ingredients
# def sandwich(food="--Котлета--"):
#   print(food)
# sandwich()

