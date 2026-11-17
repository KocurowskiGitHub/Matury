import math
from matplotlib import pyplot as plt

def pobierz(sciezka):
    with open(sciezka,"r") as plik:
        return [line.strip() for line in plik.readlines()]

def zapisz(sciezka,lines):
    with open(sciezka,"w") as plik:
        plik.writelines(lines)

def dopisz(sciezka,lines):
    with open(sciezka,"a") as plik:
        plik.writelines(lines)

def zad4_1():
    lines = pobierz("punkty.txt")
    ilosc = 0
    listaWspolrzednych = []
    odp = ["Zadanie 4.1:\n"]
    for line in lines:
        ab = line.split(" ")
        x = int(ab[0])
        y = int(ab[1])

        if (x - 200)**2 + (y - 200) ** 2 == 200**2:
            listaWspolrzednych.append((x,y))
        if (x - 200)**2 + (y - 200) ** 2 < 200**2:
            ilosc += 1
    odp.append(f'{listaWspolrzednych}\n')
    odp.append(f'{ilosc}\n')
    zapisz("wyniki_4.txt",odp)

def zad4_2():
    lines = pobierz("punkty.txt")
    iloscWKole = 0
    iloscPrzejrzanychPunktow = 1
    odp = ["Zadanie 4.2:\n"]
    for line in lines:
        ab = line.split(" ")
        x = int(ab[0])
        y = int(ab[1])
        if (x - 200)**2 + (y - 200) ** 2 <= 200**2:
            iloscWKole += 1
        if iloscPrzejrzanychPunktow == 1000:
            odp.append(f'{iloscWKole/250:.5}\n')
        if iloscPrzejrzanychPunktow == 5000:
            odp.append(f'{4*iloscWKole/5000:.5}\n')
        iloscPrzejrzanychPunktow += 1
    odp.append(f'{iloscWKole/2500:.5}\n')
    dopisz("wyniki_4.txt",odp)

def zad4_3():
    lines = pobierz("punkty.txt")
    iloscWKole = 0
    En = []
    odp = ["Zadanie 4.3:\n"]
    for i in range(1700):
        ab = lines[i].split(" ")
        x = int(ab[0])
        y = int(ab[1])
        if (x - 200) ** 2 + (y - 200) ** 2 <= 200 ** 2:
            iloscWKole += 1
        En.append(abs(math.pi-4*iloscWKole/(i+1)))
        if i+1 == 1000 or i + 1 == 1700:
            odp.append(f'{En[i]:.3}\n')
    dopisz("wyniki_4.txt",odp)
    plt.plot(En)
    plt.title('Błąd bezwzględny', fontsize=12)
    plt.xlabel('',fontsize=12)
    plt.ylabel('',fontsize=12)
    plt.show()

def zad6_1():
    lines = pobierz("dane_6_1.txt")
    Odp = ["Zadanie 6.1:\n", "Tekst Jawny\t","Tekst Zaszyfrowany\n"]
    for line in lines:
        Odp.append(line + "\t")
        zaszyfrowany = ""
        for litera in line:
            cyfra = ord(litera)
            klucz = 107
            klucz %= 26
            if cyfra + klucz > 90:
                zaszyfrowany += chr(64+abs(cyfra + klucz - 90))
                continue
            zaszyfrowany += chr(cyfra+klucz)
        Odp.append(zaszyfrowany + "\n")
    zapisz("wyniki_6_1.txt",Odp)

def zad6_2():
    lines = pobierz("dane_6_2.txt")
    Odp = ["Zadanie 6.2:\n", "Tekst Zaszyfrowany\t","Tekst Jawny\n"]
    for line in lines:
        zaszyfrowana = line.split(" ")[0]
        if len(line.split()) > 1:
            klucz = int(line.split(" ")[1])
        else:
            klucz = 0
        klucz %= 26
        Odp.append(zaszyfrowana + "\t")
        odszyfrowany = ""
        for litera in zaszyfrowana:
            cyfra = ord(litera)
            if cyfra - klucz < 65:
                odszyfrowany += chr(91 - abs(cyfra - klucz - 65))
                continue
            odszyfrowany += chr(cyfra - klucz)
        Odp.append(odszyfrowany + "\n")
    zapisz("wyniki_6_2.txt", Odp)

def Zaszyfruj(litera,klucz):
    klucz %= 26
    cyfra = ord(litera)
    if cyfra + klucz > 90:
        return chr(64 + abs(cyfra + klucz - 90))
    else:
        return chr(cyfra + klucz)

def zad6_3():
    lines = pobierz("dane_6_3.txt")
    Odp = ["Zadanie 6.3:\n", "Tekst Jawny\t", "Tekst Blednie Zaszyfrowany\n"]
    for line in lines:
        (jawny,zaszyfrowany) = line.split(" ")
        znaleziony_klucz = 0
        for klucz in range(0, 27):
            if zaszyfrowany[0] == Zaszyfruj(jawny[0], klucz):
                znaleziony_klucz = klucz
                break
        for i in range(1,len(jawny)):
            if Zaszyfruj(jawny[i],znaleziony_klucz) != zaszyfrowany[i]:
                Odp.append(jawny + "\t" + zaszyfrowany + "\n")
                break
    zapisz("wyniki_6_3.txt", Odp)


zad4_1()
zad4_2()
zad4_3()
zad6_1()
zad6_2()
zad6_3()