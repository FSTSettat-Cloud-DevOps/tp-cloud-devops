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

### Étape A — Vérifier l'installation (5 min)

```bash
docker --version
docker version
docker info | head -n 20
docker run hello-world
```

Noter la version du client, celle du serveur, le nombre d'images et de conteneurs indiqué par `docker info`. Lire le message affiché par `hello-world` et recopier les étapes qu'il décrit.

---

### Étape B — Premier serveur web (15 min)

```bash
docker run -d --name monweb -p 8080:80 nginx
docker ps
curl http://localhost:8080
docker port monweb
docker logs monweb
docker logs -f monweb
```

Pour la dernière commande, ouvrir un second terminal, exécuter `curl http://localhost:8080` et observer la ligne de journal produite ; arrêter le suivi avec `Ctrl+C`.

**Questions :** Quelle est la signification de chaque colonne de `docker ps` ? Que se passerait-il si l'option `-d` était omise ?

---

### Étape C — Explorer un conteneur en cours d'exécution (15 min)

```bash
docker exec -it monweb bash
cat /etc/os-release | head -n 3
ls /usr/share/nginx/html
echo "<h1>Bonjour Docker</h1>" > /usr/share/nginx/html/index.html
exit
curl http://localhost:8080
docker inspect -f '{{.NetworkSettings.IPAddress}}' monweb
docker inspect -f '{{.State.Status}}' monweb
```

**Questions :** Quel système d'exploitation voit-on dans le conteneur ? Est-il identique à celui de la VM ? Quel noyau le conteneur utilise-t-il (`uname -r` dans le conteneur et dans la VM) ?

---

### Étape D — Cycle de vie d'un conteneur (10 min)

```bash
docker stop monweb
docker ps
docker ps -a
docker start monweb
curl http://localhost:8080
docker rm -f monweb
docker run -d --name monweb -p 8080:80 nginx
curl http://localhost:8080
```

**Observer et expliquer :** Après `stop` puis `start`, quel message la page affiche-t-elle ? Et après la suppression suivie de la recréation ? Que peut-on en déduire sur la persistance des données écrites dans un conteneur ?

---

### Étape E — Mini-exercice Redis (15 min)

1. Créer et démarrer, en arrière-plan, un conteneur `cache01` à partir de l'image `redis`.
2. Afficher tous les conteneurs, démarrés ou arrêtés.
3. Ouvrir un terminal Bash dans `cache01`, puis exécuter `redis-cli ping`.
4. Dans `redis-cli` (lancé via `docker exec -it cache01 redis-cli`), stocker puis relire une valeur avec `SET module cloud` et `GET module`.
5. Que se passe-t-il si l'on exécute `docker run redis` sans `-d` ? Comment sortir proprement ?

---

### Étape F — Plusieurs conteneurs, une seule image : mesures (15 min)

```bash
docker run -d --name web1 -p 8081:80 nginx
docker run -d --name web2 -p 8082:80 nginx
docker ps
docker images
docker stats --no-stream
time docker run --rm alpine echo "bonjour"
```

Compléter le tableau ci-dessous, puis mesurer (chronomètre) le temps de démarrage d'une VM VirtualBox comparable et le comparer à celui du conteneur.

| Mesure | nginx | alpine |
| :--- | :---: | :---: |
| Taille de l'image (`docker images`) | | |
| Mémoire utilisée par un conteneur (`docker stats`) | | --- |
| Temps de démarrage (`time docker run`) | --- | |
| Nombre d'images pour `web1` et `web2` | \multicolumn{2}{c\|}{} |

Nettoyer ensuite l'environnement :
```bash
docker rm -f web1 web2 monweb cache01
docker ps -a
```

---

> ### 📝 À rendre en fin de séance
> Une fiche d'une page contenant : 
> 1. Le tableau de l'étape F complété.
> 2. Les réponses aux questions des étapes B à E.
> 3. Trois commandes que vous avez utilisées avec une phrase d'explication chacune.

---

<details>
<summary><b>💡 Corrigé de la Partie TP (Cliquer pour dérouler)</b></summary>

* **Étape A :** `docker version` affiche deux sections (Client et Server/Engine) car le client et le démon sont deux composants distincts. Le message de `hello-world` décrit : 
  1. Le client contacte le démon.
  2. Le démon télécharge l'image depuis Docker Hub.
  3. Il crée un conteneur qui produit le message.
  4. Le flux est envoyé au terminal.

* **Étape B :** 
  * **Colonnes :** `CONTAINER ID`, `IMAGE`, `COMMAND`, `CREATED`, `STATUS`, `PORTS` (redirection `0.0.0.0:8080->80/tcp`), `NAMES`.
  * `curl` renvoie la page « Welcome to nginx! ». 
  * Sans `-d`, le conteneur reste au premier plan et bloque le terminal ; `Ctrl+C` l'arrête.

* **Étape C :** Le conteneur affiche Debian (image officielle Nginx) alors que la VM est sous Ubuntu : le *userland* diffère. En revanche `uname -r` renvoie **le même noyau** dans le conteneur et dans la VM : preuve que le noyau est partagé.

* **Étape D :** Après `stop`/`start`, le message modifié (« Bonjour Docker ») est conservé. Après `rm` et recréation, c'est la page d'origine de Nginx : la couche modifiable disparaît avec le conteneur $\Rightarrow$ nécessité des volumes (Série 3).

* **Étape E :**
  ```bash
  docker run -d --name cache01 redis
  docker ps -a
  docker exec -it cache01 bash
  redis-cli ping         # Réponse: PONG
  ```
  Avec `SET module cloud` on obtient `OK`, puis `GET module` renvoie `"cloud"`. Sans `-d`, Redis journalise au premier plan ; `Ctrl+C` arrête le conteneur (ou `docker stop` depuis un autre terminal).

* **Étape F :** 
  * **Ordres de grandeur :** Image `alpine` de quelques Mo contre plusieurs dizaines à centaines de Mo pour `nginx`.
  * Mémoire d'un conteneur Nginx de quelques Mo.
  * Démarrage d'`alpine` en une fraction de seconde (quelques secondes au plus), contre des dizaines de secondes à minutes pour une VM.
  * `web1` et `web2` partagent **une seule** image.

</details>