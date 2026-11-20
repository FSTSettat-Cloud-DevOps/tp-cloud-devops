# Université Hassan 1er — FST Settat
**Département Informatique**  
**Année Universitaire :** 2026–2027  
**Module :** Cloud Computing, Virtualisation & DevOps  
**Enseignant :** Pr. Abdelfattah Abassi  

---

# Série 4 — Conteneurs, architecture et commandes de base
* **Durée :** 2 h (TD 40 min + TP 80 min)
* **Chapitre :** Conteneurisation — Parties I, II et III du cours

> ### 🎯 Objectifs de la série
> À l'issue de cette série, l'étudiant sera capable de :
> * Distinguer une machine virtuelle d'un conteneur et justifier le choix ;
> * Situer le client, le démon et le registre dans l'architecture Docker ;
> * Distinguer une *image* d'un *conteneur* ;
> * Démarrer, lister, explorer, arrêter et supprimer des conteneurs ;
> * Mesurer expérimentalement la légèreté des conteneurs.

---

## 1. Partie TD (40 min)

### Exercice 1 — VM ou conteneur ? (10 min)

Indiquer si chaque affirmation est vraie ou fausse, puis corriger les affirmations fausses.

1. Un conteneur embarque son propre noyau (kernel) de système d'exploitation.
2. Une machine virtuelle s'exécute au-dessus d'un hyperviseur.
3. Un conteneur démarre généralement plus vite qu'une machine virtuelle.
4. L'isolation offerte par un conteneur est plus forte que celle d'une machine virtuelle.
5. Dans le Cloud, on exécute souvent des conteneurs à l'intérieur de machines virtuelles.
6. Docker s'appuie sur les *namespaces* et les *cgroups* du noyau Linux.

**Question complémentaire :** Un serveur possède 16 Go de RAM. Pourquoi peut-on y lancer beaucoup plus de conteneurs que de VM ?

---

### Exercice 2 — Architecture de Docker (10 min)

```
+------------------------+             +--------------------------+             +------------------------+
|      Composant (1)     |     (a)     |       Composant (2)      |     (b)     |      Composant (3)     |
|   commandes docker...  | <---------> |    processus dockerd     | <---------> |     ex. Docker Hub     |
+------------------------+             +--------------------------+             +------------------------+
```

1. Nommer les composants **(1)**, **(2)**, **(3)** et les échanges **(a)**, **(b)**.
2. Pour chacune des commandes `docker pull`, `docker run`, `docker build`, `docker push`, indiquer quels composants interviennent.
3. Le démon Docker est arrêté. Que renvoient `docker --version` et `docker version` ? Justifier.

---

### Exercice 3 — Image ou conteneur ? (10 min)

Un administrateur exécute trois fois la commande suivante, sans option `--name` :

```bash
docker run -d nginx
```

1. Combien d'images `nginx` et combien de conteneurs existent-ils ensuite sur la machine ?
2. Il supprime ensuite les trois conteneurs avec `docker rm -f`. L'image existe-t-elle encore ? Pourquoi ?
3. Compléter l'analogie : 
   * **Image** $\leftrightarrow$ ......... (programmation orientée objet) $\leftrightarrow$ ......... (cuisine)
   * **Conteneur** $\leftrightarrow$ ......... $\leftrightarrow$ .........

---

### Exercice 4 — Lire une commande (10 min)

```bash
docker run -d --name monweb -p 8080:80 nginx
```

1. Expliquer chaque option de la commande.
2. Quelle URL faut-il ouvrir sur la machine hôte pour voir la page d'accueil de Nginx ?
3. On exécute une seconde fois exactement la même commande. Que se passe-t-il ? Pourquoi ?
4. On exécute maintenant `docker run -d --name monweb2 -p 8080:80 nginx`. Que se passe-t-il ? Proposer une correction.

---

<details>
<summary><b>💡 Corrigé de la Partie TD (Cliquer pour dérouler)</b></summary>

#### Corrigé Exercice 1
* **1.** Faux (il partage le noyau de l'hôte).
* **2.** Vrai.
* **3.** Vrai (secondes ou millisecondes contre minutes).
* **4.** Faux (l'isolation d'une VM, au niveau matériel, est plus forte).
* **5.** Vrai (on cumule les deux niveaux d'isolation).
* **6.** Vrai.
* **Question complémentaire :** Chaque VM réserve la RAM d'un OS complet ; les conteneurs partagent le noyau de l'hôte et ne consomment que la mémoire de leurs processus.

#### Corrigé Exercice 2
1. **Composants :** (1) Docker CLI (client), (2) Docker Daemon, (3) Registry. **Échanges :** (a) API REST, (b) pull / push.
2. **Interventions :**
   * `pull` : CLI $\rightarrow$ démon $\rightarrow$ registre.
   * `run` : CLI $\rightarrow$ démon (et registre si l'image est absente : pull implicite).
   * `build` : CLI $\rightarrow$ démon (le contexte est envoyé au démon ; le registre n'intervient que pour l'image de base).
   * `push` : CLI $\rightarrow$ démon $\rightarrow$ registre.
3. `docker --version` affiche la version du client : elle ne contacte pas le démon. `docker version` affiche la section *Client* puis une erreur de connexion pour la section *Server*.

#### Corrigé Exercice 3
1. Une seule image, trois conteneurs (noms aléatoires, ex. `eager_curie`).
2. Oui : supprimer un conteneur ne supprime pas l'image (il faut `docker rmi`).
3. Image = **Classe** = **Recette** ; Conteneur = **Objet (instance)** = **Plat préparé**.

#### Corrigé Exercice 4
1. `-d` : arrière-plan ; `--name monweb` : nom lisible ; `-p 8080:80` : port 8080 de l'hôte redirigé vers le port 80 du conteneur ; `nginx` : image.
2. `http://localhost:8080`
3. **Erreur :** le nom `monweb` est déjà utilisé par un conteneur (même arrêté). Il faut le supprimer ou choisir un autre nom.
4. **Erreur « port is already allocated » :** le port 8080 de l'hôte est déjà publié. Correction : `-p 8081:80`.

</details>

---

## 2. Partie TP (80 min)

> ⚠️ **Attention :** Travailler dans la VM Ubuntu. Si Docker répond `permission denied`, exécuter `sudo usermod -aG docker $USER` puis se reconnecter (ou utiliser `newgrp docker`).

Noter la version du client, celle du serveur, le nombre d'images et de conteneurs indiqué par `docker info`. Lire le message affiché par `hello-world` et recopier les étapes qu'il décrit.

---
### ✅ Résultats de l'Étape A

**1. Version du client Docker :**
Docker version 29.9.1, build dfc520d 
**2. Version du serveur (moteur Linux WSL 2) :**
Server Version: 29.9.1
Storage Driver: overlayfs
Cgroup Version: 2
Kernel Version: 6.18.54.1-microsoft-standard-WSL2
Operating System: Docker Desktop
OSType: linux
Architecture: x86_64
CPUs: 8
Total Memory: 3.748GiB
**3. Nombre d'images et de conteneurs (docker info) :**
- **Images :** 4 (hello-world, nginx, redis, alpine)
- **Conteneurs :** 1 (hello-world en état Exited)

**4. Étapes décrites par le message `hello-world` :**

Le message "Hello from Docker!" confirme que l'installation fonctionne correctement. Docker a suivi les étapes suivantes :

1. Le client Docker a contacté le démon Docker.
2. Le démon Docker a téléchargé (*pulled*) l'image "hello-world" depuis Docker Hub (amd64).
3. Le démon Docker a créé un nouveau conteneur à partir de cette image, qui exécute l'exécutable produisant la sortie que nous lisons actuellement.
4. Le démon Docker a diffusé (*streamed*) cette sortie au client Docker, qui l'a envoyée à notre terminal.
 **Capture :**
   <img width="856" height="146" alt="docker --version" src="https://github.com/user-attachments/assets/14c7407e-08ec-455a-9090-00590aa8ae91" />
---

### Étape B — Premier serveur web (15 min)

Pour la dernière commande, ouvrir un second terminal, exécuter `curl http://localhost:8080` et observer la ligne de journal produite ; arrêter le suivi avec `Ctrl+C`.

**Questions :** Quelle est la signification de chaque colonne de `docker ps` ? Que se passerait-il si l'option `-d` était omise ?
### ✅ Réponses aux questions de l'Étape B

**1. Signification de chaque colonne de `docker ps` :**

| Colonne | Signification | Exemple (d'après ta capture) |
| :--- | :--- | :--- |
| **CONTAINER ID** | Identifiant unique du conteneur | `0eb76f2fc2f1` |
| **IMAGE** | Image utilisée pour créer le conteneur | `nginx` |
| **COMMAND** | Commande exécutée au démarrage | `"/docker-entrypoint.s…"` |
| **CREATED** | Date/heure de création | `18 minutes ago` |
| **STATUS** | État actuel du conteneur | `Up 18 minutes` |
| **PORTS** | Redirections de ports (hôte → conteneur) | `0.0.0.0:8080->80/tcp, [::]:8080->80/tcp` |
| **NAMES** | Nom attribué au conteneur | `monweb` |

**2. Que se passerait-il si l'option `-d` était omise ?**
Si on omet l'option -d (détaché / detached), le conteneur s'exécute au premier plan et bloque le terminal PowerShell. Tu ne pourras plus taper de commandes tant que le conteneur tourne. Pour arrêter le conteneur, il faudra faire Ctrl+C, ce qui terminera également le processus du conteneur. L'option -d est donc essentielle pour libérer le terminal tout en gardant le serveur web actif en arrière-plan.

---


**Questions :** Quel système d'exploitation voit-on dans le conteneur ? Est-il identique à celui de la VM ? Quel noyau le conteneur utilise-t-il (`uname -r` dans le conteneur et dans la VM) ?

**1— Exploration interactive du conteneur** .
Comme le montre la sortie de cat /etc/os-release : 
PRETTY_NAME="Debian GNU/Linux 13 (trixie)"
NAME="Debian GNU/Linux"
VERSION_ID="13"
Ce n'est PAS Windows ! Le conteneur Nginx est basé sur une image Debian Linux.
**2. 6.18.54.1-microsoft-standard-WSL2**
C'est le noyau Linux fourni par WSL 2 (Windows Subsystem for Linux) de Microsoft.
**3.C'est un noyau LINUX, pas un noyau Windows.**
Bien que Docker Desktop s'exécute sur Windows, il utilise WSL 2 (Windows Subsystem for Linux 2) qui fournit un vrai noyau Linux léger et optimisé. Les conteneurs Linux partagent ce noyau WSL 2, ce qui leur permet de fonctionner nativement sans avoir besoin d'une VM complète.


---

### Étape D — Cycle de vie d'un conteneur (10 min)


**Observer et expliquer :** Après `stop` puis `start`, quel message la page affiche-t-elle ? Et après la suppression suivie de la recréation ? Que peut-on en déduire sur la persistance des données écrites dans un conteneur ?
**Reponces**
La modification est conservée. Après docker stop monweb puis docker start monweb, la page affiche toujours <h1>Bonjour Docker depuis Windows</h1>. Le système de fichiers du conteneur est persistant tant que le conteneur existe, même s'il est arrêté. Les données ne sont pas perdues lors d'un simple arrêt.
La modification est perdue. Après docker rm -f monweb (suppression) puis docker run -d --name monweb -p 8080:80 nginx (recréation), la page revient à "Welcome to nginx!" (la version par défaut de l'image). Un nouveau conteneur part de l'image originale intacte, sans les modifications précédentes.
Un conteneur n'est pas persistant par défaut après suppression. Les données écrites dans le système de fichiers du conteneur survivent aux arrêts/redémarrages, mais sont perdues définitivement quand le conteneur est supprimé (docker rm). Pour conserver les données de manière permanente, il faut utiliser des volumes Docker (-v) qui montent un dossier de l'hôte Windows dans le conteneur, ou des bind mounts.

---

3. Ouvrir un terminal Bash dans `cache01`, puis exécuter `redis-cli ping`.
4. Dans `redis-cli` (lancé via `docker exec -it cache01 redis-cli`), stocker puis relire une valeur avec `SET module cloud` et `GET module`.
5. Que se passe-t-il si l'on exécute `docker run redis` sans `-d` ? Comment sortir proprement ?
**Réponse**
Erreur CommandNotFoundException. PowerShell ne reconnaît pas la commande redis-cli car Redis n'est pas installé sur la machine hôte Windows. Redis n'existe que dans le conteneur Docker cache01. Pour utiliser Redis, il faut obligatoirement passer par docker exec -it cache01 redis-cli qui ouvre un terminal à l'intérieur du conteneur où Redis est installé.

---

Compléter le tableau ci-dessous, puis mesurer (chronomètre) le temps de démarrage d'une VM VirtualBox comparable et le comparer à celui du conteneur.

| Mesure | nginx | alpine |
| :--- | :--- | :--- |
| **Taille de l'image** (`docker images`) | **243 MB** (disk) / 66.8 MB (content) | **13 MB** (disk) / 3.94 MB (content) |
| **Mémoire RAM utilisée** (`docker stats`) | **~8-11 MiB** par conteneur | **< 1 MiB** (négligeable) |
| **Temps de démarrage** (PowerShell) | **~2-4 secondes** | **~1-2 secondes** |
| **Nombre d'images pour web1 et web2** | **1 seule image partagée** | **1 seule image partagée** |

Nettoyer ensuite l'environnement :
```bash
docker rm -f web1 web2 monweb cache01
docker ps -a
```
Observations :
Taille des images : Alpine est extrêmement légère (3.94 MB) comparée à Nginx (66.8 MB), soit 17 fois plus petite !
Mémoire RAM : Les conteneurs Nginx consomment seulement ~8-11 MiB chacun, ce qui est dérisoire comparé à une VM qui consommerait plusieurs Go.
Temps de démarrage : Alpine démarre en moins d'une seconde, tandis que Nginx prend quelques secondes pour initialiser le serveur web.
Partage des images : Même si tu lances web1 et web2, Docker ne stocke qu'une seule copie de l'image nginx en mémoire. Les deux conteneurs partagent la même image de base.

---
###  Trois commandes que j'ai utilisées avec une phrase d'explication chacune

1. **`docker run -d --name monweb -p 8080:80 nginx`**  
   Cette commande démarre un conteneur Nginx en arrière-plan (`-d`), lui attribue le nom `monweb` et redirige le port 8080 de ma machine Windows vers le port 80 du conteneur, ce qui me permet d'accéder au serveur web via `http://localhost:8080`.

2. **`docker exec -it monweb bash`**  
   Cette commande ouvre un terminal Bash interactif (`-it`) à l'intérieur du conteneur `monweb` déjà en cours d'exécution, ce qui m'a permis d'explorer son système de fichiers, de modifier la page `index.html` et de vérifier le système d'exploitation (Debian) et le noyau Linux (WSL 2) utilisés.

3. **`docker stats --no-stream`**  
   Cette commande affiche les statistiques d'utilisation des ressources (CPU, mémoire RAM, réseau) de tous les conteneurs en cours d'exécution, sans rafraîchissement en continu (`--no-stream`). Elle m'a permis de constater que les conteneurs Nginx ne consommaient que ~8-11 MiB de RAM, prouvant leur légèreté comparée aux machines virtuelles.
### Une capture d’écran de votre navigateur Windows affichant la page personnalisée Nginx
   <img width="861" height="304" alt="la page personnalisée Nginx" src="https://github.com/user-attachments/assets/1e9c67cd-8848-43cf-b432-b7144216f62c" />

### Explication synthétique du rôle de WSL 2 dans le fonctionnement de Docker Desktop sous Windows
WSL 2 (Windows Subsystem for Linux 2) est une fonctionnalité de Windows qui permet d'exécuter un vrai noyau Linux de manière native et optimisée, sans avoir besoin d'une machine virtuelle classique lourde.
Dans le contexte de Docker Desktop sous Windows, WSL 2 joue un rôle central :
Hébergement du démon Docker : Le démon dockerd (moteur Docker) s'exécute à l'intérieur d'une instance WSL 2, qui fournit un environnement Linux complet avec un vrai noyau Linux (visible via uname -r : 6.18.54.1-microsoft-standard-WSL2).
Exécution des conteneurs Linux : Les conteneurs Docker (qui sont par nature Linux) partagent ce noyau WSL 2, ce qui leur permet de fonctionner nativement sans émulation ni virtualisation lourde.
Communication avec Windows : Le client Docker sous Windows (PowerShell, CMD) communique avec le démon via un Named Pipe (\\.\pipe\docker_engine), permettant une intégration transparente avec l'hôte Windows.
Avantages par rapport à une VM Hyper-V classique :
Démarrage rapide : WSL 2 démarre en quelques secondes contre plusieurs minutes pour une VM.
Faible consommation mémoire : La mémoire est dynamique et partagée avec Windows (quelques Mo pour les conteneurs vs plusieurs Go pour une VM).
Intégration native : Accès direct via localhost, partage de fichiers entre Windows et Linux, CLI PowerShell compatible.
Performance : Les conteneurs bénéficient des performances quasi-natives du noyau Linux sans la surcharge d'un hyperviseur complet.
En résumé, WSL 2 permet à Docker Desktop d'offrir une expérience Linux native sous Windows, combinant la légèreté des conteneurs avec l'intégration parfaite à l'environnement Windows, ce qui en fait la solution idéale pour le développement et le déploiement d'applications conteneurisées.


> ### 📝 À rendre en fin de séance
> Une fiche d'une page contenant : 
