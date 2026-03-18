def primes():
    n = 2
    while True:
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
        if prime:
            yield n
        n += 1
p = primes()
for i in range(15):
    print(next(p))