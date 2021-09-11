def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x ** 0.5)):
        if x % i == 0:
            return False
    return True


def next_prime(x):
    while True:
        x += 1
        if is_prime(x) == True:
            return x


def prime_factors(n):
    prime = 2
    all_primes = []
    sorted_primes = []
    final_string = ''
    while n != 1:
        if n % prime == 0:
            all_primes.append(prime)
            n /= prime
        else:
            prime = next_prime(prime)
    set_primes = sorted(list(set(all_primes)))
    for i in set_primes:
        if all_primes.count(i) == 1:
            final_string += "(" + str(i) + ")"
        else:
            final_string += "(" + str(i) + "**" + str(all_primes.count(i)) + ")"
    return final_string


print(prime_factors(7775460))
