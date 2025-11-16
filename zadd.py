def wyswielt_co_drugi(lista):
    for i in range(0, len(lista), 2):
        print(lista[i])

liczby = list(range(10))
wyswielt_co_drugi(liczby)