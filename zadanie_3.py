
koszyk = [
    {'produkt': 'mleko', 'ilosc': 1, 'cena': 1.5},
    {'produkt': 'czekolada', 'ilosc': 2, 'cena': 3},
    {'produkt': 'konserwa', 'ilosc': 4, 'cena': 3.5}
]

suma = 0
for poz in koszyk:
    il = poz['ilosc']
    c = poz ['cena']
    suma = suma + (c * il)
    #print(c)
    #print(suma)
    #print(poz)
print(suma)
