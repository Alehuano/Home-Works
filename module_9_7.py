def is_prime(func):
    def wrapper(one, two, three):
        n = func(one, two, three)
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        if count == 2:
            return ('Простое число')
        else:
            return ('Составное число')
    return wrapper


@is_prime
def sum_three(one, two, three):
    sum = one + two + three
    print(sum)
    return sum


result = sum_three(2, 3, 6)
print(result)
