#1
immutable_var = 1, 2, 'Hi'
print(immutable_var)
#2
#immutable_var[0] = 3 # кортеж не ищзменяемый тип данных. Изменять элементы в кортеже  можно только, если сам элемент является списком
#Например
immutable_var_1 = ([5,7], 'Hello', 3, 5)
immutable_var_1[0][0] = 2
print(immutable_var_1)

#3
mutable_list = [1999, 12, True, 'Hawaii']
mutable_list[1] = 6171
mutable_list[3] = 'Madrid'
print((mutable_list))

