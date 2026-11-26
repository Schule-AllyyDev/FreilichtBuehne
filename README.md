# Freilichtbühne Waldblick

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
