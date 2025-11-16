def wyswietl_parzyste(lista):
    for liczba in lista:
        if liczba % 2 == 0:
            print(liczba)

liczby = list(range(10))
wyswietl_parzyste(liczby)
