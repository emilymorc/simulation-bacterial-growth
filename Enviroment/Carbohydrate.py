def carbohydrate_adjust(numero):
    if 0 <= numero <= 0.3:
        return -0.2
    elif 0.31 <= numero <= 0.49:
        return -0.18
    elif numero == 0.5:
        return 0
    elif 0.51 <= numero <= 0.7:
        return 0.2
    elif 0.71 <= numero <= 1:
        return 0.3
    else:
        return 0