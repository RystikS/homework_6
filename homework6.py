my_dict = {'Москва': '+495', 'Санкт-Петербург': '+7812', 'Уфа': '+7347'} #В качестве значений использовал str, воспрос опыта. С int уже есть примеры
print(my_dict)
print('Введите название города ')
city= input()
print('Код города '+ my_dict[city])
my_dict['Казань']= '+7843'
print(my_dict['Казань'])
my_dict['Новосибирск']='+7383'
my_dict['Владивосток']='+74232'
a = my_dict.pop('Москва')
print('Удаленное значение: '+a)
print(my_dict)

my_set={1,False,2,'True', 4.5,True,False,2}
print(my_set)
print(my_set.add(5))
print(my_set.add('Train'))
print(my_set.remove('True'))
print(my_set)
