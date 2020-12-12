# haslo, zmienia oprocz 1 i ostatniej litery w *
haslo = "password"
ukryte = "*"
dlugosc_srodka = len(haslo) - 2

srodek = '*' * dlugosc_srodka

print(haslo[0] + srodek + haslo[-1])
