processus = [
    {"id": "P1", "arrivee": 0, "burst": 5, "restant": 5},
    {"id": "P2", "arrivee": 1, "burst": 3, "restant": 3},
    {"id": "P3", "arrivee": 2, "burst": 8, "restant": 8},
    {"id": "P4", "arrivee": 3, "burst": 6, "restant": 6},
]

quantum = 2
temps = 0
file_attente = []
termine = {}
sequence = []
restants = {p["id"]: p["burst"] for p in processus}
arrivees = sorted(processus, key=lambda p: p["arrivee"])
index_arrivee = 0
file_attente.append(arrivees[0]["id"])
index_arrivee = 1
ids = {p["id"]: p for p in processus}

while file_attente:
    pid = file_attente.pop(0)
    p = ids[pid]
    execution = min(quantum, restants[pid])
    sequence.append((pid, temps, temps + execution))
    temps += execution
    restants[pid] -= execution

    while index_arrivee < len(arrivees) and arrivees[index_arrivee]["arrivee"] <= temps:
        file_attente.append(arrivees[index_arrivee]["id"])
        index_arrivee += 1

    if restants[pid] > 0:
        file_attente.append(pid)
    else:
        termine[pid] = temps

print("Sequence d'execution (Round Robin, quantum=2):")
for pid, debut, fin in sequence:
    print(pid, ": de", debut, "a", fin)

print()
print("Temps de fin de chaque processus:")
for p in processus:
    print(p["id"], ":", termine[p["id"]])
