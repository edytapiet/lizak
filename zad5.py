def sprawdz(lista, liczba):
    for element in lista:
        if element == liczba:
            return True
    return False

print(sprawdz([10, 20, 30], 20))
print(sprawdz([10, 20, 30], 5))
