def pomnoz_przez_dwa(lista):
    nowa_lista = []
    for liczba in lista:
        nowa_lista.append(liczba * 2)
    return nowa_lista


def pomnoz_przez_dwa_skladana(lista):
    return [x * 2 for x in lista]


liczby = [1, 2, 3, 4, 5]

print(pomnoz_przez_dwa(liczby))
print(pomnoz_przez_dwa_skladana(liczby))