#!/bin/bash
echo "=== Rapport systeme ===" > systeme.log
date >> systeme.log

echo "" >> systeme.log
echo "Nombre de processus en cours:" >> systeme.log
ps -e --no-headers | wc -l >> systeme.log

echo "" >> systeme.log
echo "Espace disque disponible:" >> systeme.log
df -h / >> systeme.log

charge=$(uptime | awk -F'load average:' '{print $2}' | awk -F, '{print $1}' | tr -d ' ')
seuil="1.0"
if (( $(echo "$charge > $seuil" | bc -l) )); then
    echo "Attention : Forte charge CPU detectee !"
fi
