#!/usr/bin/env python3
processus = [
    {"id": "P1", "arrivee": 0, "burst": 5},
    {"id": "P2", "arrivee": 1, "burst": 3},
    {"id": "P3", "arrivee": 2, "burst": 8},
    {"id": "P4", "arrivee": 3, "burst": 6},
]

processus.sort(key=lambda p: p["arrivee"])

temps_actuel = 0
total_attente = 0

print("ID    Arrivee   Burst   Debut   Fin   Rotation   Attente")

for p in processus:
    debut = max(temps_actuel, p["arrivee"])
    fin = debut + p["burst"]
    rotation = fin - p["arrivee"]
    attente = rotation - p["burst"]
    total_attente += attente
    temps_actuel = fin
    print(p["id"], p["arrivee"], p["burst"], debut, fin, rotation, attente)

moyenne_attente = total_attente / len(processus)
print("Temps d'attente moyen (FCFS):", round(moyenne_attente, 2))
