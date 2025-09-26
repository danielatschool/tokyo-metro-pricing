import math  # Importiere das math-Modul für mathematische Funktionen

# Berechnet den Fahrpreis basierend auf der zurückgelegten Strecke
def berechne_fahrpreis(strecke):
    # Wenn die Strecke kleiner oder gleich 6 km ist, beträgt der Fahrpreis 170 Yen
    if strecke <= 6:
        return 170
    # Wenn die Strecke zwischen 7 und 11 km liegt, beträgt der Fahrpreis 200 Yen
    elif strecke <= 11:
        return 200
    # Wenn die Strecke zwischen 12 und 19 km liegt, beträgt der Fahrpreis 250 Yen
    elif strecke <= 19:
        return 250
    # Wenn die Strecke zwischen 20 und 27 km liegt, beträgt der Fahrpreis 290 Yen
    elif strecke <= 27:
        return 290
    # Für Strecken über 27 km beträgt der Fahrpreis 320 Yen
    else:
        return 320

# Berechnet den Kinderpreis aus dem Preis der Erwachsenen, abgerundet auf das nächste Zehnfache
def berechne_kinderpreis(erwachsenenpreis):
    # Kinder zahlen die Hälfte des Erwachsenentarifs
    kinderpreis = erwachsenenpreis / 2
    # Rundet den Preis auf das nächste Zehnfache
    return math.ceil(kinderpreis / 10) * 10

# Fordert den Benutzer auf, die Strecke in Kilometern einzugeben
strecke = int(input("Bitte geben Sie die Strecke in Kilometern ein: "))
# Ermittelt den Fahrpreis für Erwachsene basierend auf der eingegebenen Strecke
erwachsenenpreis = berechne_fahrpreis(strecke)
# Berechnet den Preis für Kinder
kinderpreis = berechne_kinderpreis(erwachsenenpreis)

# Gibt den berechneten Fahrpreis aus
print(f"Der Fahrpreis für {strecke} km beträgt:")
print(f"Erwachsene: {erwachsenenpreis} Yen")
print(f"Kinder: {kinderpreis} Yen")