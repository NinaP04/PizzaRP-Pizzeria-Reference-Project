# Packete um Eingaben zuspeichern vor beendung des programms
import json
import os

# JSON weil komplexe, strukturierte Daten einfach speichern und laden - Flexibilität
DATEN_DATEI = "budget_daten.json"

STANDARD_KATEGORIEN = {
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

budget_kategorien = {}     # z. B. {"Miete": ["Strom - 90 CHF", ...]}
budget_limits = {}         # z. B. {"Miete": 1500}
finanzziele = {}           # z. B. {"Miete": {"ziel": 1200, "meldung": "Ziel erreicht!"}}


def daten_laden():
    global budget_kategorien, budget_limits, finanzziele
    if os.path.exists(DATEN_DATEI):
        with open(DATEN_DATEI, "r", encoding="utf-8") as f:
            daten = json.load(f)
            budget_kategorien = daten.get("budget_kategorien", {})
            budget_limits = daten.get("budget_limits", {})
            finanzziele = daten.get("finanzziele", {})
    else:
        # Erste Programmausführung → Standarddaten übernehmen
        budget_kategorien = STANDARD_KATEGORIEN.copy()
        budget_limits = {}
        finanzziele = {}


def daten_speichern():
    daten = {
        "budget_kategorien": budget_kategorien,
        "budget_limits": budget_limits,
        "finanzziele": finanzziele
    }
    with open(DATEN_DATEI, "w", encoding="utf-8") as f:
        json.dump(daten, f, indent=4, ensure_ascii=False)




# Standardkategorien mit Beispieldaten


budget_limit = None
finanzielle_ziele = []


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
    global budget_limit
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
            print(f"\n\033[32mKategorie wurde erfolgreich von '{gewählte_kategorie}' zu '{neuer_name}' umbenannt.\033[0m")


    elif aktion == 2:

        art = input("\nArt der Kosten: ").strip()

        try:

            betrag = float(input("Betrag in CHF: "))

            # Berechne aktuelle Summe der Kategorie

            aktuelle_summe = 0

            for eintrag in budget_kategorien[gewählte_kategorie]:

                teile = eintrag.split(" - ")

                if len(teile) == 2:

                    try:

                        aktuelle_summe += float(teile[1].replace("CHF", "").strip())

                    except ValueError:

                        continue

            neue_summe = aktuelle_summe + betrag

            # Budgetlimit prüfen

            limit = budget_limits.get(gewählte_kategorie)

            print(f"\n\033[32mEintrag '{art} – {betrag} CHF' wurde erfolgreich hinzugefügt.\033[0m")

            if limit is not None and neue_summe > limit:
                print(
                    f"\033[31mAchtung: Budgetlimit von {limit:.2f} CHF für '{gewählte_kategorie}' überschritten!\033[0m")

            budget_kategorien[gewählte_kategorie].append(f"{art} - {betrag} CHF")

        except ValueError:

            print("\n\033[31mAchtung: Ungültiger Betrag.\033[0m")

    elif aktion == 3:
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


# Globale Variablen für Limits und Ziele pro Kategorie
budget_limits = {}  # z. B. {"Freizeit": 300.0}
finanzziele = {}    # z. B. {"Freizeit": {"ziel": 200.0, "meldung": "Ziel erreicht!"}}

def finanzkontrolle():
    global budget_limits, finanzziele

    kategorien_liste = list(budget_kategorien.keys())
    print("\n\033[1mFinanzkontrolle pro Kategorie\033[0m")
    for i, kategorie in enumerate(kategorien_liste, start=1):
        print(f"{i}. {kategorie}")
    print("")

    try:
        index = int(input("\033[38;5;208mWähle eine Kategorie für die Finanzkontrolle (Nummer): \033[0m")) - 1
        if not (0 <= index < len(kategorien_liste)):
            print("\n\033[31mUngültige Auswahl.\033[0m")
            return
    except ValueError:
        print("\n\033[31mBitte eine gültige Zahl eingeben.\033[0m")
        return

    gewählte_kategorie = kategorien_liste[index]

    print(f"\n\033[1mWas möchtest du für '{gewählte_kategorie}' bearbeiten?\033[0m")
    print("1. Budgetlimite")
    print("2. Finanzziel")
    print("3. Zurück zum Hauptmenü")

    hauptwahl = input("\n\033[38;5;208mWähle eine Option (1–3): \033[0m")

    if hauptwahl == "1":
        print(f"\n\033[1mBudgetlimite für '{gewählte_kategorie}'\033[0m")
        print("1. Anzeigen")
        print("2. Setzen")
        print("3. Ändern")
        print("4. Entfernen")
        print("5. Zurück")

        auswahl = input("\n\033[38;5;208mWähle eine Option (1–5): \033[0m")

        if auswahl == "1":
            limit = budget_limits.get(gewählte_kategorie)
            if limit is not None:
                print(f"\n\033[1mAktuelles Budgetlimit:\033[0m {limit:.2f} CHF")
            else:
                print("\n\033[33mKein Budgetlimit gesetzt.\033[0m")

        elif auswahl == "2":
            try:
                limit = float(input("Neues Budgetlimit in CHF: "))
                budget_limits[gewählte_kategorie] = limit
                print(f"\n\033[32mBudgetlimite gesetzt: {limit:.2f} CHF\033[0m")
            except ValueError:
                print("\n\033[31mUngültiger Betrag.\033[0m")

        elif auswahl == "3":
            if gewählte_kategorie not in budget_limits:
                print("\n\033[33mKein Limit vorhanden.\033[0m")
            else:
                try:
                    neues_limit = float(input("Neues Limit in CHF: "))
                    budget_limits[gewählte_kategorie] = neues_limit
                    print(f"\n\033[32mLimit geändert auf {neues_limit:.2f} CHF\033[0m")
                except ValueError:
                    print("\n\033[31mUngültiger Betrag.\033[0m")

        elif auswahl == "4":
            if gewählte_kategorie in budget_limits:
                del budget_limits[gewählte_kategorie]
                print(f"\n\033[32mLimit entfernt.\033[0m")
            else:
                print("\n\033[33mKein Limit vorhanden.\033[0m")

    elif hauptwahl == "2":
        print(f"\n\033[1mFinanzziel für '{gewählte_kategorie}'\033[0m")
        print("1. Anzeigen")
        print("2. Setzen")
        print("3. Ändern")
        print("4. Entfernen")
        print("5. Zurück")

        auswahl = input("\n\033[38;5;208mWähle eine Option (1–5): \033[0m")

        if auswahl == "1":
            ziel_info = finanzziele.get(gewählte_kategorie)
            if ziel_info:
                print(f"\n\033[1mZiel:\033[0m {ziel_info['ziel']} CHF")
                print(f"Meldung: {ziel_info['meldung']}")
            else:
                print("\n\033[33mKein Ziel gesetzt.\033[0m")

        elif auswahl == "2":
            try:
                ziel = float(input("Zielbetrag in CHF: "))
                meldung = input("Meldung bei Zielerreichung: ").strip()
                finanzziele[gewählte_kategorie] = {"ziel": ziel, "meldung": meldung}
                print(f"\n\033[32mZiel gespeichert.\033[0m")
            except ValueError:
                print("\n\033[31mUngültiger Betrag.\033[0m")

        elif auswahl == "3":
            if gewählte_kategorie not in finanzziele:
                print("\n\033[33mKein Ziel vorhanden.\033[0m")
            else:
                try:
                    neues_ziel = float(input("Neues Ziel in CHF: "))
                    neue_meldung = input("Neue Meldung: ").strip()
                    finanzziele[gewählte_kategorie] = {"ziel": neues_ziel, "meldung": neue_meldung}
                    print(f"\n\033[32mZiel aktualisiert.\033[0m")
                except ValueError:
                    print("\n\033[31mUngültiger Betrag.\033[0m")

        elif auswahl == "4":
            if gewählte_kategorie in finanzziele:
                del finanzziele[gewählte_kategorie]
                print(f"\n\033[32mZiel entfernt.\033[0m")
            else:
                print("\n\033[33mKein Ziel vorhanden.\033[0m")

    elif hauptwahl == "3":
        return

    else:
        print("\n\033[31mUngültige Eingabe.\033[0m")



# Hauptmenü
def hauptmenü():
    while True:
        print("\n\n\033[1mKategorien Menü\033[0m")
        print("1. Kategorien anzeigen")
        print("2. Neue Kategorie hinzufügen")
        print("3. Kategorie bearbeiten")
        print("4. Kategorie löschen")
        print("5. Finanzkontrolle")
        print("6. Beenden")

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
            finanzkontrolle()
        elif auswahl == "6":
            print("\n\033[32mProgramm beendet.\033[0m")
            break
        else:
            print("\n\033[31mUngültige Eingabe: \033[0mBitte wähle eine Zahl zwischen 1 und 5.")

# Hauptfunktion für den Programmstart
def main():
    daten_laden()
    hauptmenü()
    daten_speichern()


# Nur ausführen, wenn dieses Skript direkt gestartet wird
if __name__ == "__main__":
    main()
