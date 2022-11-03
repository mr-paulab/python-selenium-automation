# ALGO HW 1
# Q1
# Compute sum of digits from 1 to n


def compute_sum_of_digits(n):
    sum_of_digits = 0
    for x in range(1, n + 1):
        sum_of_digits += x
        print(f'n = {x}, sum of digits = {sum_of_digits}')


n = 6
compute_sum_of_digits(n)
