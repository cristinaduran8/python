"""
CRISTINA DURÀN 
EXERCICI:
Una aplicació de seguretat controlaMaquina reb  una llistes de valors que indiquen les temperatures d’una màquina. 
A cada rebuda de dades l’aplicació ha de imprimir el valor màxim i el mínim. També ha d’imprimir el nombre de vegades que ha superat el valor 3 (sols una vegada superat i desprès baixa i el torna superar, són dos pics).
Exemples de valors:
Entrada de valors: [1,2,4,4,5,6,7,1,2,5]
Sortida de valors: “màxim: 7, mínim: 1, variat: 2
Entrada de valors: [1,4,1,4,1,4]
Sortida de valors: “màxim: 4, mínim: 1, variat: 3

"""

a = [6, 34, 1, 22, 13, 23, 56, 2, 4, 39, 9, 21]

print("Aquest és el recomte de la temperatura")
print(a)

max = 0
min = 1000

for i in a:
    if (i > max):
        max = i
    if (i < min):
        min = i

print('Valor màxim:', max)
print('Valor mínim:', min)
