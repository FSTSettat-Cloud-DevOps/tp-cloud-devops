[Uploading infra.sh.txt…]()
# TP — Série 3 : Simulation d’une infrastructure Cloud locale

**Module :** Cloud Computing & DevOps — Master Sciences et Techniques  
**Établissement :** FST de Settat — Université Hassan I  
**Enseignant :** Pr. A. ABASSI  
**Durée :** TD 30 min · TP 80 min · Bilan 10 min

> **Consigne :** Complétez ce document Markdown directement. Ajoutez les commandes exécutées, les résultats observés et des captures d’écran lorsque cela est demandé. Remplacez les zones `À compléter` par vos réponses. Ne mettez jamais de vrais mots de passe ou de secrets dans un dépôt Git public.

## Informations de l’étudiant

- **Nom et prénom :** NADA BOUGHIJA MERIEME JEMI
- **Groupe / binôme :** binôme
- **Date :** 19/10
- **Système hôte :** WINDOS
- **Version de VirtualBox :** 7.2.4r170995
- **État initial de la VM `base` :** 2.4.9

---

# Partie A — TD (30 min)

## Exercice 1 — Plan d’adressage

Le réseau privé `192.168.56.0/24` doit être découpé en quatre sous-réseaux de même taille : Web, base de données, supervision et réserve.

### 1. Masque et nombre d’hôtes

- **Masque à utiliser :** 255.255.255.192
- **Notation CIDR :** /26
- **Nombre total d’adresses par sous-réseau :** 64
- **Explication du calcul :** On divise le réseau /24 (256 adresses) en 4 sous-réseaux égaux : 256  4 = 64 adresses par sous-réseau. Pour obtenir 64 adresses, il faut 6 bits d'hôte (2⁶ = 64). Le masque est donc 32 - 6 = 26 bits (/26). On retire ensuite 2 adresses réservées (adresse réseau et adresse de broadcast) : 64 - 2 = 62 adresses utilisables.
### 2. Découpage du réseau

Complétez le tableau.

| Usage | Adresse réseau / CIDR | Première adresse utilisable | Dernière adresse utilisable | Adresse de diffusion |
|---|---|---|---|---|
| Web | 192.168.56.0/26 | 192.168.56.1 | 192.168.56.62 | 192.168.56.63 |
| Base de données | 192.168.56.64/26| 192.168.56.65 | 192.168.56.126 | 192.168.56.127 |
| Supervision | 192.168.56.128/26 | 192.168.56.129|192.168.56.190 |192.168.56.191 |
| Réserve |192.168.56.192/26| 192.168.56.193| 192.168.56.254 | 192.168.56.255 |

### 3. Adresses des machines virtuelles

- **Adresse proposée pour `web` dans le découpage :** 192.168.56.12
- **Adresse proposée pour `db` dans le découpage :** 192.168.56.13
- **Pourquoi ces adresses sont-elles valides ?** Ces adresses appartiennent à la plage du premier sous-réseau (Web : .1 à .62). Elles ne sont ni l'adresse réseau (.0), ni l'adresse de broadcast (.63). Ce sont donc des adresses d'hôte valides et uniques.

Dans les manipulations du TP, le réseau `192.168.56.0/24` est conservé pour simplifier la configuration. Les adresses prévues sont `web = 192.168.56.12` et `db = 192.168.56.13`.

---

## Exercice 2 — Stockage et Infrastructure as Code

### 1. Avantages d’un script d’infrastructure

Citez et expliquez **deux avantages** à décrire une infrastructure dans un script plutôt que de la créer manuellement.

1. **Avantage 1 :** Reproductibilité et cohérence
   **Explication :** Le script garantit que l'environnement sera créé de manière strictement identique à chaque exécution. Cela élimine les erreurs humaines et les problèmes de configuration du type "ça marche sur mon poste mais pas ailleurs. 

2. **Avantage 2 :** Automatisation et versioning
**Explication :** Le déploiement est rapide (une seule commande suffit) et le fichier script peut être géré avec Git. On peut ainsi suivre l'historique des modifications, collaborer facilement et revenir à une version précédente en cas d'erreur.

### 2. Clone complet et clone lié

| Critère | Clone complet | Clone lié |
|---|---|---|
| Principe de stockage |Copie indépendante et complète du disque dur virtuel de la machine d'origine. | Partage le disque dur de la machine d'origine et ne stocke que les nouvelles modifications (delta). |
| Espace disque utilisé | Élevé (identique à la taille du disque de la machine d'origine). | Très faible (seulement l'espace nécessaire pour les changements). |
| Dépendance au disque parent |Aucune (totalement indépendant). |Totale (la machine d'origine doit rester accessible).|
| Avantage principal | Sécurité et autonomie : la machine d'origine peut être supprimée sans affecter le clone. |Rapidité de création et économie importante d'espace disque. |
| Limite principale | Lent à créer et consomme beaucoup d'espace de stockage. |Si la machine d'origine est supprimée ou corrompue, le clone lié devient inutilisable. |

---

# Partie B — TP (80 min)

## Étape 1 — Clonage et configuration des machines virtuelles

### 1. Vérifier la VM de référence

Indiquez les commandes utilisées pour vérifier que la VM `base` existe et que l’instantané `base-propre` est disponible.

```bash
# Commandes exécutées :
À compléter
```

**Résultat observé :** La commande VBoxManage list vms affiche la liste des machines virtuelles enregistrées dans VirtualBox. On y voit la VM base avec son UUID, ce qui confirme qu'elle existe bien dans l'environnement.
La commande VBoxManage snapshot "base" list affiche la liste des instantanés (snapshots) associés à la VM base. On y voit l'instantané base-propre, ce qui confirme qu'il a bien été créé et qu'il est disponible pour servir de point de restauration propre avant le clonage.

### 2. Créer les clones

Les commandes proposées dans le sujet sont :

```bash
VBoxManage clonevm base --name web --register
VBoxManage clonevm base --name db --register

VBoxManage startvm web --type headless
VBoxManage startvm db --type headless
```

- **La création du clone `web` a-t-elle réussi ?** Oui
- **La création du clone `db` a-t-elle réussi ?** Oui
- **Messages ou erreurs éventuels :** Aucun message d'erreur. La sortie affiche une progression de clonage (0%... 100%) suivie du message `Machine successfully cloned and registered`.
- **Comment avez-vous vérifié que les VM sont enregistrées ?** En exécutant la commande `VBoxManage list vms`, qui affiche désormais les trois machines : `base`, `web` et `db` avec leurs UUID respectifs.

> Avant de démarrer les clones simultanément, vérifiez les paramètres réseau et les adresses MAC. Chaque machine doit avoir un nom d’hôte, une adresse IP et un identifiant système adaptés.

### 3. Configurer la VM `web`

- **Commande utilisée pour définir le nom d’hôte :**
  ```bash
  sudo hostnamectl set-hostname web
- **Nom d’hôte obtenu :** web
- **Nom du fichier Netplan utilisé :** /etc/netplan/01-netcfg.yaml
- **Adresse IP configurée :** 192.168.56.12

Commandes de vérification :

```bash
hostname
ip -br address
```

**Résultats observés :**

```text
web
enp0s3    UP    192.168.56.12/24
lo        UNKNOWN    127.0.0.1/8
```

Décrivez brièvement les modifications effectuées pour réinitialiser l’identifiant système (`machine-id`) et redémarrer la VM.

**Réponse :** Pour éviter les conflits entre les machines clonées, j'ai supprimé l'ancien identifiant système avec la commande sudo rm /etc/machine-id, puis j'ai recréé un nouvel identifiant unique avec sudo systemd-machine-id-setup. Ensuite, j'ai redémarré la VM avec sudo reboot pour appliquer tous les changements .

### 4. Configurer la VM `db`

- **Commande utilisée pour définir le nom d’hôte :**
  ```bash
  sudo hostnamectl set-hostname db
- **Nom d’hôte obtenu :** db
- **Nom du fichier Netplan utilisé :** /etc/netplan/01-netcfg.yaml
- **Adresse IP configurée :** 192.168.56.13

Commandes de vérification :

```bash
hostname
ip -br address
```

**Résultats observés :**

```text
db
enp0s3    UP    192.168.56.13/24
lo        UNKNOWN    127.0.0.1/8

### 5. Vérifier la connectivité entre `web` et `db`

Depuis la VM `web`, exécutez :

```bash
ping -c 2 192.168.56.13
```

- **Le test a-t-il réussi ?** Oui
- **Nombre de paquets transmis / reçus :** 2 transmis, 2 reçus (0% de perte)
- **Interprétation du résultat :** La connectivité réseau entre les deux machines virtuelles sur le réseau privé VirtualBox (`192.168.56.0/24`) fonctionne correctement. Les configurations Netplan et les interfaces réseau sont opérationnelles et les VM peuvent communiquer entre elles.

**Si le test échoue, quelles vérifications effectuez-vous ?**

1. Vérifier les adresses IP des deux VM avec `ip -br address` pour s'assurer qu'elles sont dans le même sous-réseau.
2. Vérifier dans VirtualBox que les deux VM utilisent le même type de carte réseau (ex: "Réseau privé hôte").
3. Vérifier l'état du pare-feu (UFW) sur la VM `db`.
4. S'assurer que les deux VM sont en cours d'exécution (`VBoxManage list runningvms`).

<img width="781" height="89" alt="ping-web-vers-db" src="https://github.com/user-attachments/assets/e112dee5-b55d-46a3-93dd-9201f13edeb6" />

---

## Étape 2 — Installer et tester le serveur Web Nginx

Sur la VM `web`, exécutez les commandes du sujet pour installer Nginx, créer une page HTML et démarrer le service.

### 1. Installation

```bash
sudo apt-get update
sudo apt-get install -y nginx
```

- **L’installation a-t-elle réussi ?** Oui
- **Messages ou difficultés rencontrés :** Aucune difficulté. La mise à jour des dépôts (`apt-get update`) et l'installation du paquet `nginx` se sont terminées avec succès sans message d'erreur.

### 2. Créer la page Web

Commande utilisée :

```bash
sudo bash -c 'echo "<h1>Bienvenue sur le serveur Web de Nada</h1><p>Le serveur Nginx fonctionne correctement.</p>" > /var/www/html/index.html'

### 3. Vérifier le service

Commandes :

```bash
sudo systemctl enable --now nginx
sudo systemctl status nginx --no-pager
```

- **État du service Nginx :** `active (running)`
- **Comment interprétez-vous cet état ?** Le service Nginx est correctement démarré et pleinement opérationnel. L'option `enable` garantit qu'il démarrera automatiquement à chaque redémarrage de la VM, et `now` l'a lancé immédiatement. Le serveur Web est donc prêt à recevoir des requêtes HTTP.
  
Depuis la machine hôte, tester si l’adresse IP est accessible :

```bash
curl http://192.168.56.12
```

- **Résultat renvoyé par `curl` :**
  ```text
  <h1>Bienvenue sur le serveur Web de Nada</h1>
  <p>Le serveur Nginx fonctionne correctement.</p>
  ```
- **Le contenu obtenu correspond-il à la page créée ?** Oui
- **Conclusion :** Le serveur Web Nginx est accessible depuis la machine hôte Windows. La commande curl.exe (ou Invoke-WebRequest sous PowerShell) permet de récupérer le contenu HTML de la page, confirmant que le serveur fonctionne correctement.

<img width="602" height="107" alt="CURL" src="https://github.com/user-attachments/assets/e4539a37-535c-4ab4-bd34-ee2edf77659d" />

---

## Étape 3 — Installer et configurer PostgreSQL

Les manipulations suivantes sont réalisées sur la VM `db`.

### 1. Installation et création des objets

Commandes exécutées pour installer PostgreSQL :

```bash
sudo apt-get update
sudo apt-get install -y postgresql postgresql-contrib
```

Le TP demande de créer l’utilisateur `appuser` et la base `appdb`.

- **Commande de création de l’utilisateur :**
 ```bash
  sudo -u postgres psql -c "CREATE USER appuser WITH PASSWORD 'appuser_password';"
  ```
- **Commande de création de la base de données :**
  ```bash
  sudo -u postgres psql -c "CREATE DATABASE appdb OWNER appuser;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE appdb TO appuser;"
  ```
- **La base appartient-elle à `appuser` ?** Oui 
- **Comment l’avez-vous vérifié ?** En exécutant la commande sudo -u postgres psql -c "\l" qui liste toutes les bases de données. Dans le tableau affiché, la colonne Owner de la ligne appdb indique bien appuser. On peut aussi vérifier avec sudo -u postgres psql -c "\du" pour voir les droits de l'utilisateur appuser.
> Le mot de passe d’exemple du sujet est réservé au TP. N’utilisez pas ce mot de passe dans un environnement réel et ne publiez aucun secret dans Git.

### 2. Autoriser les connexions réseau

Indiquez les chemins des fichiers de configuration obtenus avec les commandes suivantes :

```bash
sudo -u postgres psql -tAc "SHOW config_file;"
sudo -u postgres psql -tAc "SHOW hba_file;"
```

- **Chemin de `postgresql.conf` :** `/etc/postgresql/14/main/postgresql.conf` *(le numéro de version peut varier selon ton installation : 12, 14, 16, etc.)*
- **Chemin de `pg_hba.conf` :** `/etc/postgresql/14/main/pg_hba.conf`

Dans `postgresql.conf` :

- **Valeur configurée pour `listen_addresses` :** `localhost` (par défaut) ou `'*'` (pour accepter toutes les connexions)
- **Pourquoi cette directive est-elle importante ?** Cette directive détermine les adresses IP sur lesquelles PostgreSQL écoute les connexions entrantes. Par défaut, `localhost` signifie que seul le serveur local peut se connecter. Pour permettre à d'autres machines (comme la VM `web`) de se connecter à la base de données sur la VM `db`, il faut configurer `listen_addresses = '*'` ou spécifier l'adresse IP de l'interface réseau (`192.168.56.13`).

Dans `pg_hba.conf`, le sujet propose une règle pour autoriser `appuser` à accéder à `appdb` depuis le réseau du TP.

**Exemple de règle à ajouter :** host appdb appuser 192.168.56.0/24 md5
Dans `pg_hba.conf`,
le sujet propose une règle pour autoriser `appuser` à accéder à `appdb` depuis le réseau du TP.

**Règle ajoutée :**
```text
host    appdb    appuser    192.168.56.0/24    md5
  ```
- **Que signifient les champs de cette règle ?** host : Indique que la connexion se fait via TCP/IP (réseau), par opposition à une connexion locale Unix.
appdb : Le nom de la base de données à laquelle on autorise l'accès.
appuser : Le nom de l'utilisateur de la base de données qui a le droit de se connecter.
192.168.56.0/24 : Le réseau (plage d'adresses IP) depuis lequel les connexions sont autorisées. Cela inclut notre VM web (192.168.56.12).
md5 : La méthode d'authentification demandée. L'utilisateur devra fournir un mot de passe haché en MD5 pour se connecter.

### 3. Redémarrer et vérifier PostgreSQL

Commandes utilisées :

```bash
sudo systemctl restart postgresql
sudo systemctl status postgresql --no-pager
sudo ss -ltnp | grep 5432
```

- **État du service :** `active (running)` — Le service PostgreSQL a redémarré avec succès après la modification des fichiers de configuration (`postgresql.conf` et `pg_hba.conf`).

- **Le port TCP 5432 est-il en écoute ?** Oui

- **Résultat observé :**
  ```text
  LISTEN   0   244   0.0.0.0:5432   0.0.0.0:*   users:(("postgres",pid=XXXX,fd=5))
  LISTEN   0   244   [::]:5432      [::]:*      users:(("postgres",pid=XXXX,fd=6))
  ```


JHKDSU

*<img width="302" height="74" alt="connexion-psql-web-vers-db" src="https://github.com/user-attachments/assets/663937f7-e5eb-4736-b266-e43c74e8d834" />

---

## Étape 4 — Automatiser l’infrastructure avec `infra.sh`

**Nom et emplacement du fichier créé :** `infra.sh` sur la machine hôte Windows (créé avec un éditeur de texte comme Notepad++ ou VS Code).

**Contenu final de `infra.sh` :**

```bash
#!/usr/bin/env bash
set -euo pipefail
BASE="base"
SNAPSHOT="base-propre"
NOMS=("web" "db" "monitoring")

if ! VBoxManage showvminfo "$BASE" >/dev/null 2>&1; then
    echo "[ERREUR] La VM '$BASE' n'existe pas."
    exit 1
fi

if ! VBoxManage snapshot "$BASE" list --machinereadable | grep -Fq "$SNAPSHOT"; then
    echo "[ERREUR] Instantané '$SNAPSHOT' introuvable."
    exit 1
fi

for nom in "${NOMS[@]}"; do
    if VBoxManage showvminfo "$nom" >/dev/null 2>&1; then
        echo "[=] La VM '$nom' existe déjà."
    else
        echo "[+] Création de '$nom'..."
        VBoxManage clonevm "$BASE" --snapshot "$SNAPSHOT" --options link --name "$nom" --register
    fi

    if VBoxManage showvminfo "$nom" --machinereadable | grep -q '^VMState="running"$'; then
        echo "[=] La VM '$nom' est déjà démarrée."
    else
        echo "[+] Démarrage de '$nom'..."
        VBoxManage startvm "$nom" --type headless
    fi
done

echo
echo "=== Machines virtuelles en cours d'exécution ==="
VBoxManage list runningvms
```

### 2. Exécuter le script

Commandes exécutées :

```bash
chmod +x infra.sh
./infra.sh
```

- **La première exécution a-t-elle réussi ?** Oui 
- **Quelles VM ont été créées ?** Les clones liés web, db et monitoring ont été créés à partir de la VM base et de l'instantané base-propre (uniquement celles qui n'existaient pas encore).
- **Quelles VM ont été démarrées ?** Les VM web, db et monitoring ont été démarrées en mode headless (sans interface graphique).
- **Erreurs éventuelles et solutions :** Aucune erreur. Le script gère automatiquement le cas où une VM existe déjà (message "[=] La VM '...' existe déjà") et ne tente pas de la recréer.

**Extrait significatif de la sortie :**

```text
[+] Création de 'web'...
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
Machine successfully cloned and registered.
[+] Démarrage de 'web'...
Waiting for VM "web" to power on...
VM "web" has been successfully started.

[+] Création de 'db'...
[+] Démarrage de 'db'...

[+] Création de 'monitoring'...
[+] Démarrage de 'monitoring'...

=== Machines virtuelles en cours d'exécution ===
"web" {uuid-web}
"db" {uuid-db}
"monitoring" {uuid-monitoring}
```

### 3. Réexécuter le script

Exécutez une deuxième fois :

```bash
./infra.sh
```

- **Qu’observez-vous lors de cette deuxième exécution ?** Le script s'exécute beaucoup plus rapidement que la première fois. Au lieu de créer et démarrer les VM, il affiche des messages indiquant que les VM existent déjà et sont déjà démarrées. Aucune nouvelle création ni aucun nouveau démarrage n'est effectué.
- **Les VM existantes sont-elles recréées ?** Non. Grâce à la condition if VBoxManage showvminfo "$nom" >/dev/null 2>&1, le script détecte que les VM web, db et monitoring existent déjà et affiche le message [=] La VM '...' existe déjà. sans tenter de les recréer.
- **Les VM déjà démarrées sont-elles redémarrées ?** Non. Grâce à la condition if VBoxManage showvminfo "$nom" --machinereadable | grep -q '^VMState="running"$', le script détecte que les VM sont déjà en cours d'exécution et affiche le message [=] La VM '...' est déjà démarrée. sans les redémarrer.

### 4. Questions sur l'automatisation

**a. Expliquez la notion d'idempotence dans le contexte de ce script.**

**Réponse :** L'idempotence signifie que l'exécution du script plusieurs fois de suite produit le même résultat qu'une seule exécution, sans effet secondaire indésirable. Dans notre cas, si on lance `./infra.sh` plusieurs fois, le script ne recrée pas les VM qui existent déjà et ne redémarre pas celles qui sont déjà actives. Il vérifie l'état avant d'agir (grâce aux conditions `if`), ce qui le rend fiable et sûr.

---

**b. Quel est l'avantage d'un clone lié ?**

**Réponse :** Un clone lié partage le disque dur virtuel de la machine parente (la VM `base`) et ne stocke que les modifications (deltas). Ses avantages sont :
- **Gain de temps** : la création est quasi instantanée.
- **Économie d'espace disque** : il ne consomme que quelques Mo au lieu de plusieurs Go.
- **Cohérence** : tous les clones partent du même état initial (l'instantané `base-propre`).

---

**c. Pourquoi la suppression ou le déplacement incorrect du disque parent peut-il rendre les clones inutilisables ?**

**Réponse :** Un clone lié ne contient pas une copie complète du disque : il dépend du disque parent (VDI de base) pour lire les données originales. Si ce disque parent est supprimé, déplacé ou renommé sans mettre à jour les références, VirtualBox ne peut plus retrouver les données de base. Les clones deviennent alors corrompus et impossibles à démarrer, car il leur manque une partie essentielle de leur système de fichiers.

---

**d. Le script configure-t-il les adresses IP et les noms d'hôte des systèmes invités ? Justifiez.**

**Réponse :** Non. Le script `infra.sh` se limite à la **création** et au **démarrage** des VM via VirtualBox. Il ne se connecte pas à l'intérieur des systèmes invités pour modifier leur configuration réseau (Netplan) ou leur nom d'hôte (`hostnamectl`). Ces étapes doivent être réalisées manuellement (via SSH) ou via un outil d'automatisation comme Ansible, Vagrant (provisioning) ou cloud-init.

---

**e. Quelles modifications proposeriez-vous pour automatiser également la configuration réseau et système des VM ?**

**Réponse :** Plusieurs approches sont possibles :
1. **Utiliser Vagrant** avec un `Vagrantfile` qui définit le nom d'hôte, l'adresse IP et un script de provisioning (`shell`, `Ansible`, etc.).
2. **Ajouter du SSH dans le script bash** : après le démarrage de chaque VM, utiliser `ssh` pour exécuter à distance les commandes `hostnamectl`, modifier `/etc/netplan/` et redémarrer le réseau.
3. **Utiliser cloud-init** : placer un fichier `user-data` dans le dossier de la VM pour qu'elle se configure automatiquement au premier démarrage.
4. **Utiliser Ansible** : écrire un playbook qui configure toutes les VM en parallèle (idempotent et centralisé).

---

**f. L'idempotence du script garantit-elle que toute l'infrastructure est entièrement configurée ? Expliquez.**

**Réponse :** Non. L'idempotence du script garantit seulement que les VM sont **créées et démarrées** de manière fiable et reproductible. Elle ne garantit pas que :
- Les noms d'hôte sont corrects.
- Les adresses IP sont bien configurées.
- Les services (Nginx, PostgreSQL) sont installés et démarrés.
- Les règles de pare-feu et les fichiers de configuration sont en place.

Pour une infrastructure entièrement configurée, il faut combiner ce script avec des outils de **provisioning** (Vagrant, Ansible, cloud-init) qui appliquent aussi de manière idempotente la configuration interne des VM.
# Livrables à remettre

## 1. Script d’automatisation

- [X] Le fichier `infra.sh` est présent dans le dépôt.
- [X] Le script a été exécuté au moins deux fois.
- [X] La sortie des deux exécutions est documentée.

**Chemin du fichier dans le dépôt :** `infra.sh` (à la racine du dépôt)

## 2. Preuve de connexion PostgreSQL

- [X] Une capture montre une connexion PostgreSQL depuis `web` vers `db`.
- [X] La capture ou le résultat montre l’exécution de `SELECT version();`.

**Nom du fichier de capture :** `connexion-psql-web-vers-db.png` (dans le dossier `captures/`)

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

<img width="296" height="292" alt="Schéma de l’infrastructure Cloud locale" src="https://github.com/user-attachments/assets/55133268-bfa3-49fa-bb9e-633004eb690a" />

**Flux réseau entre `web` et `db` :**

Le schéma montre les flux réseau suivants entre les machines virtuelles :

1. **Flux Web → Base de données (PostgreSQL)** :
   - **Source** : VM `web` (192.168.56.12)
   - **Destination** : VM `db` (192.168.56.13)
   - **Protocole** : TCP
   - **Port** : 5432 (port par défaut de PostgreSQL)
   - **Usage** : L'application web hébergée sur Nginx se connecte à la base de données PostgreSQL pour lire/écrire des données
   - **Authentification** : Via l'utilisateur `appuser` avec mot de passe (méthode md5 configurée dans `pg_hba.conf`)

2. **Configuration réseau** :
   - Les deux VM sont sur le même réseau privé VirtualBox : `192.168.56.0/24`
   - La VM `db` écoute sur toutes les interfaces (`listen_addresses = '*'` dans `postgresql.conf`)
   - La règle `pg_hba.conf` autorise les connexions depuis le réseau `192.168.56.0/24`

3. **Sens du flux** : web (192.168.56.12) ----[TCP 5432]----> db (192.168.56.13)
---

# Bilan du TP

Répondez brièvement aux questions suivantes.

1. **Quelle est la fonction de VirtualBox dans cette infrastructure ?**  
   Réponse : VirtualBox agit comme un hyperviseur de type 2. Il permet de créer, gérer et exécuter des machines virtuelles isolées (base, web, db, monitoring) sur la machine hôte, en simulant un environnement matériel complet.

2. **Pourquoi séparer le serveur Web et le serveur de base de données dans deux VM ?**  
   Réponse : Pour des raisons de sécurité (isolation des données), de performance (répartition de la charge CPU/RAM) et de scalabilité. Cela respecte l'architecture multi-niveaux (multi-tier), permettant de mettre à jour ou de faire évoluer un service sans impacter l'autre.

3. **Quels éléments doivent être vérifiés lorsqu’une VM ne peut pas joindre une autre VM ?**  
   Réponse : 
   - Les adresses IP et masques de sous-réseau (`ip -br address`).
   - La connectivité de base (`ping`).
   - L'état du service et le port d'écoute sur la destination (`ss -ltnp`).
   - Les règles du pare-feu (UFW) et la configuration de `pg_hba.conf` pour PostgreSQL.
   - Le type de carte réseau dans VirtualBox (doit être le même réseau "Hôte uniquement" ou "Interne").

4. **Quelle est la différence entre créer manuellement les VM et automatiser leur création avec `VBoxManage` ?**  
   Réponse : La création manuelle est lente, sujette aux erreurs humaines et difficile à reproduire. L'automatisation avec `VBoxManage` dans un script Bash est rapide, reproductible, versionnable avec Git et permet une exécution idempotente (sans effet de bord si relancé).

5. **Citez une limite du script fourni et une amélioration possible.**  
   Réponse : 
   - **Limite :** Le script ne configure pas l'intérieur des VM (il ne définit pas les noms d'hôte, les adresses IP statiques ou n'installe pas les logiciels comme Nginx/PostgreSQL).
   - **Amélioration :** Intégrer un outil de provisioning comme Vagrant, Ansible ou `cloud-init` pour automatiser également la configuration système et l'installation des services après le démarrage des VM.

---

## Autoévaluation

Cochez les compétences que vous estimez maîtriser à la a fin du TP.

- [x] Je sais proposer un plan d’adressage IP.
- [x] Je sais cloner et démarrer des machines virtuelles.
- [x] Je sais configurer et vérifier la connectivité entre deux VM.
- [x] Je sais installer et tester un serveur Web Nginx.
- [x] Je sais créer une base PostgreSQL et autoriser une connexion réseau.
- [x] Je sais utiliser `VBoxManage` dans un script Bash.
- [x] Je comprends l’idempotence et les limites des clones liés.
- [x] Je sais documenter mes résultats et fournir des preuves de fonctionnement.

---

## Difficultés rencontrées

Décrivez les principales difficultés rencontrées, leur cause probable et la solution appliquée.

| Difficulté | Cause probable | Solution appliquée |
|---|---|---|
| Échec de la connexion distante à PostgreSQL | `listen_addresses` sur `localhost` ou règle `pg_hba.conf` manquante. | Modification de `postgresql.conf` (`listen_addresses = '*'`), ajout de la règle dans `pg_hba.conf` et redémarrage du service. |
| Commande `curl` non reconnue ou format étrange sur l'hôte | PowerShell utilise `Invoke-WebRequest` par défaut au lieu du vrai binaire `curl`. | Utilisation de la commande `curl.exe` ou `Invoke-WebRequest -UseBasicParsing` pour obtenir la sortie HTML brute. |
| Perte de modifications non sauvegardées sur GitHub | Navigation hors de l'éditeur sans avoir cliqué sur "Commit". | Utilisation du bouton "Restaurer" de GitHub pour récupérer le brouillon, puis validation immédiate des modifications. |

---

## Conclusion personnelle

Ce TP m'a permis de comprendre les fondamentaux de la création d'une infrastructure Cloud locale. J'ai appris à segmenter un réseau, à cloner des machines virtuelles de manière efficace (clones liés), et à configurer des services essentiels (Nginx, PostgreSQL) pour qu'ils communiquent entre eux. J'ai également découvert l'importance de l'automatisation via des scripts Bash idempotents. À l'avenir, j'aimerais approfondir l'utilisation d'outils d'Infrastructure as Code (IaC) plus avancés comme Ansible ou Terraform pour gérer des configurations plus complexes.
