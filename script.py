#!/usr/bin/env python3

import argparse

# Aufgabe: Erstellen Sie ein Skript, das einfache mathematische Operationen basierend auf Befehlszeilenargumenten durchführt.

# 1. Das Skript soll zwei Pflichtargumente akzeptieren, die als ganze Zahlen eingegeben werden.
#    - 'zahl1': Die erste Zahl, die verwendet wird.
#    - 'zahl2': Die zweite Zahl, die verwendet wird.

# 2. Es soll ein optionales Argument '--operation' geben, das die gewünschte mathematische Operation festlegt:
#    - Mögliche Optionen: 'add' (Addition), 'sub' (Subtraktion), 'mul' (Multiplikation), 'div' (Division).
#    - Wenn keine Operation angegeben wird, soll standardmäßig die Addition ausgeführt werden.

# 3. Implementieren Sie die Berechnungslogik für die oben genannten Operationen:
#    - Bei der Division soll eine Fehlerbehandlung implementiert werden, um eine Division durch Null zu vermeiden.

# 4. Geben Sie das Ergebnis der Berechnung aus.

parser = argparse.ArgumentParser(description="Gib zwei Zahlen ein und optional den Operator. Default ist die Addition")
parser.add_argument("zahl1",help="Zahl1. Diese Zahl ist ein Integer", type=int)
parser.add_argument("zahl2",help="Zahl2. Diese Zahl ist ein Integer", type=int)
parser.add_argument("--operation",default="add", help="Operator, default is add", type=str, choices=["add", "sub", "mul", "div"])

args = parser.parse_args()

if (args.operation == "add"):
        print("Das Ergebnis von "+str(args.zahl1)+" + "+str(args.zahl2)+" ist " + str((args.zahl1+args.zahl2)))
elif (args.operation == "sub"):
        print("Das Ergebnis von "+str(args.zahl1)+" - "+str(args.zahl2)+" ist " + str((args.zahl1-args.zahl2)))
elif (args.operation == "mul"):
        print("Das Ergebnis von "+str(args.zahl1)+" * "+str(args.zahl2)+" ist " + str((args.zahl1*args.zahl2)))
elif (args.operation == "div"):
        print("Das Ergebnis von "+str(args.zahl1)+" / "+str(args.zahl2)+" ist " + str(float(args.zahl1)/float(args.zahl2)))

