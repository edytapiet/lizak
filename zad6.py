def polacz_i_przetworz(lista1, lista2):
    polaczone = lista1 + lista2

    nowe = []
    for x in polaczone:
        if x not in nowe:
            nowe.append(x)

    wynik = []
    for x in nowe:
        wynik.append(x ** 3)

    return wynik

lista_a = [1, 2, 3]
lista_b = [2, 4]

wynik = polacz_i_przetworz(lista_a, lista_b)

print(wynik)
