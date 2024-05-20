# работа со списками
my_list = ['Кетонал', 'дегсалгин', 'дексакетопрофен', 'анальгин']
print(my_list)
print(my_list[0], my_list[-1])
my_list_1 = my_list[1]
print(my_list_1[3:7])
my_list[3] = 'нош-па'
print(my_list)

# работа со словарями

my_dict = {'790': 'МО', '797': 'Москва', '198': 'Санкт-Петербург', '33': 'Владимир'}
print(my_dict)
print(my_dict['797'])
my_dict['198'] = 'Нижний Новгород'
my_dict['37'] = 'Иваново'
print(my_dict)
