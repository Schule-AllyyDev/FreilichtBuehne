from enum import Enum
from typing import Dict


# Enum für die Belegung der Sitzplätze
class Belegung(Enum):
    Frei = 0
    Belegt = 1

# Dictionary zur Speicherung der Sitzplatzbelegung
sitzplaetze: Dict[int, Dict[int, Belegung]] = {}

def menu():
    print("==== Sitzplatzverwaltung ====")
    print("1. Sitzplatz belegen")
    print("2. Freie Sitzplätze anzeigen")
    print("3. Belegung anzeigen")
    print("4. Alle Sitzplätze anzeigen")
    print("5. Beenden")


def get_plaetze(belegung: Belegung) -> list[tuple[int, int]]:
    plaetze = []
    for reihe, plaetze_in_reihe in sitzplaetze.items():
        for platz, plaetzung in plaetze_in_reihe.items():
            if plaetzung == belegung:
                plaetze.append((reihe, platz))
    return plaetze

def main():
    # Input für Reihen und Plätze
    reihen = int(input("Geben Sie die Anzahl der Reihen ein: "))
    plaetze = int(input("Geben Sie die Anzahl der Plätze pro Reihe ein: "))

    # Initialisierung der Sitzplätze
    for i in range(reihen):
        sitzplaetze[i] = {}
        for j in range(plaetze):
            sitzplaetze[i][j] = Belegung.Frei

    while True:
        menu()
        auswahl = int(input("Wählen Sie eine Option: "))

        match auswahl:
            # Sitzplatz belegen
            case 1:   
                freie_plaetze = get_plaetze(Belegung.Frei)
                if not freie_plaetze:
                    print("Keine freien Sitzplätze verfügbar.")
                    continue

                ausgewaehlte_reihe = int(input("Geben Sie die Reihe ein (0-{}): ".format(reihen - 1)))
                ausgewaehlter_sitzplatz = int(input("Geben Sie den Sitzplatz ein (0-{}): ".format(plaetze - 1)))

                # Gültigkeit der Eingabe überprüfen und Sitzplatz belegen
                if (ausgewaehlte_reihe, ausgewaehlter_sitzplatz) in freie_plaetze:
                    sitzplaetze[ausgewaehlte_reihe][ausgewaehlter_sitzplatz] = Belegung.Belegt
                    print(f"Sitzplatz Reihe {ausgewaehlte_reihe}, Platz {ausgewaehlter_sitzplatz} wurde belegt.")
                else:
                    print("Ungültige Eingabe oder Sitzplatz bereits belegt.")
            
            # Freie Sitzplätze anzeigen
            case 2:
                freie_plaetze = get_plaetze(Belegung.Frei)
                if not freie_plaetze:
                    print("Keine freien Sitzplätze verfügbar.")
                else:
                    print("Verfügbare freie Sitzplätze:")
                    for reihe, platz in freie_plaetze:
                        print(f"Reihe {reihe+1}, Platz {platz+1}")

            # Belegung anzeigen
            case 3:
                belegte_plaetze = get_plaetze(Belegung.Belegt)
                if not belegte_plaetze:
                    print("Alle Sitzplätze sind frei.")
                else:
                    print("Belegte Sitzplätze:")
                    for reihe, platz in belegte_plaetze:
                        print(f"Reihe {reihe+1}, Platz {platz+1}")
                pass

            # Alle Sitzplätze anzeigen
            case 4:
                print("Alle Sitzplätze:")
                for reihe, plaetze in sitzplaetze.items():
                    for platz, belegung in plaetze.items():
                        status = "Belegt" if belegung == Belegung.Belegt else "Frei"   
                        print(f"Reihe {reihe+1}, Platz {platz+1}: {status}")
                    print("==========================")
                pass

            # Beenden
            case 5:
                break


if __name__ == "__main__":
    main()