def competence_adjust(numero):
    if 0 <= numero <= 200:
        return -0.5
    elif 201 <= numero <= 400:
        return -0.1
    elif 401 <= numero <= 500:
        return 0
    elif 501 <= numero <= 600:
        return 0.05
    elif 601 <= numero <= 800:
        return 0.2
    elif 801 <= numero <= 1000:
        return 0.3
    else:
        return 0
