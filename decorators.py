def is_prime(func):
    def wrapper(*num: int):
        result = func(*num)
        for div in range(2, result):
            if div % 2 == 0:
                print('not prime')
                break
            else:
                print('prime')
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
