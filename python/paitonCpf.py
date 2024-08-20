#paitonkdfi
#cpf

def cpf(cpf):
    y = 0
    if len(cpf) != 14:
        return False
    for x in cpf:
        y += 1
        if y == 4 or y == 8:
            if x == ".":
                continue
            else:
                return False
        elif y == 12:
            if x == "-":
                continue
            else:
                return False
        else:
            if x.isnumeric():
                continue
            else:
                return False
    return True

print(cpf("111.111.111-12"))