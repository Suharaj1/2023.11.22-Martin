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