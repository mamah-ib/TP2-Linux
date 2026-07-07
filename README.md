# TP2 Linux : Administration Systeme et Ordonnancement

**Etudiant :** Mamah
**Cours :** LIU 2026 - Introduction aux Systemes d'Exploitation

## Description
Ce depot contient les 6 exercices du TP2, couvrant la gestion des utilisateurs,
des processus, des algorithmes d'ordonnancement, l'automatisation par scripts
Bash, la surveillance systeme et la planification via cron.

## Structure du depot

### Exercice 1 : Gestion des utilisateurs et groupes
Creation des utilisateurs etudiant1/etudiant2, creation du groupe projet_linux,
gestion du repertoire partage /data/commun avec permissions 770.

### Exercice 2 : Gestion des processus
Lancement de 5 processus en arriere-plan, analyse des threads avec ps -eLf,
modification de priorite avec renice.

### Exercice 3 : Algorithmes d'ordonnancement
Implementation en Python des algorithmes FCFS (non-preemptif) et Round Robin
(preemptif, quantum=2), avec calcul du temps d'attente moyen.

### Exercice 4 : Scripts Bash
Scripts bash interactifs utilisant read, echo, date et ls.

### Exercice 5 : Surveillance systeme
Utilisation de top, ps -ef et kill pour surveiller et gerer les processus.

### Exercice 6 : Maintenance automatisee
Script rapport_sys.sh generant un rapport systeme (date, nombre de processus,
espace disque) avec detection de charge CPU elevee, et planification via cron.

## Methodologie
Chaque commande executee a ete enregistree via la commande `script`, produisant
un fichier .log par exercice avec l'historique complet des commandes et de
leurs sorties.
