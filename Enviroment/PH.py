def ph_adjust(numero):
    if numero in [1, 2]:
        return 0.3
    elif numero in [3, 4]:
        return 0.12
    elif numero in [5, 6]:
        return -0.3
    elif numero in [7, 8]:
        return -0.25
    elif numero == 9:
        return 0.07
    else:
        return 0
