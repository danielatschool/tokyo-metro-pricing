import math

def berechne_fahrpreis(strecke):
    if strecke <= 6:
        return 170
    elif strecke <= 11:
        return 200
    elif strecke <= 19:
        return 250
    elif strecke <= 27:
        return 290
    else:
        return 320

def berechne_kinderpreis(erwachsenenpreis):
    kinderpreis = erwachsenenpreis / 2
    return math.ceil(kinderpreis / 10) * 10
    
strecke = int(input("Bitte geben Sie die Strecke in Kilometern ein: "))
erwachsenenpreis = berechne_fahrpreis(strecke)
kinderpreis = berechne_kinderpreis(erwachsenenpreis)

print(f"Der Fahrpreis für {strecke} km beträgt:")
print(f"Erwachsene: {erwachsenenpreis} Yen")
print(f"Kinder: {kinderpreis} Yen")