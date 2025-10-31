# Standardkategorien mit Beispieldaten
budget_kategorien = {
    "Lebensmittel": [
        "Einkauf Coop - 45 CHF",
        "Gemüsemarkt - 12 CHF",
        "Bäckerei - 8 CHF",
        "Migros - 30 CHF",
        "Kaffee to go - 4 CHF",
        "Snacks Tankstelle - 6 CHF",
        "Wochenmarkt - 20 CHF",
        "Pizzaabend - 25 CHF",
        "Getränkeautomat - 3 CHF",
        "Bio-Laden - 18 CHF"
    ],
    "Miete": [
        "Monatsmiete Oktober - 1200 CHF",
        "Nebenkosten - 150 CHF",
        "Internet - 60 CHF",
        "Stromrechnung - 90 CHF",
        "Hauswartung - 30 CHF",
        "Heizung - 100 CHF",
        "Hausratsversicherung - 25 CHF",
        "TV-Gebühr - 40 CHF",
        "Wasser - 35 CHF",
        "Reparatur Tür - 75 CHF"
    ],
    "Freizeit": [
        "Kinoabend - 20 CHF",
        "Bowling - 15 CHF",
        "Museumseintritt - 12 CHF",
        "Netflix Abo - 18 CHF",
        "Fitnessstudio - 50 CHF",
        "Ausflug Zürichsee - 25 CHF",
        "Buchhandlung - 22 CHF",
        "Café mit Freunden - 14 CHF",
        "Konzertticket - 60 CHF",
        "Eis essen - 6 CHF"
    ]
}



def anzeigen_kategorien():
    print("\n\033[1mAktuelle Budget-Kategorien: \033[0m")
    for i, kategorie in enumerate(budget_kategorien.keys(), start=1 ):
        print(f"{i}. {kategorie}")
    print("")

    try:
        auswahl = int(input("\033[38;5;208mGebe die Nummer der gewünschten Kategorie ein, um sie anzuzeigen: \033[0m")) - 1
        kategorien_liste = list(budget_kategorien.keys())
        if 0 <= auswahl < len(kategorien_liste):
            gewählte_kategorie = kategorien_liste[auswahl]
            print(f"\n\033[1mKostenübersicht für \033[1m{gewählte_kategorie}\033[0m:") # \033[1m und \033[0m für fette formatierung ¬ \n zeilenumbruch
            print(f"{'Kostenart':<30} {'Betrag (CHF)':>12}")    # neu hinzugefügt für formatierung
            print("-" * 45) # Gestrichelte linie als trenner
            for zeile in budget_kategorien[gewählte_kategorie]:
                teile = zeile.split(" - ")                                                     # von hier bis
                if len(teile) == 2:
                    kostenart = teile[0].strip()
                    betrag_str = teile[1].replace("CHF", "").strip()               #
                    try:
                        betrag = float(betrag_str)
                        print(f"{kostenart:<30} {betrag:>12.2f}")                             #
                    except ValueError:
                        print(f"{kostenart:<30} {'Ungültiger Betrag':>12}")                #
                else:
                    print(f"{zeile:<30} {'Formatfehler':>12}")                            # hier neu eingesetz wegen formatierung
        else:
            print("\n\033[31mAchtung: Ungültige Nummer!\033[0m")  #Fehlermeldung
    except ValueError:
        print("Bitte eine gültige Zahl eingeben.")



def neue_kategorie_hinzufügen():                                        # wenn bereits gleichen eigegene wird?
    neue_kategorie = input("\n\033[38;5;208mGib den Namen der neuen Kategorie ein: \033[0m").strip() #strip entfernt leerzeichen vorne hinte etc.

    if not neue_kategorie:                                                    # Prüfen auf leere Eingabe
        print("\n\033[31mBitte gib einen gültigen Namen ein.\033[0m")
    elif neue_kategorie in budget_kategorien:                                     #   Prüfen auf Duplikat
        print(f"\n\033[31mAchtung: Die Kategorie '{neue_kategorie}' existiert bereits: \033[0mBitte gib einen anderen Namen ein, der noch nicht verwendet wurde.")
    else:
        budget_kategorien[neue_kategorie] = []
        print(f"\n\033[32mKategorie '{neue_kategorie}' wurde erfolgreich hinzugefügt.\033[0m")



def kategorie_bearbeiten():
    kategorien_liste = list(budget_kategorien.keys())

    print("\n\033[1mAktuelle Budget-Kategorien: \033[0m")
    for i, kategorie in enumerate(kategorien_liste, start=1):
        print(f"{i}. {kategorie}")
    print("")

    try:
        index = int(input("\033[38;5;208mWähle eine Kategorie aus, die du bearbeiten möchtest (Nummer): \033[0m")) - 1
    except ValueError:
        print("\n\033[31mAchtung: Bitte eine gültige Zahl eingeben.\033[0m")
        return

    if not (0 <= index < len(kategorien_liste)):
        print("\n\033[31mAchtung: Ungültige Nummer: \033[0mBitte wähle eine Zahl aus der Liste.")
        return

    gewählte_kategorie = kategorien_liste[index]

    print(f"\n\033[1mWas möchtest du in der Kategorie '{gewählte_kategorie}' bearbeiten?\033[0m")
    print("1. Namen ändern")
    print("2. Eintrag hinzufügen")
    print("3. Eintrag löschen")
    print("4. Kategorie löschen")
    print("")

    try:
        aktion = int(input("\033[38;5;208mGib die Nummer der gewünschten Aktion ein: \033[0m"))
    except ValueError:
        print("\n\033[31mBitte eine gültige Zahl eingeben.\033[0m")
        return

    if aktion == 1:
        neuer_name = input("Neuer Name für die Kategorie: ").strip()
        if not neuer_name:
            print("\n\033[31mDer neue Name darf nicht leer sein.\033[0m")
        elif neuer_name in budget_kategorien:
            print(f"\n\033[31mDie Kategorie '{neuer_name}' existiert bereits.\033[0m")
        else:
            budget_kategorien[neuer_name] = budget_kategorien.pop(gewählte_kategorie)
            print(f"\n\033[32mKategorie wurde erfolgreich von '{gewählte_kategorie}' zu '{neuer_name} umbenannt'.\033[0m")

    elif aktion == 2:
        art = input("\nArt der Kosten: ").strip()
        try:
            betrag = float(input("Betrag in CHF: "))
            budget_kategorien[gewählte_kategorie].append(f"{art} - {betrag} CHF")
            print(f"\n\033[32mEintrag '{art} – {betrag} CHF' wurde erfolgreich hinzugefügt.\033[0m")
        except ValueError:
            print("\n\033[31mAchtung: Ungültiger Betrag.\033[0m")

    elif aktion == 3:                                                           # überlegen ob hier oder unter Menü behalten / löschen
        einträge = budget_kategorien[gewählte_kategorie]
        if not einträge:
            print("\n\033[33mKeine Einträge vorhanden! (0 Positionen)\033[0m")
            return

        print("\n\033[1mAktuelle Einträge: \033[0m")
        for i, eintrag in enumerate(einträge, start=1):
            print(f"{i}. {eintrag}")

        try:
            zu_löschen = int(input("\n\033[38;5;208mNummer des Eintrags zum Löschen: \033[0m")) - 1
            gelöscht = einträge.pop(zu_löschen)
            print(f"\n\033[32mEintrag '{gelöscht}' wurde erfolgreich gelöscht.\033[0m")
        except (ValueError, IndexError):
            print("\n\033[31mUngültige Auswahl.\033[0m")

    elif aktion == 4:
        del budget_kategorien[gewählte_kategorie]
        print(f"\n\033[32mKategorie '{gewählte_kategorie}' wurde gelöscht.\033[0m")

    else:
        print("\n\033[31mUngültige Aktion. Bitte wähle eine Zahl zwischen 1 und 4.\033[0m")



def kategorie_löschen():
    kategorien_liste = list(budget_kategorien.keys())
    for i, kategorie in enumerate(kategorien_liste, start=1):
        print(f"{i}. {kategorie} \n")
    try:
        index = int(input("\n\033[38;5;208mWelche Kategorie möchtest du löschen? (Nummer): \033[0m")) - 1
        if 0 <= index < len(kategorien_liste):
            entfernte = budget_kategorien.pop(kategorien_liste[index])
            print(f"\n\033[32mKategorie '{kategorien_liste[index]}' wurde erfolgreich gelöscht.\033[0m")
        else:
            print("\n\033[31mAchtung: Ungültige Nummer.\033[0m")
    except ValueError:
        print("Bitte eine gültige Zahl eingeben.")


# Hauptmenü
def hauptmenü():
    while True:
        print("\n\n\033[1mKategorien Menü\033[0m")
        print("1. Kategorien anzeigen")
        print("2. Neue Kategorie hinzufügen")
        print("3. Kategorie bearbeiten")
        print("4. Kategorie löschen")
        print("5. Beenden")

        auswahl = input("\n\033[38;5;208mWähle eine Option (1-5): \033[0m")  #Text farbe organee

        if auswahl == "1":
            anzeigen_kategorien()
        elif auswahl == "2":
            neue_kategorie_hinzufügen()
        elif auswahl == "3":
            kategorie_bearbeiten()
        elif auswahl == "4":
            kategorie_löschen()
        elif auswahl == "5":
            print("\n\033[32mProgramm beendet.\033[0m")
            break
        else:
            print("\n\033[31mUngültige Eingabe: \033[0mBitte wähle eine Zahl zwischen 1 und 5.")

# Hauptfunktion für den Programmstart
def main():
    hauptmenü()

# Nur ausführen, wenn dieses Skript direkt gestartet wird
if __name__ == "__main__":
    main()
