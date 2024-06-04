numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()
is_prime = True
for i in range(1, len(numbers)):
    for j in range(1, i):
        if numbers[i] % numbers[j] == 0:
            is_prime = False
            not_primes.append(numbers[i])
            break
        else:
            is_prime = True
    if is_prime == True:
        primes.append(numbers[i])

print("Primes: ", primes)
print("Not Primes:", not_primes)
