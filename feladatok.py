
elso, masodik, nagyobbik, szovegKiir= 0,0,0,""

elso = int(input("Kérem az első számot:"))
masodik = int(input("Kérem a második számot:"))

if elso <= masodik:
    nagyobbik = masodik
else:
    nagyobbik = elso

    szovegKiir= f"A nagyobb szám: {nagyobbik}"
    print(szovegKiir)