elso,masodik,harmadik,legnagyobb,szovegKiir = 0,0,0,0,""

nagyobb = 0

elso = int(input("Kérem az első számot: "))
masodik = int(input("Kérem a második számot: "))
harmadik = int(input("Kérem a harmadik számot: "))

if elso <= masodik:
    nagyobb = elso
else:
    nagyobb = masodik

if nagyobb <= harmadik:
    legnagyobb = nagyobb
else:
    legnagyobb = harmadik

szovegKiir = f"A legnagyobb szám: {legnagyobb}"
print(szovegKiir)