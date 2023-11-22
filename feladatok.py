elso,masodik,harmadik,legkisebb,szovegKiir = 0,0,0,0,""

kisebb = 0

elso = int(input("Kérem az első számot: "))
masodik = int(input("Kérem a második számot: "))
harmadik = int(input("Kérem a harmadik számot: "))

if elso <= masodik:
    kisebb = elso
else:
    kisebb = masodik

if kisebb <= harmadik:
    legkisebb = kisebb
else:
    legkisebb = harmadik

szovegKiir = f"A legkisebb szám: {legkisebb}"
print(szovegKiir)