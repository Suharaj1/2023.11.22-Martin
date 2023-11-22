elso, masodik, osszeg, kulonbseg, szorzat,hanyados, szovegKiir = 0,0,0,0,0,0,0.0,""

elso = int(input("Kérem az első számot: "))
masodik = int(input("Kérem az második számot: "))

osszeg = elso + masodik
kulonbseg = elso - masodik
szorzat = elso * masodik
hanyados = elso / masodik

szovegKiir = f"A számok: {elso}, {masodik}"
szovegKiir = f"Összege: {osszeg}"
szovegKiir = f"Különbsége: {kulonbseg}"
szovegKiir = f"szorzata: {szorzat}"
szovegKiir = f"Hányadosa: {hanyados}"