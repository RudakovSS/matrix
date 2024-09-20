numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
notPrimes = []
for i in numbers:
    isPrime = True
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime == True:
        primes.append(i)
    else:
        notPrimes.append(i)
print(primes, notPrimes)