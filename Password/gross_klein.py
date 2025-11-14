# App Funktionen definieren
import sys
import regex as re

# pylance Import nicht notwendig, da es als extension vorhanden ist

# App durch Passwort schützen
passwort = "T12"  # Passwort mit Buchstaben, Gross- und Kleinschreibung funktioniert

anmeldeversuche = 0

passwort_input = (input("Bitte geben Sie ihr Passwort ein:"))
while passwort != passwort_input:
    anmeldeversuche = anmeldeversuche + 1

    anmeldeversuche = int(anmeldeversuche)
    if anmeldeversuche == 3:
        print("zu viele fehlerhafte Anmeldungen")
        # Programm beenden Nachricht
        sys.exit(1)

    passwort_input = (input("Falsches Passwort, versuchen Sie es nochmals:"))
else:
    print("Erfolgreich eingeloggt")
    print("")


# Funktion - Passwort ändern

input("Bitte geben Sie ihr Passwort ein:")
if passwort != passwort_input:
    print("Falsches Passwort")
else:
    print("")
    print("Passwort neu festlegen")
    print("")
    print("Ihr Passwort muss enthalten:")
    print("-Mindestens 8 Zeichen")
    print("-Gross- und Kleinschreibung")
    print("-Mindestens eine Zahl")
    print("-Mindestens ein Sonderzeichen")

passwort_neu1 = (input("Geben Sie das neue Passwort ein:"))


# Passwort auf Sicherheitsvorgaben validieren --> ein Package importieren?
def ValidPasswortNeu(passwort_neu1):
    SpecialSym = ['$', '@', '#', '%', '!', '?', '&', '*']
    val = True

    # Länge des Passworts überprüfen
    if len(passwort_neu1) < 8:
        print('Passwort muss mindestens 8 Zeichen lang sein')
        val = False
    if len(passwort_neu1) > 20:
        print('Passwort darf maximal 20 Zeichen lang sein')
        val = False

        # lowerCase = False
        # upperCase = False
        # num = False
        # special = False

        has_digit = has_upper = has_lower = has_special = False

        # Überprüfen, ob Gross- und Kleinbuchstaben, Zahlen und Sonderzeichen enthalten sind
        for char in passwort_neu1:
            if (char.isdigit()):
                has_digit = True
            if (char.islower()):
                has_lower = True
            if (char.isupper()):
                has_upper = True
            if (not char.isalnum()):  # überprüfen, dass Sonderzeichen erkannt werden
                has_special = True
            # schauen ob if oder elif bei dem oberen code verwendet werden soll

        if not has_digit:
            print('Passwort muss mindestens eine Zahl enthalten')
            val = False
        if not has_upper:
            print('Passwort muss mindestens einen Grossbuchstaben enthalten')
            val = False
        if not has_lower:
            print('Passwort muss mindestens einen Kleinbuchstaben enthalten')
            val = False
        if not has_special:
            print('Passwort muss mindestens ein Sonderzeichen enthalten')
            val = False
        return val

    else:
        return False


passwort_neu2 = (input("Geben Sie ihr neues Passwort erneut ein:"))
print(" ")

if (passwort_neu1) == (passwort_neu2):
    passwort = passwort_neu1
    print("Passwort erfolgreich geändert")
else:
    print("die Passwörter stimmen nicht überein")
