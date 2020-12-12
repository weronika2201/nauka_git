def print_dict(d):
    for key in samolot:
        print("{0}:{1}".format(key, d[key]))

if __name__ == "__main__":
    samolot = {'name': 'boeing',
    'przebieg': 10000,
    'type':'pasazerski'}

    print_dict(samolot)


# haslo, zmienia oprocz 1 i ostatniej litery w *
haslo = "password"
ukryte = "*"
dlugosc_srodka = len(haslo) - 2

srodek = '*' * dlugosc_srodka

print(haslo[0] + srodek + haslo[-1])
