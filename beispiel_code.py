#!/usr/bin/env python3

# Einführung in Funktionen mit Typehints

# Funktion zur Addition zweier Zahlen mit Typehints
def addiere(zahl1: int, zahl2: int) -> int:
  ret = zahl1 + zahl2
  return ret

# Funktion zur Begrüßung eines Benutzers mit Typehints
def begruessung(name: str) -> str:
  return f"Hallo, {name}!"

# Funktion zur Berechnung des Flächeninhalts eines Rechtecks mit Typehints
def berechne_flaeche(laenge: float, breite: float) -> float:
    """
    Berechne die Fläche des Rechtecks.
    Parameters:
      laenge (float): Die Länge des Rechtecks.
      breite (float): Fie Breite des Rechtecks.
    Returns:
      float: die Fläche des Rechtecks.
    """

    return laenge * breite

def subtrahiere(zahl1: int, zahl2: int) -> int:
  ret = zahl1 - zahl2
  return ret

summe = addiere(10,5)
print(summe)

gruss = begruessung("Hans Meiser")
print(gruss)

flaeche = berechne_flaeche(10.5, 4.3)
print(flaeche)

differenz = subtrahiere(100.5, 50.3)
print(differenz)