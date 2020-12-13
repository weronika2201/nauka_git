
def str_calculator(a, b, operacja):
    if operacja == 'concat':
        return a + b

    if operacja == 'contains':
        return True

    if operacja == 'endsWith':
       return b.endsWith(a)
