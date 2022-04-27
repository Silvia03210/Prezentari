stiva_a = []
stiva_b = []
fisier = open("depou.in", "r")
n = fisier.readline()
linie = fisier.readline().strip().split(' ')
for i in range(len(linie)):
    stiva_a.append(int(linie[i]))
fisier.close()

contor = 1
rezultat = []
p = 1
while stiva_a or stiva_b:
    if stiva_b and stiva_b[-1] == contor:
        stiva_b.pop()
        contor += 1
        rezultat.insert(p + 1, 2)
        rezultat.insert(p + 2, 3)
        p += 2
    else:
        while stiva_a and stiva_a[-1] != contor:
            if stiva_b and stiva_a[-1] >= stiva_b[-1]:
                break
            stiva_b.append(stiva_a[-1])
            stiva_a.pop()
            rezultat.insert(p + 1, 1)
            rezultat.insert(p + 2, 2)
            p += 2
        if stiva_a[-1] == contor:
            rezultat.insert(p + 1, 1)
            rezultat.insert(p + 2, 3)
            p += 2
            stiva_a.pop()
            contor += 1
        else:
            break
if contor < int(n):
    scriere_fisier = open("depou.out", "w")
    scriere_fisier.write(0)
    scriere_fisier.close()
else:
    scriere_fisier = open("depou.out", "w")
    scriere_fisier.write(str(int((p - 1) / 2)))
    scriere_fisier.write('\n')
    for i in range(len(rezultat)):
        if rezultat[i] == 1:
            scriere_fisier.write("A ")
        if rezultat[i] == 2:
            scriere_fisier.write("B ")
        if rezultat[i] == 3:
            scriere_fisier.write("C ")
        if i % 2 == 1:
            scriere_fisier.write("\n")
    scriere_fisier.close()