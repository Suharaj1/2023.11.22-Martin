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
szovegKiir += f"\nHányadosa: {hanyados}"

print(szovegKiir)