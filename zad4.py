def suma_wieksza_lub_rowna(a: int, b: int, c: int) -> bool:
    return (a + b) >= c


wynik = suma_wieksza_lub_rowna(3, 4, 7)  # True, bo 3+4=7 >= 7
print(wynik)
