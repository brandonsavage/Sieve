#!/usr/bin/python

def sieve(max):
    primes = [2] #Two is always prime
    nums = range(3, max)
    for x in range(3, max):
        for y in primes:
            if x % y == 0:
                break
        else:
            primes.append(x)                
    return primes

print sieve(100)
