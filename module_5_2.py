class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.nunmer_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 < new_floor <= self.nunmer_of_floors:
            for i in range(1, new_floor + 1):
                print(i, "из", self.nunmer_of_floors, self.name)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.nunmer_of_floors

    def __str__(self):
        return f'Название {self.name}, количество этажей:  {self.nunmer_of_floors}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))