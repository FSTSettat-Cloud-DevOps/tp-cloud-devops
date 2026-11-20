# Compte Rendu — Série 01
## Virtualisation & Cloud Computing

### Partie B — TP : Mesurer l'élasticité

## Étape 1 : Inventaire des ressources

Nous avons utilisé Windows PowerShell pour identifier les ressources de notre ordinateur.

### Résultats obtenus

- Processeur : Intel Core i5-8250U @ 1.60 GHz
- Nombre de cœurs : 4
- Processeurs logiques : 8
- Mémoire RAM totale : 8 Go
- Espace disque utilisé : 217,75 Go
- Espace disque libre : 18,99 Go
- Adresse IPv4 Ethernet : 192.168.1.200

## Étape 2 : Simulation de l'élasticité

Nous avons exécuté le programme Python sim_elasticite.py afin de comparer une infrastructure statique et une infrastructure élastique.

### Résultats sans marge de sécurité

- Serveurs statiques : 7
- Serveur-heures statique : 168
- Coût statique : 84 EUR
- Serveur-heures élastique : 90
- Coût élastique : 45 EUR
- Économie réalisée : 46,4 %

## Étape 3 : Analyse et variantes

### 1. Économie réalisée

L'infrastructure élastique permet une économie de 39 EUR, soit 46,4 % par rapport à l'infrastructure statique.

### 2. Avec une marge de sécurité de 20 %

- Serveurs statiques : 9
- Serveur-heures statique : 216
- Coût statique : 108 EUR
- Serveur-heures élastique : 108
- Coût élastique : 54 EUR
- Économie réalisée : 50 %

### 3. Limites du modèle

Le modèle ne prend pas en compte le temps de démarrage des serveurs ni les variations imprévues de la charge.

## Conclusion

L'infrastructure élastique est plus rentable lorsque la charge varie au cours du temps.

Elle permet d'adapter automatiquement les ressources aux besoins réels et de réduire les coûts.

L'infrastructure statique est plus adaptée lorsque la charge reste constante.
## Réponse à la question finale

### Pour quel type de charge le Cloud est-il le plus rentable ?

Le Cloud est plus rentable lorsque la charge varie au cours du temps.
Il permet d'adapter automatiquement les ressources selon les besoins.
Pendant les périodes de faible activité, les serveurs inutiles sont arrêtés.
Cela permet de réduire les coûts d'exploitation.
Ainsi, le Cloud est particulièrement avantageux pour les applications ayant des pics de trafic.
