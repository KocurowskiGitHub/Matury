def zad1():
    globals()["licznik_wywolan"] = 0
    def przestaw(n):
        globals()["licznik_wywolan"] += 1
        r = n % 100
        a = r // 10
        b = r % 10
        n //= 100
        if n > 0:
            w = a + 10 * b + 100 * przestaw(n)
        else:
            if a > 0:
                w = a + 10 * b
            else:
                w = b
        return w
    print(przestaw(316498))
    print(globals()["licznik_wywolan"])
    print()
    globals()["licznik_wywolan"] = 0
    print(przestaw(43657688))
    print(globals()["licznik_wywolan"])
    print()
    globals()["licznik_wywolan"] = 0
    print(przestaw(154005710))
    print(globals()["licznik_wywolan"])
    print()
    globals()["licznik_wywolan"] = 0
    print(przestaw(998877665544321))
    print(globals()["licznik_wywolan"])
    print()

def zad2():
    def pobierzDane():
        with open("symbole.txt","r") as plik:
            return [line.strip() for line in plik.readlines()]
    def zapiszOdp(lines):
        with open("wyniki2.txt", "w") as plik:
            plik.writelines(lines)
    def dopiszOdp(lines):
        with open("wyniki2.txt", "a") as plik:
            plik.writelines(lines)
    def zad2_1():
        lines = pobierzDane()
        odp = ["Zad 2.1\n"]
        for line in lines:
            if line == line[::-1]:
                odp.append(f'{line}\n')
        zapiszOdp(odp)
    def zad2_2():
        lines = pobierzDane()
        odp = ["Zad 2.2\n"]
        iloscKwadratow = 0
        for pionowo in range(1,len(lines)-1):
            for poziomo in range(1,len(lines[pionowo])-1):
                a1 = lines[pionowo-1][poziomo-1]
                a2 = lines[pionowo-1][poziomo]
                a3 = lines[pionowo-1][poziomo+1]
                b1 = lines[pionowo][poziomo-1]
                b2 = lines[pionowo][poziomo]
                b3 = lines[pionowo][poziomo+1]
                c1 = lines[pionowo+1][poziomo-1]
                c2 = lines[pionowo+1][poziomo]
                c3 = lines[pionowo+1][poziomo+1]
                if a1 == a2 == a3 == b1 == b2 == b3 == c1 == c2 == c3:
                    odp.append(f'{pionowo+1} {poziomo+1}\n')
                    iloscKwadratow += 1
        odp.insert(1,f'{iloscKwadratow}\n')
        dopiszOdp(odp)
    def zad2_3():
        lines = pobierzDane()
        maksLiczba = 0
        napisOdp = ""
        odp = ["Zad 2.3\n"]
        cyfra = {
            "o": 0,
            "+": 1,
            "*": 2
        }
        for line in lines:
            liczba = 0
            for i in range(0,len(line)):
                liczba += cyfra[line[i]] * 3 ** (len(line)-1-i)
            if liczba > maksLiczba:
                maksLiczba = liczba
                napisOdp = line
        odp.append(f'{maksLiczba} {napisOdp}\n')
        dopiszOdp(odp)
    def zad2_4():
        lines = pobierzDane()
        sumaLiczb = 0
        napisOdp = ""
        odp = ["Zad 2.4\n"]
        cyfra = {
            "o": 0,
            "+": 1,
            "*": 2
        }
        znak = ["o","+","*"]
        for line in lines:
            liczba = 0
            for i in range(0, len(line)):
                liczba += cyfra[line[i]] * 3 ** (len(line) - 1 - i)
            sumaLiczb += liczba
        odp.append(f'{sumaLiczb} ')
        i = 0
        while True:
            i += 1
            if 3**i > sumaLiczb:
                break
        i -= 1
        while sumaLiczb > 0:
            ileZmiesciSiePotegi = 0
            liczba = 3**i
            while liczba <= sumaLiczb:
                ileZmiesciSiePotegi += 1
                liczba *= ileZmiesciSiePotegi + 1
            napisOdp += znak[ileZmiesciSiePotegi]
            if ileZmiesciSiePotegi > 0:
                sumaLiczb -= 3**i * ileZmiesciSiePotegi
            i -= 1
        odp.append(f'{napisOdp}\n')
        dopiszOdp(odp)

    zad2_1()
    zad2_2()
    zad2_3()
    zad2_4()

def zad3():
    def pobierzDane():
        with open("dron.txt","r") as plik:
            return [line.strip() for line in plik.readlines()]
    def zapiszOdp(lines):
        with open("wyniki3.txt", "w") as plik:
            plik.writelines(lines)
    def dopiszOdp(lines):
        with open("wyniki3.txt", "a") as plik:
            plik.writelines(lines)
    def NWD(A,B):
        dzielnikiA = []
        dzielnikiB = []
        dzielnik = 2
        while A > 1:
            if A % dzielnik == 0:
                dzielnikiA.append(dzielnik)
                A /= dzielnik
                continue
            dzielnik += 1
        dzielnik = 2
        while B > 1:
            if B % dzielnik == 0:
                dzielnikiB.append(dzielnik)
                B /= dzielnik
                continue
            dzielnik += 1
        nwd = 1
        if len(dzielnikiA) > len(dzielnikiB):
            for i in range(len(dzielnikiB)):
                if dzielnikiA.__contains__(dzielnikiB[i]):
                    dzielnikiA.remove(dzielnikiB[i])
                    nwd *= dzielnikiB[i]
        else:
            for i in range(len(dzielnikiA)):
                if dzielnikiB.__contains__(dzielnikiA[i]):
                    dzielnikiB.remove(dzielnikiA[i])
                    nwd *= dzielnikiA[i]
        return nwd


    def zad3_1():
        lines = pobierzDane()
        odp = ["Zad 3.1\n"]
        licznik = 0
        for line in lines:
            liczby = line.split(" ")
            A = abs(int(liczby[0]))
            B = abs(int(liczby[1]))
            if A == 0:
                wynik = B
            elif B == 0:
                wynik = A
            else:
                wynik = NWD(A,B)
            if wynik > 1:
                licznik += 1
        odp.append(f'{licznik}\n')
        zapiszOdp(odp)
    def zad3_2():
        lines = pobierzDane()
        odp = ["Zad 3.2\n"]
        A = 0
        B = 0
        punkty = []
        licznik = 0
        for line in lines:
            liczby = line.split(" ")
            A += int(liczby[0])
            B += int(liczby[1])
            punkty.append((A,B))
            if A in range(1,5000) and B in range(1,5000):
                licznik += 1
        odp.append(f'{licznik}\n')
        for i in range(len(punkty)):
            punkt1 = punkty[i]
            for j in range(i+1,len(punkty)-1):
                punkt2 = punkty[j]
                for k in range(i+1,len(punkty)-1):
                    punkt3 = punkty[k]
                    sredniaX = abs(punkt2[0]+punkt1[0])/2
                    sredniaY = abs(punkt2[1]+punkt1[1])/2
                    if punkt3[0] == sredniaX and punkt3[1] == sredniaY:
                        odp.append(f'{punkt1},{punkt3},{punkt2}')
        dopiszOdp(odp)

    zad3_1()
    zad3_2()


zad1()
#zad2()
#zad3()