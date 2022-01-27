print("Introdueix una paraula qualsevol: ")
paraula = input()

j = len(paraula) -1

capicua = True

for i in paraula:
    if i != paraula[j]:
        capicua = False
    j -= 1
if capicua:
    print("Es capicua")
else:
    print("No es capicua")