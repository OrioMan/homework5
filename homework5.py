#Задайте переменные разных типов данных:
immutable_var = 1, 2, 3, 25,
print(immutable_var)
#Изменение значений переменных:
immutable_var = ([1, 2], 3, 25)
print(type(immutable_var))
immutable_var[0][0] = 2
print(immutable_var)
#Создание изменяемых структур данных:
mutable_list = [1, 2, 3, 25]
mutable_list[0] = "труп"
print(mutable_list)