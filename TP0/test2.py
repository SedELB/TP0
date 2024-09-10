temp = input('Entrez la temperature').strip()
unit = input('Entrez unite C ou F').strip()
temp = float(temp)
unit = str(unit)
if unit == 'C':
    F = (temp * 1.8) + 32
    print(F)
elif unit == 'F':
    C = (temp - 32) * (5/9)
    print(C)
else :
    print('Entree non valide')