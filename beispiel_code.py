#! /usr/bin/python

# Eingaben über die Kommandzeile
# Einlesen eines Strings
#name = input("Bitte gibt den Namen ein: ")
#print("Hallo, " + name + "!")

# Einlesen eines Integers und Umwandlung
alter = input("Bitte geben Sie Ihr Alter ein: ")
alter = int(alter)
print("Sie sind", alter, "Jahre alt.")
print("Sie sind " + str(alter) + " Jahre alt.") # alternativ

# Berechnung mit Alter
jahre_bis_30 = 30 -alter
if jahre_bis_30 > 0:
  print("In " + str(jahre_bis_30)+ " Jahren wirst Du 30")
else:
  print(" Du bist bereits 30 oder älter")

lieblingsfilm = input("Wie heißt Dein Lieblingsfilm?")
lieblingszahl = input("Wie lautet Deine Lieblingszahl?")

lieblingszahl = float(lieblingszahl)
neuezahl  = lieblingszahl+14.5

neuezahl  = lieblingszahl+14.5
print("Dein Lieblingsfilm ist \""+ 
      lieblingsfilm+"\" und wenn man  zu deiner Lieblingszahl 14.5 addiert erhälst Du "
      +str(neuezahl))