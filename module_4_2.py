def test_function():
    txt2 = "Проверка"

    def inner_function():
        txt = "Я в области видимости функции test_function"
        return txt

    print(inner_function()) #Ничего не выдает
    return txt2


print(inner_function()) #Выдает ошибку
print(test_function()) #Печатает оба принта
