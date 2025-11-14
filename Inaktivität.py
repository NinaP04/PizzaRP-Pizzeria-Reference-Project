#nach x Sekunden von Inaktivität wird der User automatisch ausgeloggt
import time


#schauen, ob das untere eine gute Lösung ist --> noch zu überprüfen
def auto_logout(inactivity_time):
    time.sleep(inactivity_time)
    print("Sie wurden aufgrund von Inaktivität automatisch ausgeloggt.")
