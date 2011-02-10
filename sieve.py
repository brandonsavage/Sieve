def sieve(max):
    primes = [2] #Two is always prime
    for x in range(3, max):
        for y in primes:
            if not x % y:
                break
        else:
            primes.append(x)                
    return primes
