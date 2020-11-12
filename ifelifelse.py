В программировании False обычно приравнивают к нулю, а True – к единице.
 Чтобы в этом убедиться, можно преобразовать булево значение к целочисленному типу:
# print(int(True))
# print(int(False))




 Возможно и обратное. Можно преобразовать какое-либо значение к булевому типу:
# print(bool(3.4))
# print(bool(-150))
# print(bool(0))
# print(bool('qwe'))
# print(bool(''))



Логические операторы  
 # a = 10
# b = 5
 
# print(a + b > 14) #True
# print(a < 14 - b) # False
# print(a <= b + 5) # True
# print(a != b) # True
# print(a == b) # False 
# c = a == b
# print(a, b, c) # (10, 5, False)




Сложные логические выражения  
OR AND NOT    
 
# x = 8
# y = 13
# print('AND: ', y < 15 and x > 8)
# print('OR: ',  y < 15 or x > 8)
# print('NOT: ', not 13 < 15)




 
СРАВНИВАННИЕ СТРОК 
 
# nurbek = "urbek"
# Nurbek = "urbek"
# # this_is_also_nurbek = "nurbek"
# print('Nurbek == nurbek', Nurbek==nurbek)
# print('nurbek==this_is_also_nurbek', nurbek==this_is_also_nurbek)
 
# print(nurbek>nurbek)
# print(Nurbek>nurbek)
 
# # … потому что порядковый номер в USCII “n” равен 110, порядковый номер “N” равен 78:
# print(ord('N'))
# print(ord('n'))







 
# grade = input("Enter grade: ")
# if grade == "5":
#     print("Молодец, так держать!")
# else:
#     print("Ну! Ты можешь лучше учиться, я в этом уверен!")






# grade = input("Enter grade: ")
# if grade == "5":
#     print("Молодец, так держать!")
# elif grade == "4":
#     print("Аххх! Еще чуть-чуть и ты отличник!")
# elif grade == "3":
#     print("Старайся учиться еще лучше!")
# elif grade == "2":
#     print("Та наверно учишься где то в Антарктиде!")
# elif grade == '1':
#     print('Очень плохо')
# else:
#     print("Такой оценки не существует")








 
# is_user_facebook_user = True
# is_user_github_user = True
# is_user_age_greater_18 = True
# user_account_money = 1000
 
 
# if (is_user_facebook_user and is_user_github_user) and (is_user_age_greater_18 and user_account_money > 10000):
#     print("You can enter the system")
# else:
#     print("Sorry, you should have Facebook and Github accounts")









 
# user_is_logged_in = True
# user_has_facebook_account = True
# user_has_github_account = True
 
# if user_is_logged_in:
#     print("Logged in")
 
# if user_has_facebook_account:
#     print("Has FB account")
 
# if user_has_github_account:
#     print("Has Github account")








# user_is_logged_in = True
# user_has_facebook_account = False
# user_has_github_account = True
 
# if user_is_logged_in:
#     print("Logged in")
# elif user_has_facebook_account:
#     print("Has FB account")
# elif user_has_github_account:
#     print("Has Github account")
# else:
#     print("Not logged in and has no accounts")








 
# shopping_total = 100
# # country = "US"
# country = "AU"
# if country == "US":
#     if shopping_total <= 50:
#         print("Shipping Cost is  $50")
#     elif shopping_total <= 100:
#         print("Shipping Cost is $25")
#     elif shopping_total <= 150:
#       print("Shipping Costs $5")
#     else:
#         print("FREE")
 
# if country == "AU":
#     if shopping_total <= 50:
#         print("Shipping Cost is  $100")
#     else:
#         print("FREE")    









