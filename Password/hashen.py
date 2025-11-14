# App Funktionen definieren
import sys
import bcrypt

# App durch Passwort schützen
password = 1234

#Hier kann das Passwort nicht gehasht werden, da es sich so vor der Eingabe verändert = falsches Passwort

#Anmeldeversuche zählen
anmeldeversuche = 0
password_input = int(input("Bitte geben Sie ihr Passwort ein:"))
while password != password_input:
    anmeldeversuche = anmeldeversuche + 1

    anmeldeversuche = int(anmeldeversuche)
    if anmeldeversuche == 3:
        print("zu viele fehlerhafte Anmeldungen")
        sys.exit(1)

    password_input = int(input("Falsches Passwort, versuchen Sie es nochmals:"))
else:
    print("Erfolgreich eingeloggt")
    print("")


# Passwort hashen --> noch zu implementieren
#bytes = password.encode('utf-8')
#salt = bcrypt.gensalt()
#hash = bcrypt.hashpw(bytes, salt)
#print(hash) 

# Passwort hashen --> wahrscheinlich nach der Passwortänderung implementieren
#es könnte auch sinnvoll sein, das Passwort in einem seperaten File zu hashen und zu speichern. Bei der Änderung wird das Passwort dort entschlüsselt, überschrieben und wieder gehasht.
password = str(password).encode('utf-8')
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
returned_hash = bcrypt.hashpw(password, hashed)
