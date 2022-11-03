# ALGO HW 1
# Q2
# Compute max of three values


def compute_max_of_three_values(v1, v2, v3):
    if v1 > v2 and v1 > v3:
        vmax = v1
        print(f'maximum value = {vmax}')
    elif v2 > v1 and v2 > v3:
        vmax = v2
        print(f'maximum value = {vmax}')
    elif v3 > v1 and v3 > v2:
        vmax = v3
        print(f'maximum value = {vmax}')
    else:
        print("More than one max value")
    return vmax

v1 = 0
v2 = 100
v3 = -100
compute_max_of_three_values(v1, v2, v3)

