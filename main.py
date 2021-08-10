#!/usr/bin/env python3
import pyautogui
import time
from random import seed, randint

seed()

print('Satz (1) / Buchstaben (2)')

spamtype = input()[0]

if spamtype not in '12sbSB':
    print('Please enter a proper spam mode.')
    exit(1)

if spamtype in '1sS':
    print("Sie haben den Satz-Spambot gewählt")
    print("")

    print("Welchen Text möchten sie Spamen?")
    print("1 steht für einen vorhandenen Text, 2 um selbst einen zu machen:")
    erstep = 0
    while erstep == 0:

        try:
            y = int(input())
            if y == 1 or y == 2:
                erstep = erstep + 1
            else:
                print("Muss die Zahl 1 oder 2 sein")
                pass
        except:
            print("Muss eine natürliche Zahl sein")

    if y == 1:
        pass
    elif y == 2:
        print("Gebe deinen Text ein:")

        p = 0
        while p == 0:
            try:
                s = str(input())
                p = p + 1
            except:
                print(
                    "Irgendetwas ist bei deinem Text nicht zu verarbeiten, versuche es mit anderen Zeichen/Buchstaben")

                p2 = 0
                while p2 == 0:
                    print("Gebe 1 ein um es erneut zu versuchen, oder 2 für den vorhandenen Text:")

                    ss = 0
                    while ss < 1 or ss > 2:
                        pp = 0
                        while pp == 0:
                            try:
                                ss = int(input())
                                pp = pp + 1
                            except:
                                print("Sie müssen eine ganze Zahl eingeben!")

                        if ss == 2:
                            p = p + 1
                            p2 = p2 + 1
                        elif ss == 1:
                            p2 = p2 + 1
                            pass
                        else:
                            pass

    # Geschwindigkeit festlegen
    print("Lege die Geschwindigkeit fest, je größer die Zahl, desto langsamer der Bot (in Sekunden)")
    g = -1
    while g < 0:
        print("Es geht nicht schneller als 0:")
        try:
            g = float(input())
        except:
            print("Muss eine natürliche Zahl sein")
            pass

    # Anzahl festlegen
    print("Lege die Anzahl des zu versendenden Textes ein")
    anz = -1
    while anz < 0:
        print("Es geht nicht weniger als 0:")
        try:
            anz = int(input())
        except:
            print("Muss eine ganze Zahl sein")
            pass

    # Warten
    print("Sie haben 15 Sekunden zeit, den Chat auszuwählen...")
    time.sleep(15)

    # Spamen
    if y == 1:
        x = 0

        while x <= anz:
            x = x + 1

            zua = randint(1, 20)
            if zua == 1:
                s = "Physik ist super"
            elif zua == 2:
                s = "Pytob stinkt wie ein verrottender Schildkroeten-Kadaver"
            elif zua == 3:
                s = "Allgemeine Relativitaetstheorie for the win"
            elif zua == 4:
                s = "May mass times acceleration be with you"
            elif zua == 5:
                s = "Bloodbath"
            elif zua == 6:
                s = "gd"
            elif zua == 7:
                s = "Das Haus des Verderbens"
            elif zua == 8:
                s = "Trink mal weniger Monster"
            elif zua == 9:
                s = "Karl von Chlodwig"
            elif zua == 10:
                s = "Mach mal mehr Sport!"
            elif zua == 11:
                s = "Nicht so viel essen, mein Haus"
            elif zua == 12:
                s = "Was ist hier los"
            elif zua == 13:
                s = "Moin"
            elif zua == 14:
                s = "Du stinkst"
            elif zua == 15:
                s = "Tallinn, die Hauptstadt von Estland"
            elif zua == 16:
                s = "Visit GD Quant"
            elif zua == 17:
                s = "Pytob stinkt wie ein verrottender Schildkroeten-Kadaver"
            elif zua == 18:
                s = "Pytob stinkt wie ein verrottender Schildkroeten-Kadaver"
            elif zua == 19:
                s = "Pytob stinkt wie ein verrottender Schildkroeten-Kadaver"
            else:
                s = "Pytob stinkt wie ein verrottender Schildkroeten-Kadaver"

            n = [s]

            for word in n:
                pyautogui.typewrite(word)
                pyautogui.press("enter")
                time.sleep(g)
    else:
        x = 0

        while x <= anz:
            x = x + 1

            n = [s]

            for word in n:
                pyautogui.typewrite(word)
                pyautogui.press("enter")
                time.sleep(g)


elif type == 2:
    print("Sie haben den Buchstaben-Spambot gewählt.")
    print("")

    print("Welchen Text möchten sie Spamen?")
    print("1 steht für einen vorhandenen Text, 2 um selbst einen zu machen:")
    erstep = 0
    while erstep == 0:

        try:
            y = int(input())
            if y == 1 or y == 2:
                erstep = erstep + 1
            else:
                print("Muss die Zahl 1 oder 2 sein")
                pass
        except:
            print("Muss eine natürliche Zahl sein")

    if y == 1:
        pass
    elif y == 2:
        print("Gebe deinen Text ein:")

        p = 0
        while p == 0:
            try:
                s = str(input())
                p = p + 1
            except:
                print(
                    "Irgendetwas ist bei deinem Text nicht zu verarbeiten, versuche es mit anderen Zeichen/Buchstaben")

                p2 = 0
                while p2 == 0:
                    print("Gebe 1 ein um es erneut zu versuchen, oder 2 für den vorhandenen Text:")

                    ss = 0
                    while ss < 1 or ss > 2:
                        pp = 0
                        while pp == 0:
                            try:
                                ss = int(input())
                                pp = pp + 1
                            except:
                                print("Sie müssen eine ganze Zahl eingeben!")

                        if ss == 2:
                            p = p + 1
                            p2 = p2 + 1
                        elif ss == 1:
                            p2 = p2 + 1
                            pass
                        else:
                            pass

    # Geschwindigkeit festlegen
    print("Lege die Geschwindigkeit fest, je größer die Zahl, desto langsamer der Bot (in Sekunden)")
    g = -1
    while g < 0:
        print("Es geht nicht schneller als 0:")
        try:
            g = float(input())
        except:
            print("Muss eine natürliche Zahl sein")
            pass

    # Anzahl festlegen
    print("Lege die Anzahl des zu versendenden Textes ein")
    anz = -1
    while anz < 0:
        print("Es geht nicht weniger als 0:")
        try:
            anz = int(input())
        except:
            print("Muss eine ganze Zahl sein")
            pass

    # Warten
    print("Sie haben 15 Sekunden zeit, den Chat auszuwählen...")
    time.sleep(15)

    # Spamen
    if y == 1:
        x = 0

        while x <= anz:
            x = x + 1

            zua = random.randint(1, 20)
            if zua == 1:
                s = "Physik ist super"
            elif zua == 2:
                s = "chrissx stinkt wie ein verrottender Schildkroeten-Kadaver"
            elif zua == 3:
                s = "Allgemeine Relativitaetstheorie for the win"
            elif zua == 4:
                s = "May mass times acceleration be with you"
            elif zua == 5:
                s = "Bloodbath"
            elif zua == 6:
                s = "gd"
            elif zua == 7:
                s = "Das Haus des Verderbens"
            elif zua == 8:
                s = "Trink mal weniger Monster"
            elif zua == 9:
                s = "Karl von Chlodwig"
            elif zua == 10:
                s = "Mach mal mehr Sport!"
            elif zua == 11:
                s = "Nicht so viel essen, mein Haus"
            elif zua == 12:
                s = "Was ist hier los"
            elif zua == 13:
                s = "Moin"
            elif zua == 14:
                s = "Du stinkst"
            elif zua == 15:
                s = "Tallinn, die Hauptstadt von Estland"
            elif zua == 16:
                s = "Visit GD Quant"
            elif zua == 17:
                s = "chrissx stinkt wie ein verrottender Schildkroeten-Kadaver"
            elif zua == 18:
                s = "chrissx stinkt wie ein verrottender Schildkroeten-Kadaver"
            elif zua == 19:
                s = "chrissx stinkt wie ein verrottender Schildkroeten-Kadaver"
            else:
                s = "chrissx stinkt wie ein verrottender Schildkroeten-Kadaver"

            n = s

            for word in n:
                pyautogui.typewrite(word)
                pyautogui.press("enter")
                time.sleep(g)
    else:
        x = 0

        while x <= anz:
            x = x + 1

            n = s

            for word in n:
                pyautogui.typewrite(word)
                pyautogui.press("enter")
                time.sleep(g)



