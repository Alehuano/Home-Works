n = int(input("Введите число от 3 до 20... А можно любое: "))
password = list()
result = ""
for i in range(1, n):
    for j in range(1, n):
        sum = i + j + i
        if n % sum == 0:
            password.extend([i, j + i])
for k in password:
    result += str(k)
print(result)