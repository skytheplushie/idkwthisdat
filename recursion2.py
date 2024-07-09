def get_multiplied_digits(numbers):
    str_number = str(numbers)
    first = int(str_number[0:])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[0:]))
    else:
        return first


result = get_multiplied_digits(40203)
result1 = get_multiplied_digits(203) * 4
result2 = get_multiplied_digits(3) * 4 * 2
print(result)