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
    print("\nPasswort neu festlegen\n")
    print("Ihr Passwort muss enthalten:")
    print("- Mindestens 8 Zeichen")
    print("- Gross- und Kleinschreibung")
    print("- Mindestens eine Zahl")
    print("- Mindestens ein Sonderzeichen: $, @, #, %, !, ?, &, *")


SpecialSym = ['$', '@', '#', '%', '!', '?', '&', '*']
val = True

while True:
    val = True
    passwort_neu1 = input("Geben Sie Ihr neues Passwort ein: ")

    
    # Validierung
    if len(passwort_neu1) < 8:
        print('\n\033[31mPasswort muss mindestens 8 Zeichen lang sein\033[0m')
        val = False
    if len(passwort_neu1) > 20:
        print('\n\033[31mPasswort darf maximal 20 Zeichen lang sein\033[0m')
        val = False
    if not any(char.isdigit() for char in passwort_neu1):
        print('\n\033[31mPasswort muss mindestens eine Zahl enthalten\033[0m')
        val = False
    if not any(char.isupper() for char in passwort_neu1):
        print('\n\033[31mPasswort muss mindestens einen Grossbuchstaben enthalten\033[0m')
        val = False
    if not any(char.islower() for char in passwort_neu1):
        print('\n\033[31mPasswort muss mindestens einen Kleinbuchstaben enthalten\033[0m')
        val = False
    if not any(char in SpecialSym for char in passwort_neu1):
        print('\n\033[31mPasswort muss mindestens ein Sonderzeichen enthalten ($,@,#,%,!,?,&,* )\033[0m')
        val = False

    
    # Wenn gültig, zweite Eingabe abfragen
    if val:
        passwort_neu2 = input("Geben Sie Ihr neues Passwort erneut ein: ")
        if passwort_neu1 == passwort_neu2:
            passwort = passwort_neu1
            print("\n\033[92mPasswort erfolgreich geändert!\033[0m")
            break
        else:
            print("\n\033[31mDie Passwörter stimmen nicht überein!\033[0m\n")
    else:
        print("\n\033[31mBitte versuchen Sie es erneut.\033[0m\n")
