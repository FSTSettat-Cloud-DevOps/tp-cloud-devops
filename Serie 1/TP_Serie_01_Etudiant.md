# Cloud Computing & DevOps
## Série 1 --- Caractéristiques du Cloud et étude de cas de migration
**Master Sciences et Techniques** | Faculté des Sciences et Techniques de Settat  
**Enseignant :** Pr. A. Abassi  

---

### 👤 Informations du Binôme
* **Étudiant 1 :** [Nom, Prénom, CNE]
* **Étudiant 2 :** [Nom, Prénom, CNE]
* **Groupe :** [Groupe]
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
> * **(a)** 
> * **(b)** 
> * **(c)** 
> * **(d)** 
> * **(e)** 

---

### Exercice 2 --- Scalabilité, élasticité, disponibilité

Associer chaque énoncé au concept le plus adapté et justifier :

* **(a)** « Nous pouvons passer de 1 000 à 100 000 utilisateurs en ajoutant des machines. »
* **(b)** « Les ressources s'ajustent automatiquement à la charge, en montée comme en descente. »
* **(c)** « Le service répond 99,95 % du temps, même en cas de panne d'un serveur. »
* **(d)** Expliquer la différence entre *scalabilité verticale* (scale up) et *horizontale* (scale out) avec un exemple.

> **Réponse Exercice 2 :**
> * **(a)** 
> * **(b)** 
> * **(c)** 
> * **(d)** 

---

### Exercice 3 --- Choisir un modèle de déploiement

Pour chaque organisation, proposer un modèle (*public, privé, hybride, communautaire*) et justifier en deux lignes :

* **(a)** Une startup de 3 personnes qui lance une application mobile.
* **(b)** Une faculté : données des étudiants sensibles, mais fortes pointes de charge lors des inscriptions.
* **(c)** Une banque soumise à une réglementation stricte sur la localisation des données.
* **(d)** Un consortium d'universités marocaines qui mutualise une plateforme de calcul pour la recherche.

> **Réponse Exercice 3 :**
> * **(a)** 
> * **(b)** 
> * **(c)** 
> * **(d)** 

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
> * 
>
> **2. Stratégie de migration recommandée et justification :**
> * 
>
> **3. Risques et mesures d'atténuation :**
> * **Risque 1 :** 
>   * *Atténuation :* 
> * **Risque 2 :** 
>   * *Atténuation :* 
> * **Risque 3 :** 
>   * *Atténuation :* 
>
> **4. Plan de migration en 4 phases :**
> * **Phase 1 :** 
> * **Phase 2 :** 
> * **Phase 3 :** 
> * **Phase 4 :** 

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
> | **Nombre de cœurs CPU** | |
> | **RAM Totale** | |
> | **Espace disque libre (/ ou C:)** | |
> | **Adresse(s) IP** | |

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
