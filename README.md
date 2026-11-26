# Freilichtbühne Waldblick

## Aufgaben & Kontext
1. Beschreiben Sie die Anforderungen an eine eingesetzte Datenstruktur für den Fall.
	Gehen Sie dabei unter anderem darauf ein, welche Eigenschaften die Daten haben und wie sie effizient angeordnet werden können.
2. Wählen Sie eine passende Datenstruktur aus und begründen Sie Ihre Entscheidung. Erläutern Sie auch kurz, warum andere Datenstrukturen hier weniger geeignet wären.
3. Implementieren Sie eine Lösung in Python. Die Umsetzung kann als Konsolenprogramm oder mit einer einfachen grafischen Oberfläche erfolgen.

Sie unterstützen die kleine, unabhängige Freilichtbühne Waldblick bei der Entwicklung für ein Modul zur Verwaltung der Sitzplatzbelegung.
Der Zuschauerbereich besteht aus mehreren Sitzreihen mit jeweils einer festen Anzahl an Sitzplätzen. Jeder Sitzplatz ist eindeutig über Reihe und Sitznummer identifizierbar, zum Beispiel Reihe 3, Platz 12.
Die Anwendung soll die aktuelle Belegung der Plätze  verwalten und so bei der Buchung an der Abendkasse unterstützen. Sitzplätze können im Rahmen des Ticketverkaufs als frei oder belegt markiert werden. 
Dabei sollen einzelne Plätze gezielt ausgewählt und gebucht werden können. 


## Aufgabe 1: Anforderungen und Effizienz

- Für den gegebenen Fall lässt sich die Situation gut mit einer Dictionary lösen
- Eine Dictionary wäre sinnvoll, da sich Reihen und Plätze nicht wiederholen
  - Somit bräuchte man eine Nested Dictionary, um für jede Reihe, eine weitere Dictionary and Platznummer und Name der Person

  - Für die Belegung benutzt man ein einfaches Enum mit "Frei" oder "Belegt"

## Aufgabe 2: Datenstruktur

- Hier eignet es sicher eine Dictionary zu nutzen
- Reihen und Platznummern in einer Reihe wiederholen sich nicht
  - Somit kann man sie als Keys verwenden
- Dynamische Datenstrukuren, wie Listen, Queues oder Stacks sind weniger sinnvoll wegen der Traversierung oder Navigation
  - Ist möglich aber nicht effizient
- Statische Datenstrukturen wie Arrays oder Hashmaps könnten möglicherweise passen
  - Problem ist, weil es eine Outdoorveranstaltung ist, soll man recht flexibel bleiben mit Reihen hinzufügen oder wegnehmen (Je nach Sitzplatzbelegung)
