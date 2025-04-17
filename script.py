#!/usr/bin/env python3

# Aufgabe: Erstellen Sie ein Skript, das die Länge eines Textes analysiert und Informationen darüber liefert.

# Das Skript soll folgende Funktionalität bieten:
# 1. Ein Pflichtargument (positional argument), das einen Text entgegennimmt.
# 2. Ein optionales Argument --details, das zusätzliche Informationen liefert:
#    - Anzahl der Wörter
# 3. Wenn das Argument --details nicht angegeben wird, soll nur die Anzahl der Zeichen ausgegeben werden.

# Beispiel:
# python3 script.py "Dies ist ein Beispieltext." --details
# Ausgabe:
# Zeichen: 27
# Wörter: 5

# Optional: Erweitern Sie das Skript, um auch die Anzahl der Vokale und Konsonanten zu zählen.
import argparse

parser = argparse.ArgumentParser(description="Dieses Script zählt die Anzahl der Zeichen in einem Text")

parser.add_argument("text",help="Gib einen Text ein, von dem ich die Zeichen und Wörter zählen soll", type=str)
parser.add_argument("--woerter", help="wieviele Wörter hat der Text ?", type=int, default=None)

args = parser.parse_args()

text_len = len(args.text)
print("Zeichen: "+ str(text_len))
if args.woerter is not None:
    print("Wörter: " + str(args.woerter))

text_wo_space = args.text.replace(" ","")
print("ohne Leerzeichen: " + str(len(text_wo_space)))

liste_vokale = ["a", "e", "i", "o", "u"]
count_vokale = 0
for vokale in liste_vokale:
    count_vokale = count_vokale + args.text.count(vokale)

print("vokale: "+ str(count_vokale))
print("kons: "+ str(len(text_wo_space)-count_vokale))