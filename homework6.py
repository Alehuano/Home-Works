#Словари
my_dict={"Илья":1974, "Сергей":1973,"Рустам":1982, "Олег":1998}
print(my_dict)
print(my_dict.get('Сергей'))
print(my_dict.get('Саша'))
my_dict.update({'Оля':2003,
               'Лена':2006})
s=my_dict.pop("Олег")
print(s)
print(my_dict)

#Множества
my_set={1,3,2,7,6,3,2,3,4,1,7,8,5,4}
print(my_set)
my_set.add("Игра")
my_set.add(False)
my_set.discard(4)
print(my_set)