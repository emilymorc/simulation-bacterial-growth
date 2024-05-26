def temperature_adjust(numero):
    if 4 <= numero <= 10:
        return -0.4
    elif 11 <= numero <= 17:
        return -0.3
    elif 18 <= numero <= 23:
        return -0.1
    elif 24 <= numero <= 30:
        return 0
    elif 31 <= numero <= 35:
        return 0.1
    elif numero == 36 or numero == 37:
        return 0.25
    elif 38 <= numero <= 45:
        return 0.1
    else:
        return 0

