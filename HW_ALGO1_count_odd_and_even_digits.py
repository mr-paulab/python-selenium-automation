# ALGO HW 1
# Q3
# Count odd and even digits in a number

def count_odd_even_digits(num):
    even_count = 0
    odd_count = 0
    for x in num:
        x = int(x)
        if x == 0:
            even_count += 1
        elif x % int(2) == 0:
            even_count += 1
        else:
            odd_count += 1
    print(f'even count = {even_count}, odd count = {odd_count}')


num = '203040506070'
count_odd_even_digits(num)
