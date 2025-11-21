import sys  #für Beendung des Programms bei zu vielen fehlerhaften Anmeldungen

#mit Passwort einloggen
passwort = 1234
anmeldeversuche = 0

passwort_input = int(input("Bitte geben Sie ihr Passwort ein:"))
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
