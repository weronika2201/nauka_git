
vat = 0.23
cena = float(input())
def calculate_vat(netto):
    wart_vat = cena * vat
    netto = cena - wart_vat
    return(netto)

if __name__ == "__main__":
    vat = calculate_vat(1000)
    print("{0}".format(vat))


# drugi sposob
def calucate_vat(netto):
    return (netto * 23)/100

if __name__ == "__main__":
    vat = calucate_vat(777)
    print("{​​​​0}​​​​".format(vat))
