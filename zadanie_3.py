
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



#wersja druga
owady = [
    {'owad': 'biedronka', 'ilosc': 3, 'odnoza': 4},
    {'owad': 'motyl', 'ilosc': 2, 'odnoza': 6},
    {'owad': 'pszczola', 'ilosc': 3, 'odnoza': 4},
]
suma_odnoz = 0
for insekt in owady:
    ilosc_owadow = insekt['ilosc']
    od = insekt['odnoza']
    suma_odnoz = suma_odnoz + (ilosc_owadow * od)
print(suma_odnoz)

# wersja 3

koszyk = [
    {'produkt': 'mleko', 'ilosc': 1, 'cena': 1.5, 'alergeny': 'laktoza'},
    {'produkt': 'czekolada', 'ilosc': 2, 'cena': 3, 'alergeny': 'orzechy'},
    {'produkt': 'woda', 'ilosc': 4, 'cena': 3.5, 'alergeny': 'brak'}
]

for poz in koszyk:
    alerg = poz['alergeny']
    if alerg == 'laktoza':
        print("Uwaga ten produkt zawiera laktoze")
    elif alerg == 'orzechy':
        print("Uwaga ten produkt zawiera orzechy")
    else:
        print("Ten produkt jest ok")
