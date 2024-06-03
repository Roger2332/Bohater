





punkty = 30
bohater = {}
atributes = [["Health", 0], ["Strenght", 0], ["Agility", 0], ["Inteligence", 0], ["reszta punktow", punkty]]

menu ="""
0 - Zakoncz gre
1 - Pokaz punkty bohatera
2 - Stworz bohatera
3 - Sprzedaj przedmiot
4 - Dokup przedmiot
5 - Pokaz przedmioty
"""
menu1 = None

while menu1 != 0:
    print("\t\nWitaj w Grze Kreator postaci")
    print(menu)
    while True:
        try:
            menu1 = int(input("\nPodaj wartosc: "))
            if type(menu1) is int:
                break
        except ValueError:
            print('podana zla wartosc: ')

    if menu1 == 0:
        print("Do zobaczenia")

    elif menu1 ==1:
        name = input("Podaj imie bohatera: ")
        if name in bohater:
            print(bohater[name][4])
        else:
            print("Nie znalazlem takiego bohatera")

    elif menu1 == 2:
        punkty = 30
        name = input("Podaj imie bohatera: ")
        if name not in bohater:
            print(f"Okej teraz wybierz co twoj bohater ma miec, pamietaj ze masz tylko 30pkt")
            print(f"Dostepne atrybuty: {atributes}")
        while True:
            try:
                sila = int(input(f"\nsila: "))

                if sila <= punkty:
                    punkty -=sila
                    print(f'Zostalo ci {punkty} pkt')
                    break
            except ValueError:
                print('podana zla wartosc: ')
        while True:
            try:
                Zdrowie = int(input(f"Zdrowie: "))

                if Zdrowie <= punkty:
                    punkty -=Zdrowie
                    print(f'Zostalo ci {punkty} pkt')
                    break
            except ValueError:
                print('podana zla wartosc: ')

        while True:
            try:
                Madrosc = int(input(f"Madrosc: "))

                if Madrosc <= punkty:
                    punkty -=Madrosc
                    print(f'Zostalo ci {punkty} pkt')
                    break
            except ValueError:
                print('podana zla wartosc: ')

        while True:
            try:
                Zrecznosc = int(input(f"Zrecznosc: "))

                if Zrecznosc <= punkty:
                    punkty -=Zrecznosc
                    print(f'Zostalo ci {punkty} pkt')
                    break
            except ValueError:
                print('podana zla wartosc: ')
        zmienna =[["Health", sila], ["Strenght", Zdrowie], ["Agility", Madrosc], ["Inteligence", Zrecznosc], ["reszta punktow", punkty]]
        bohater[name] = zmienna

    elif menu1 == 3:
        name = input("Podaj imie bohatera: ")
        if name in bohater:
            print("Ktory przedmiot chcesz sprzedac?: ")
            n=1
            for i in bohater[name]:
                print(f"Atrybut {n}: {i}")
                n+=1
            while True:
                try:
                    sell = int(input(f"Podaj nr ktory chcesz sprzedac: "))
                    if 0 < sell < 5 :
                        break
                except ValueError:
                    print('podana zla wartosc: ')
            sell -=1
            print(bohater[name][sell])
            while True:
                try:
                    wartosc = int(input(f"Podaj wartosc jaka chcesz odjac: "))
                    if bohater[name][sell][1] >=wartosc>=0:
                        break
                    else:
                        print("Podano zla wartosc")
                except ValueError:
                    print('podana zla wartosc: ')
            bohater[name][sell][1] -= wartosc
            bohater[name][4][1] += wartosc
        else:
            print("Nie znalazlem takiego bohatera")

    elif menu1 == 4:
        name = input("Podaj imie bohatera: ")
        if name in bohater:
            print("Ktory przedmiot chcesz dokupic?: ")
            print(f"Zostalo ci {bohater[name][4][1]}")
            n=1
            for i in bohater[name]:
                print(f"Atrybut {n}: {i}")
                n+=1
            while True:
                try:
                    buy = int(input(f"Podaj nr ktory chcesz Dokupic: "))
                    if 0 < buy < 5 :
                        break
                except ValueError:
                    print('podana zla wartosc: ')
            buy -=1
            print(bohater[name][buy])
            while True:
                try:
                    wartosc = int(input(f"Podaj wartosc jaka chcesz dodac: "))
                    if bohater[name][4][1] >=wartosc>=0:
                        break
                    else:
                        print("Podano zla wartosc")
                except ValueError:
                    print('podana zla wartosc: ')

            bohater[name][buy][1] += wartosc
            bohater[name][4][1] -= wartosc

    elif menu1 == 5:
        name = input("Podaj imie bohatera: ")
        if name in bohater:
            print(bohater[name])
        else:
            print("Nie znalazlem takiego bohatera")
    else:
        print("podana bledna wartosc")
