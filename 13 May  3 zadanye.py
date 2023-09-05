spisok = list(map(int, input("Throw some numbers ").split()))
def check(chislo, spisok):
    if chislo in spisok:
        return True
    else:
        return False
chislo = int(input("Vvedy chislo "))
print(check(chislo, spisok))

#alternate solution but long and inefficient
#spisok = list(map(int, input("Throw some numbers: ").split()))
#def check(chislo, spisok):
#    for i in spisok:
#        if i == chislo:
#            return True
#    return False
#
#chislo = int(input("Vvedy chislo: "))
#print(check(chislo, spisok))





