#!/usr/bin/env python3
from pyautogui import typewrite, press
from time import sleep
from random import seed, randint

def get_message(i):
    m = [
        "Physik ist super",
        "Allgemeine Relativitaetstheorie for the win",
        "May mass times acceleration be with you",
        "Bloodbath",
        "gd",
        "Das Haus des Verderbens",
        "Trink mal mehr Monster",
        "Karl von Chlodwig",
        "Mach mal weniger Sport!",
        "Auf nach Troscharad!",
        "Was ist hier los",
        "Moin",
        "Du stinkst",
        "Tallinn, die Hauptstadt von Estland",
        "Visit GD Quant",
    ]
    return m[i] if i < len(m) else "Pytob stinkt wie ein verrottender Schildkroeten-Kadaver"

def spam(elements, num, pause):
    for x in range(num + 1):
        for e in elements:
            typewrite(e)
            press("enter")
            sleep(pause)

def random_spam(num, pause, chars):
    for x in range(num + 1):
        m = get_message(randint(1, 20))
        if not chars: m = [m]
        for e in m:
            typewrite(e)
            press("enter")
            sleep(pause)

seed()

spamtype = input('Satz (1) / Buchstaben (2) ')[0]

if spamtype not in '12sbSB':
    print('Please enter a proper spam mode.')
    exit(1)

print("Vorhandener (1) / Eigener (2) Text ")
texttype = input()[0]

while texttype not in '12veVE':
    print('Please don\'t enter stupid shit.')
    texttype = input()[0]

if texttype in '2eE':
    s = input("Gebe deinen Text ein: ")

g = float(input("Sleep time in seconds. (float > 0) "))
if g < 0: raise 'no.'

anz = int(input("Lege die Anzahl des zu versendenden Textes ein. (int > 0) "))
while anz < 0: raise 'no.'

# Warten
print("Sie haben 5 Sekunden Zeit, den Chat auszuwählen...")
sleep(5)

# Spam
if texttype in '1vV':
    random_spam(anz, g, spamtype in '2bB')
else:
    spam([s] if spamtype in '1sS' else s, anz, g)
