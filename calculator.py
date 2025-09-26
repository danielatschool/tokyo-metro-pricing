import math

def berechne_fahrpreis(strecke):
    if strecke <= 6:
        return 170  # Bis 6 km
    elif strecke <= 11:
        return 200  # 7-11 km
    elif strecke <= 19:
        return 250  # 12-19 km
    elif strecke <= 27:
        return 290  # 20-27 km
    else:
        return 320  # Über 27 km

def berechne_kinderpreis(erwachsenenpreis):
    kinderpreis = erwachsenenpreis / 2
    return math.ceil(kinderpreis / 10) * 10

def main():
    # Benutzer zur Eingabe der Strecke (in Kilometern) auffordern
    strecke = int(input("Bitte geben Sie die Strecke (in km) ein: "))

    # Fahrpreise berechnen
    erwachsenenpreis = berechne_fahrpreis(strecke)
    kinderpreis = berechne_kinderpreis(erwachsenenpreis)

    # Ergebnisse ausgeben
    print(f"Der Fahrpreis für {strecke} km beträgt:")
    print(f"Erwachsene: {erwachsenenpreis} Yen")
    print(f"Kinder: {kinderpreis} Yen")

if __name__ == '__main__':
    main()