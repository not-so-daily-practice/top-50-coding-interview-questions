# How do you find the missing number in a given integer array of 1 to 100?

def missing_number_sum(a, n):
    """
    Find a single missing number in array of integers that has a range from 1-n
    :param a: array of integers
    :param n: length of array, including +1 for the missing number
    :return: missing number
    """
    sum_of_series = int(n * (n + 1) / 2)
    for i in a:
        sum_of_series -= i

    return sum_of_series


def missing_number_xor(a, n):
    """
    Find a single missing number in array of integers that has a range from 1-n
    :param a: array of integers
    :param n: lnegth of array, including +1 for the missing number
    :return:
    """
    a_1 = a[0]
    a_2 = 1

    for i in range(1, n - 1):
        a_1 ^= a[i]  # xor over all integers in array

    for i in range(2, n + 1):
        a_2 ^= i  # xor over all numbers that should be present

    return a_1 ^ a_2  # xor returns missing number


a = [1, 2, 3, 4, 6, 7, 8, 9]

print(missing_number_sum(a, 9))
print(missing_number_xor(a, 9))
