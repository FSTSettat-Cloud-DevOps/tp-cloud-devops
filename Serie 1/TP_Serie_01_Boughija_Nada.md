# Cloud Computing & DevOps
## Série 1 --- Caractéristiques du Cloud et étude de cas de migration

**Master Sciences et Techniques** | Faculté des Sciences et Techniques de Settat  
**Enseignant :** Pr. A. Abassi  

---

### 👤 Informations du Binôme

* **Étudiant 1 :** [BOUGHIJA, NADA, E138193253]
* **Étudiant 2 :** [JEMI, MERIEM, E132132754]
* **Groupe :** [IRISTI]
* **Lien du dépôt GitHub :** [URL du dépôt monorepo]

---

## Fiche Synthèse

| Fiche Synthèse | Informations |
| :--- | :--- |
| **Chapitre associé** | Ch. 1 --- Introduction au Cloud Computing |
| **Durée** | 2 h : TD 45 min, TP 65 min, bilan 10 min |
| **Objectifs** | Identifier les caractéristiques d'une architecture Cloud ; distinguer scalabilité, élasticité et disponibilité ; choisir un modèle de déploiement ; quantifier l'intérêt de l'élasticité. |
| **Prérequis** | Notions de base du cours (définition NIST, modèles de déploiement), Python 3. |

---

## Partie A --- TD (45 min)

### Exercice 1 --- Les caractéristiques essentielles du Cloud

Pour chaque situation, indiquer la caractéristique du Cloud illustrée (*libre-service à la demande, accès réseau étendu, mutualisation des ressources, élasticité rapide, service mesuré*) :

* **(a)** Un étudiant crée une machine virtuelle en 2 minutes depuis une console web, sans contacter le fournisseur.
* **(b)** La facture du mois indique 312 heures de calcul et 40 Go de stockage consommés.
* **(c)** Le service est accessible depuis un téléphone, une tablette ou un PC via HTTPS.
* **(d)** Le nombre de serveurs passe de 2 à 10 pendant les inscriptions puis redescend automatiquement.
* **(e)** Plusieurs clients différents partagent le même parc physique sans voir les données des autres.

> **Réponse Exercice 1 :**
> * **(a)** Libre-service à la demande.
> * **(b)** Service mesuré.
> * **(c)** Accès réseau étendu.
> * **(d)** Élasticité rapide.
> * **(e)** Mutualisation des ressources.

---

### Exercice 2 --- Scalabilité, élasticité, disponibilité

Associer chaque énoncé au concept le plus adapté et justifier :

* **(a)** « Nous pouvons passer de 1 000 à 100 000 utilisateurs en ajoutant des machines. »
* **(b)** « Les ressources s'ajustent automatiquement à la charge, en montée comme en descente. »
* **(c)** « Le service répond 99,95 % du temps, même en cas de panne d'un serveur. »
* **(d)** Expliquer la différence entre *scalabilité verticale* (scale up) et *horizontale* (scale out) avec un exemple.

> **Réponse Exercice 2 :**
> * **(a)** **Scalabilité.** Le système peut prendre en charge davantage d'utilisateurs en ajoutant des machines.
> * **(b)** **Élasticité.** Le système ajoute automatiquement des ressources quand la charge augmente et les retire quand elle diminue.
> * **(c)** **Disponibilité.** Le taux de 99,95 % représente la proportion du temps pendant laquelle le service répond. En cas de panne, un autre serveur peut prendre le relais.
> * **(d)** La **scalabilité verticale** (*scale up*) augmente les ressources d'une même machine, par exemple en passant de 8 à 16 Go de RAM. La **scalabilité horizontale** (*scale out*) ajoute des machines, par exemple en passant de 1 à 3 serveurs derrière un répartiteur de charge.

---

### Exercice 3 --- Choisir un modèle de déploiement

Pour chaque organisation, proposer un modèle (*public, privé, hybride, communautaire*) et justifier en deux lignes :

* **(a)** Une startup de 3 personnes qui lance une application mobile.
* **(b)** Une faculté : données des étudiants sensibles, mais fortes pointes de charge lors des inscriptions.
* **(c)** Une banque soumise à une réglementation stricte sur la localisation des données.
* **(d)** Un consortium d'universités marocaines qui mutualise une plateforme de calcul pour la recherche.

> **Réponse Exercice 3 :**
> * **(a)** **Cloud public.** La startup peut lancer son application rapidement avec peu d'investissement initial. Elle paie selon sa consommation et augmente ses ressources si le nombre d'utilisateurs grandit.
> * **(b)** **Cloud hybride.** La faculté conserve les données sensibles dans un Cloud privé. Elle utilise des ressources du Cloud public pour absorber les pics des services qui peuvent y être hébergés.
> * **(c)** **Cloud privé.** La banque peut contrôler la localisation de ses données et de ses sauvegardes. Elle choisit des centres de données qui respectent les exigences réglementaires applicables.
> * **(d)** **Cloud communautaire.** Les universités partagent une plateforme réservée aux membres du consortium. Elles mutualisent les coûts et fixent des règles communes d'accès et de sécurité.

---

### Exercice 4 --- Étude de cas : migration de « ScolaNet »

L'application ScolaNet gère la scolarité de 2 000 étudiants. Elle tourne sur un serveur physique unique (8 cœurs, 32 Go de RAM) avec une base PostgreSQL sur la même machine. Le trafic est multiplié par 10 en septembre. L'an dernier, une panne matérielle a provoqué 2 jours d'indisponibilité. Le budget d'investissement est limité.

1. Lister les problèmes de l'architecture actuelle.
2. Proposer une stratégie de migration (*rehost, replatform, refactor*) et la justifier.
3. Identifier trois risques de la migration et une mesure d'atténuation pour chacun.
4. Proposer un plan de migration en quatre phases.

> **Réponse Exercice 4 :**
>
> **1. Problèmes de l'architecture actuelle :**
> * Le serveur physique unique est un point de défaillance unique. Une panne arrête à la fois l'application et la base de données.
> * L'application et PostgreSQL partagent les mêmes ressources. En période de forte charge, elles peuvent se concurrencer pour le CPU, la RAM et les accès disque.
> * La capacité du serveur est fixe. Le pic de septembre peut provoquer une saturation, tandis qu'un achat de matériel dimensionné pour ce pic augmente l'investissement initial.
>
> **2. Stratégie de migration recommandée et justification :**
> * **Replatform.** Déployer l'application sur des instances Cloud derrière un répartiteur de charge et migrer la base vers un service PostgreSQL managé. Cette stratégie limite les modifications du code, sépare l'application de sa base et permet d'ajuster le nombre d'instances selon la charge. Une configuration redondante améliore la disponibilité, avec des coûts à estimer avant la migration.
>
> **3. Risques et mesures d'atténuation :**
> * **Risque 1 :** Perte ou corruption des données pendant le transfert.
>   * *Atténuation :* Effectuer une sauvegarde complète, tester sa restauration et vérifier l'intégrité des données migrées.
> * **Risque 2 :** Indisponibilité du service pendant la bascule.
>   * *Atténuation :* Synchroniser les données avant la bascule, choisir une période de faible trafic et préparer un plan de retour arrière.
> * **Risque 3 :** Accès non autorisé aux données des étudiants.
>   * *Atténuation :* Placer PostgreSQL sur un réseau privé, limiter les accès et chiffrer les données pendant leur transfert et leur stockage.
>
> **4. Plan de migration en 4 phases :**
> * **Phase 1 :** Auditer l'existant. Recenser les dépendances, mesurer la charge et définir les besoins de disponibilité, de sécurité et de budget.
> * **Phase 2 :** Préparer l'environnement Cloud. Configurer le réseau privé, PostgreSQL managé, le répartiteur de charge et la supervision.
> * **Phase 3 :** Réaliser une migration de test. Restaurer une copie de la base et vérifier le fonctionnement de l'application, les performances sous une charge de pointe et le plan de retour arrière.
> * **Phase 4 :** Basculer en production hors période de pointe après la synchronisation finale. Vérifier le service, puis surveiller les performances et les coûts.

---

## Partie B --- TP (65 min) : mesurer l'élasticité

### Étape 1 --- Inventaire des ressources de la machine

Relever les ressources de votre poste de travail :

* **Sous Linux / WSL :** `lscpu`, `free -h`, `df -h /`, `ip -br a`
* **Sous Windows (PowerShell) :** `Get-CimInstance Win32_Processor`, `Get-CimInstance Win32_OperatingSystem`, `Get-PSDrive C`

> **Ressources relevées sur votre poste :**
>
> | Ressource | Valeur mesurée |
> | :--- | :--- |
> | **Nombre de cœurs CPU** | 4 cœurs physiques (8 processeurs logiques) |
> | **RAM Totale** |Environ 7,85 Gio visibles par Windows |
> | **Espace disque libre (/ ou C:)** |	18,99 Go|
> | **Adresse(s) IP** |Wi-Fi : 10.223.249.83/24 ; Ethernet : 192.168.1.200/24|

---

### Étape 2 --- Simulation : infrastructure statique ou élastique

Créer et exécuter le fichier `sim_elasticite.py` dans le même dossier :

```python
import math

charge = [120, 80, 60, 50, 50, 70, 150, 300, 520, 640, 700, 680,
          600, 620, 650, 700, 560, 400, 300, 250, 200, 180, 150, 130]
CAP = 100     # requetes/s supportees par un serveur
PRIX = 0.5    # euros par serveur-heure

statique = math.ceil(max(charge) / CAP)           # dimensionne pour le pic
h_statique = statique * len(charge)
h_elastique = sum(math.ceil(c / CAP) for c in charge)

print("Serveurs (statique)      :", statique)
print("Serveur-heures statique  :", h_statique, "->", h_statique * PRIX, "EUR")
print("Serveur-heures elastique :", h_elastique, "->", h_elastique * PRIX, "EUR")
print("Economie : %.1f %%" % (100 * (1 - h_elastique / h_statique)))
```


> L'infrastructure statique mobilise 7 serveurs pendant 24 heures pour couvrir le pic de 700 requêtes/s. L'infrastructure élastique ajuste le nombre de serveurs chaque heure, ce qui permet d'économiser **39 € sur la journée simulée**.
