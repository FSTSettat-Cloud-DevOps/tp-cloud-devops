# TP — Série 3 : Simulation d’une infrastructure Cloud locale

**Module :** Cloud Computing & DevOps — Master Sciences et Techniques  
**Établissement :** FST de Settat — Université Hassan I  
**Enseignant :** Pr. A. ABASSI  
**Durée :** TD 30 min · TP 80 min · Bilan 10 min

> **Consigne :** Complétez ce document Markdown directement. Ajoutez les commandes exécutées, les résultats observés et des captures d’écran lorsque cela est demandé. Remplacez les zones `À compléter` par vos réponses. Ne mettez jamais de vrais mots de passe ou de secrets dans un dépôt Git public.

## Informations de l’étudiant

- **Nom et prénom :** À compléter
- **Groupe / binôme :** À compléter
- **Date :** À compléter
- **Système hôte :** À compléter
- **Version de VirtualBox :** À compléter
- **État initial de la VM `base` :** À compléter

---

# Partie A — TD (30 min)

## Exercice 1 — Plan d’adressage

Le réseau privé `192.168.56.0/24` doit être découpé en quatre sous-réseaux de même taille : Web, base de données, supervision et réserve.

### 1. Masque et nombre d’hôtes

- **Masque à utiliser :** À compléter
- **Notation CIDR :** À compléter
- **Nombre total d’adresses par sous-réseau :** À compléter
- **Nombre d’adresses utilisables par sous-réseau :** À compléter
- **Explication du calcul :** À compléter

### 2. Découpage du réseau

Complétez le tableau.

| Usage | Adresse réseau / CIDR | Première adresse utilisable | Dernière adresse utilisable | Adresse de diffusion |
|---|---|---|---|---|
| Web | À compléter | À compléter | À compléter | À compléter |
| Base de données | À compléter | À compléter | À compléter | À compléter |
| Supervision | À compléter | À compléter | À compléter | À compléter |
| Réserve | À compléter | À compléter | À compléter | À compléter |

### 3. Adresses des machines virtuelles

- **Adresse proposée pour `web` dans le découpage :** À compléter
- **Adresse proposée pour `db` dans le découpage :** À compléter
- **Pourquoi ces adresses sont-elles valides ?** À compléter

Dans les manipulations du TP, le réseau `192.168.56.0/24` est conservé pour simplifier la configuration. Les adresses prévues sont `web = 192.168.56.12` et `db = 192.168.56.13`.

---

## Exercice 2 — Stockage et Infrastructure as Code

### 1. Avantages d’un script d’infrastructure

Citez et expliquez **deux avantages** à décrire une infrastructure dans un script plutôt que de la créer manuellement.

1. **Avantage 1 :** À compléter  
   **Explication :** À compléter

2. **Avantage 2 :** À compléter  
   **Explication :** À compléter

### 2. Clone complet et clone lié

| Critère | Clone complet | Clone lié |
|---|---|---|
| Principe de stockage | À compléter | À compléter |
| Espace disque utilisé | À compléter | À compléter |
| Dépendance au disque parent | À compléter | À compléter |
| Avantage principal | À compléter | À compléter |
| Limite principale | À compléter | À compléter |

---

# Partie B — TP (80 min)

## Étape 1 — Clonage et configuration des machines virtuelles

### 1. Vérifier la VM de référence

Indiquez les commandes utilisées pour vérifier que la VM `base` existe et que l’instantané `base-propre` est disponible.

```bash
# Commandes exécutées :
À compléter
```

**Résultat observé :** À compléter

### 2. Créer les clones

Les commandes proposées dans le sujet sont :

```bash
VBoxManage clonevm base --name web --register
VBoxManage clonevm base --name db --register

VBoxManage startvm web --type headless
VBoxManage startvm db --type headless
```

- **La création du clone `web` a-t-elle réussi ?** Oui / Non
- **La création du clone `db` a-t-elle réussi ?** Oui / Non
- **Messages ou erreurs éventuels :** À compléter
- **Comment avez-vous vérifié que les VM sont enregistrées ?** À compléter

> Avant de démarrer les clones simultanément, vérifiez les paramètres réseau et les adresses MAC. Chaque machine doit avoir un nom d’hôte, une adresse IP et un identifiant système adaptés.

### 3. Configurer la VM `web`

- **Commande utilisée pour définir le nom d’hôte :**
  ```bash
  À compléter
  ```
- **Nom d’hôte obtenu :** À compléter
- **Nom du fichier Netplan utilisé :** À compléter
- **Adresse IP configurée :** À compléter

Commandes de vérification :

```bash
hostname
ip -br address
```

**Résultats observés :**

```text
À compléter
```

Décrivez brièvement les modifications effectuées pour réinitialiser l’identifiant système (`machine-id`) et redémarrer la VM.

**Réponse :** À compléter

### 4. Configurer la VM `db`

- **Commande utilisée pour définir le nom d’hôte :**
  ```bash
  À compléter
  ```
- **Nom d’hôte obtenu :** À compléter
- **Nom du fichier Netplan utilisé :** À compléter
- **Adresse IP configurée :** À compléter

Commandes de vérification :

```bash
hostname
ip -br address
```

**Résultats observés :**

```text
À compléter
```

### 5. Vérifier la connectivité entre `web` et `db`

Depuis la VM `web`, exécutez :

```bash
ping -c 2 192.168.56.13
```

- **Le test a-t-il réussi ?** Oui / Non
- **Nombre de paquets transmis / reçus :** À compléter
- **Interprétation du résultat :** À compléter

**Si le test échoue, quelles vérifications effectuez-vous ?**

À compléter.

**Preuve / capture d’écran :** Ajoutez ici une capture du test `ping`, ou indiquez le nom du fichier image ajouté au dépôt.

---

## Étape 2 — Installer et tester le serveur Web Nginx

Sur la VM `web`, exécutez les commandes du sujet pour installer Nginx, créer une page HTML et démarrer le service.

### 1. Installation

```bash
sudo apt-get update
sudo apt-get install -y nginx
```

- **L’installation a-t-elle réussi ?** Oui / Non
- **Messages ou difficultés rencontrés :** À compléter

### 2. Créer la page Web

Commande utilisée :

```bash
À compléter
```

- **Contenu de la page créée :** À compléter
- **Emplacement du fichier HTML :** À compléter

### 3. Vérifier le service

Commandes :

```bash
sudo systemctl enable --now nginx
sudo systemctl status nginx --no-pager
```

- **État du service Nginx :** À compléter
- **Comment interprétez-vous cet état ?** À compléter

Depuis la machine hôte, tester si l’adresse IP est accessible :

```bash
curl http://192.168.56.12
```

- **Résultat renvoyé par `curl` :**
  ```text
  À compléter
  ```
- **Le contenu obtenu correspond-il à la page créée ?** Oui / Non
- **Conclusion :** À compléter

**Preuve / capture d’écran :** Ajoutez une capture de la page ou du résultat de `curl`.

---

## Étape 3 — Installer et configurer PostgreSQL

Les manipulations suivantes sont réalisées sur la VM `db`.

### 1. Installation et création des objets

Commandes exécutées pour installer PostgreSQL :

```bash
À compléter
```

Le TP demande de créer l’utilisateur `appuser` et la base `appdb`.

- **Commande de création de l’utilisateur :**
  ```bash
  À compléter
  ```
- **Commande de création de la base de données :**
  ```bash
  À compléter
  ```
- **La base appartient-elle à `appuser` ?** Oui / Non
- **Comment l’avez-vous vérifié ?** À compléter

> Le mot de passe d’exemple du sujet est réservé au TP. N’utilisez pas ce mot de passe dans un environnement réel et ne publiez aucun secret dans Git.

### 2. Autoriser les connexions réseau

Indiquez les chemins des fichiers de configuration obtenus avec les commandes suivantes :

```bash
sudo -u postgres psql -tAc "SHOW config_file;"
sudo -u postgres psql -tAc "SHOW hba_file;"
```

- **Chemin de `postgresql.conf` :** À compléter
- **Chemin de `pg_hba.conf` :** À compléter

Dans `postgresql.conf` :

- **Valeur configurée pour `listen_addresses` :** À compléter
- **Pourquoi cette directive est-elle importante ?** À compléter

Dans `pg_hba.conf`, le sujet propose une règle pour autoriser `appuser` à accéder à `appdb` depuis le réseau du TP.

- **Règle ajoutée :**
  ```text
  À compléter
  ```
- **Que signifient les champs de cette règle ?** À compléter

### 3. Redémarrer et vérifier PostgreSQL

Commandes utilisées :

```bash
sudo systemctl restart postgresql
sudo systemctl status postgresql --no-pager
sudo ss -ltnp | grep 5432
```

- **État du service :** À compléter
- **Le port TCP 5432 est-il en écoute ?** Oui / Non
- **Résultat observé :**
  ```text
  À compléter
  ```

### 4. Tester la connexion depuis `web`

Sur `web`, installer le client PostgreSQL si nécessaire, puis tester le port et la connexion à la base.

- **Résultat de `nc -zv 192.168.56.13 5432` :**
  ```text
  À compléter
  ```

- **Résultat de la commande `psql` :**
  ```text
  À compléter
  ```

- **La connexion PostgreSQL a-t-elle réussi ?** Oui / Non
- **Quelle information renvoie `SELECT version();` ?** À compléter

Si la connexion échoue, indiquez les vérifications effectuées : adresse IP, connectivité réseau, écoute PostgreSQL, règle `pg_hba.conf`, pare-feu et identifiants.

**Diagnostic / solution appliquée :** À compléter

**Preuve / capture d’écran :** Ajoutez une capture montrant une connexion PostgreSQL réussie depuis `web` vers `db`.

---

## Étape 4 — Automatiser l’infrastructure avec `infra.sh`

### 1. Créer le script

Créez le fichier `infra.sh` sur la machine hôte qui dispose de VirtualBox. Le script du sujet doit notamment :

- vérifier l’existence de la VM `base` ;
- vérifier la présence de l’instantané `base-propre` ;
- créer les clones liés `web`, `db` et `monitoring` s’ils n’existent pas ;
- démarrer les VM qui ne sont pas déjà actives ;
- afficher les VM en cours d’exécution.

**Nom et emplacement du fichier créé :** À compléter

**Contenu final de `infra.sh` :**

```bash
# Collez ici votre script complet
À compléter
```

### 2. Exécuter le script

Commandes exécutées :

```bash
chmod +x infra.sh
./infra.sh
```

- **La première exécution a-t-elle réussi ?** Oui / Non
- **Quelles VM ont été créées ?** À compléter
- **Quelles VM ont été démarrées ?** À compléter
- **Erreurs éventuelles et solutions :** À compléter

**Extrait significatif de la sortie :**

```text
À compléter
```

### 3. Réexécuter le script

Exécutez une deuxième fois :

```bash
./infra.sh
```

- **Qu’observez-vous lors de cette deuxième exécution ?** À compléter
- **Les VM existantes sont-elles recréées ?** À compléter
- **Les VM déjà démarrées sont-elles redémarrées ?** À compléter

### 4. Questions sur l’automatisation

**a. Expliquez la notion d’idempotence dans le contexte de ce script.**

Réponse : À compléter

**b. Quel est l’avantage d’un clone lié ?**

Réponse : À compléter

**c. Pourquoi la suppression ou le déplacement incorrect du disque parent peut-il rendre les clones inutilisables ?**

Réponse : À compléter

**d. Le script configure-t-il les adresses IP et les noms d’hôte des systèmes invités ? Justifiez.**

Réponse : À compléter

**e. Quelles modifications proposeriez-vous pour automatiser également la configuration réseau et système des VM ?**

Réponse : À compléter

**f. L’idempotence du script garantit-elle que toute l’infrastructure est entièrement configurée ? Expliquez.**

Réponse : À compléter

---

# Livrables à remettre

## 1. Script d’automatisation

- [ ] Le fichier `infra.sh` est présent dans le dépôt.
- [ ] Le script a été exécuté au moins deux fois.
- [ ] La sortie des deux exécutions est documentée.

**Chemin du fichier dans le dépôt :** À compléter

## 2. Preuve de connexion PostgreSQL

- [ ] Une capture montre une connexion PostgreSQL depuis `web` vers `db`.
- [ ] La capture ou le résultat montre l’exécution de `SELECT version();`.

**Nom du fichier de capture :** À compléter

## 3. Schéma de l’infrastructure

Insérez votre schéma sous forme d’image ou utilisez le modèle textuel ci-dessous.

```text
Machine hôte : VirtualBox
       |
       +---- VM web
       |       IP : 192.168.56.12
       |       Service : Nginx
       |
       +---- VM db
       |       IP : 192.168.56.13
       |       Service : PostgreSQL (TCP 5432)
       |
       +---- VM monitoring
               IP : À configurer
               Service : À préciser
```

**Schéma final (fichier image ou lien relatif) :** À compléter

**Flux réseau entre `web` et `db` :** À compléter

---

# Bilan du TP

Répondez brièvement aux questions suivantes.

1. **Quelle est la fonction de VirtualBox dans cette infrastructure ?**  
   Réponse : À compléter

2. **Pourquoi séparer le serveur Web et le serveur de base de données dans deux VM ?**  
   Réponse : À compléter

3. **Quels éléments doivent être vérifiés lorsqu’une VM ne peut pas joindre une autre VM ?**  
   Réponse : À compléter

4. **Quelle est la différence entre créer manuellement les VM et automatiser leur création avec `VBoxManage` ?**  
   Réponse : À compléter

5. **Citez une limite du script fourni et une amélioration possible.**  
   Réponse : À compléter

## Autoévaluation

Cochez les compétences que vous estimez maîtriser à la fin du TP.

- [ ] Je sais proposer un plan d’adressage IP.
- [ ] Je sais cloner et démarrer des machines virtuelles.
- [ ] Je sais configurer et vérifier la connectivité entre deux VM.
- [ ] Je sais installer et tester un serveur Web Nginx.
- [ ] Je sais créer une base PostgreSQL et autoriser une connexion réseau.
- [ ] Je sais utiliser `VBoxManage` dans un script Bash.
- [ ] Je comprends l’idempotence et les limites des clones liés.
- [ ] Je sais documenter mes résultats et fournir des preuves de fonctionnement.

## Difficultés rencontrées

Décrivez les principales difficultés rencontrées, leur cause probable et la solution appliquée.

| Difficulté | Cause probable | Solution appliquée |
|---|---|---|
| À compléter | À compléter | À compléter |
| À compléter | À compléter | À compléter |
| À compléter | À compléter | À compléter |

## Conclusion personnelle

Résumez en quelques lignes ce que vous avez appris et ce que vous souhaiteriez approfondir.

À compléter
