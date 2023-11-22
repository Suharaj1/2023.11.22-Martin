#1
szovegKiir = f"Hello World!"
print(szovegKiir)
#2
nev, szovegKiir = "", ""

nev = input("Adja meg a nevét: ")

szovegKiir = f"Hello {nev}!"
print(szovegKiir)
#3
alapSzam, ketszeres, szovegKiir = 0,0,""

alapSzam = int(input("Kérem a számot: "))
ketszeres = 2 * alapSzam
szovegKiir = f"A {alapSzam} kétszerese:{ketszeres}"
print(szovegKiir)
#4
elso, masodik, osszeg, kulonbseg, szorzat,hanyados, szovegKiir = 0,0,0,0,0,0.0,""

elso = int(input("Kérem az első számot: "))
masodik = int(input("Kérem a második számot: "))

osszeg = elso + masodik
kulonbseg = elso - masodik
szorzat = elso * masodik
hanyados = elso / masodik

szovegKiir = f"A számok: {elso}, {masodik}"
szovegKiir += f"\nÖsszege: {osszeg}"
szovegKiir += f"\nKülönbsége: {kulonbseg}"
szovegKiir += f"\nszorzata: {szorzat}"
szovegKiir += f"\nHányadosa: {hanyados:.2f}"

print(szovegKiir)
#5
elso, masodik, nagyobbik, szovegKiir= 0,0,0,""

elso = int(input("Kérem az első számot:"))
masodik = int(input("Kérem a második számot:"))

if elso <= masodik:
    nagyobbik = masodik
else:
    nagyobbik = elso

    szovegKiir= f"A nagyobb szám: {nagyobbik}"
    print(szovegKiir)