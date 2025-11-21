import sys  #für Beendung des Programms bei zu vielen fehlerhaften Anmeldungen

#mit Passwort einloggen
passwort = "Test1234"
anmeldeversuche = 0

passwort_input = input("Bitte geben Sie ihr Passwort ein:")
while passwort != passwort_input:
    anmeldeversuche = anmeldeversuche + 1

    anmeldeversuche = int(anmeldeversuche)
    if anmeldeversuche == 3:
        print("\n\033[31mZu viele fehlerhafte Anmeldungen!\033[0m")
        sys.exit(1) #evtl. ein Time-Out implementieren
    else:
        passwort_input = int(input("\n\033[31mFehlerhaftes Passwort! Versuchen Sie es nochmals:\033[0m"))
else:
    print("\n\033[92mErfolgreich eingeloggt!\033[0m")
    print("")

# Funktion - Passwort ändern
änderung_input = input("Bitte geben Sie ihr Passwort ein:")
while passwort != änderung_input:
    print("\n\033[31mUngültiges Passwort!\033[0m")
    änderung_input = input("Versuchen Sie es erneut:")
    
else:
    print("")
    print("Passwort neu festlegen")
    print("")
    print("Ihr Passwort muss enthalten:")
    print("-Mindestens 8 Zeichen")
    print("-Gross- und Kleinschreibung")
    print("-Mindestens eine Zahl")
    print("-Mindestens ein Sonderzeichen")
    print("")
