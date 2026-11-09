# Module Cloud Computing, Virtualisation & DevOps
**Université Hassan 1er — FST Settat**  
**Département Informatique** — Année Universitaire : 2026–2027  
**Enseignant :** Pr. Abdelfattah Abassi  

---

## Série 6 — Docker Compose, bonnes pratiques et CI/CD
**Durée :** 2 h (TD : 40 min ; TP : 80 min)  
**Chapitre :** Conteneurisation — Mise en pratique de Compose, sécurisation et automatisation

---

### Informations de l'étudiant(e)
> **Nom :**  BOUGHIJA_JEMI
> **Prénom :**  NADA_MERIEM
> **Groupe / Filère :**  IRISTI
> **Date :**  09/11/2026

---

### Description & Objectifs

Cette séance prolonge les manipulations réalisées avec les conteneurs Docker. L'objectif est de faire fonctionner plusieurs services ensemble, puis d'observer le comportement du système en cas d'indisponibilité de la base de données, de gestion de la persistance ou de modification de l'accès à l'API.

**À la fin de la séance, vous devrez être en mesure de :**
- Regrouper plusieurs commandes `docker run` dans un fichier `docker-compose.yml` ;
- Lancer une application composée d'une API Flask et d'une base PostgreSQL tout en conservant les données ;
- Distinguer le démarrage d'un conteneur de la disponibilité effective du service hébergé (via *healthcheck*) ;
- Auditer un `Dockerfile` (optimisation de taille, cache, sécurité et gestion des secrets) ;
- Expliquer l'intégration de Docker dans un pipeline CI/CD et ses limites par rapport à Kubernetes.

---

## Partie 1 : Travaux Dirigés (TD - 40 min)

### Exercice 1 — De `docker run` à Compose (10 min)

À partir des commandes shell suivantes :

```bash
docker network create appnet
docker volume create pgdata
docker run -d --name db --network appnet \
  -v pgdata:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret postgres:15
docker run -d --name api --network appnet -p 5000:5000 \
  -e DATABASE_URL=postgresql://postgres:secret@db:5432/postgres monapi:1.0
```

1. **Rédiger le fichier `docker-compose.yml` correspondant :**

```yaml
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secret
    volumes:
      - pgdata:/var/lib/postgresql/data
    networks:
      - appnet

  api:
    image: monapi:1.0
    ports:
      - "5000:5000"
    environment:
      DATABASE_URL: postgresql://postgres:secret@db:5432/postgres
    networks:
      - appnet

volumes:
  pgdata:

networks:
  appnet:

```

2. **On considère que le Dockerfile de l'API se trouve dans le dossier courant. Comment demander à Compose de construire cette image ?**

> **Réponse :**
>Il faut utiliser l'instruction build: . dans la définition du service api. Cela indique à Docker Compose de construire l'image à partir du Dockerfile situé dans le répertoire courant (.). On peut conserver image: monapi:1.0 pour que l'image construite soit automatiquement taguée avec ce nom.

3. **Faut-il également déclarer le réseau créé au début dans le fichier Compose ? Justifier votre réponse.**

> **Réponse : **
> Non, ce n'est pas strictement nécessaire. Docker Compose crée automatiquement un réseau par défaut (nommé <nom_du_projet>_default) qui relie tous les services déclarés, permettant à l'API de joindre la base de données via le nom d'hôte db.
Cependant, si l'on souhaite réutiliser le réseau appnet créé manuellement via docker network create, il faut le déclarer dans la section networks du fichier Compose en précisant external: true.

---

### Exercice 2 — Comprendre un fichier Compose (10 min)

Examinez le fichier `docker-compose.yml` ci-dessous :

```yaml
services:
  api:
    build: .
    ports: ["5000:5000"]
    depends_on: [db]
  db:
    image: postgres:15
    volumes: ["data_db:/var/lib/postgresql/data"]
    environment: ["POSTGRES_PASSWORD=secret"]
volumes:
  data_db:
```

1. **Quelle est la différence entre `build:` et `image:` ?**

> **Réponse :**
> build: indique à Docker Compose de construire une image personnalisée à partir d'un Dockerfile situé dans le chemin spécifié (ici . signifie le répertoire courant).
image: indique à Docker Compose d'utiliser une image déjà construite, qui sera soit recherchée localement, soit téléchargée depuis un registre public ou privé (comme Docker Hub pour postgres:15).

2. **Que garantit exactement `depends_on` ? Que ne garantit-il pas ? Quel risque cela crée-t-il pour l'API au démarrage ?**

> **Réponse :**
> Ce qu'il garantit : Il garantit uniquement l'ordre de démarrage des conteneurs. Docker Compose s'assurera que le conteneur db est bien créé et démarré avant le conteneur api.
Ce qu'il ne garantit pas : Il ne garantit absolument pas que le service applicatif à l'intérieur du conteneur (ici le serveur PostgreSQL) soit réellement prêt à accepter des connexions. Le conteneur peut être "up" alors que la base de données est encore en phase d'initialisation.
Le risque : L'API peut démarrer et tenter de se connecter à la base de données trop tôt, ce qui provoquera une erreur de connexion (ex: Connection refused) et potentiellement un crash de l'application au démarrage. (C'est pour cela que le TP introduit la notion de healthcheck et de condition: service_healthy).

3. **Quelle est la différence entre `docker compose down` et `docker compose down -v` ? Laquelle conserve les données de la base ?**

> **Réponse :**
> docker compose down arrête les conteneurs et les supprime, ainsi que les réseaux créés par Compose. Cependant, il conserve les volumes nommés (comme data_db).
docker compose down -v effectue les mêmes opérations, mais supprime également les volumes nommés déclarés dans la section volumes du fichier Compose.
Conservation des données : C'est donc docker compose down (sans l'option -v) qui conserve les données de la base de données, car le volume persistant n'est pas détruit.

4. **Comment l'API joint-elle la base de données sur le réseau ?**

> **Réponse :**
> Par défaut, Docker Compose crée un réseau virtuel privé dédié à l'application et y connecte tous les services. Il met en place un DNS interne qui permet aux conteneurs de se résoudre entre eux en utilisant le nom de leur service. L'API joint donc la base de données simplement en utilisant le nom d'hôte db (qui correspond au nom du service de la base dans le fichier Compose), par exemple via l'URL : postgresql://postgres:secret@db:5432/postgres.

---

### Exercice 3 — Audit d'un Dockerfile (10 min)

Voici un Dockerfile à analyser :

```dockerfile
FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python3 python3-pip curl
COPY . /app
ENV DB_PASSWORD=admin123
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]
```

1. **Relever au moins 6 points à améliorer (problème + correction proposée) :**

| # | Élément / Ligne | Problème identifié | Correction proposée |
|---|----------------|--------------------|---------------------|
| 1 | `FROM ubuntu:latest` |Le tag latest n'est pas reproductible (l'image peut changer sans préavis). De plus, ubuntu est une image lourde pour une simple app Python. |Utiliser une version figée (ex: ubuntu:22.04) ou mieux, une image légère et spécialisée comme python:3.11-slim. |
| 2 | `RUN apt-get update` | Séparer update et install en deux couches RUN brise le cache Docker et peut mener à des incohérences. Aucun nettoyage n'est fait, ce qui alourdit l'image.| Combiner les commandes en une seule ligne et nettoyer le cache : RUN apt-get update && apt-get install -y ... && rm -rf /var/lib/apt/lists/*|
| 3 | `COPY . /app` |Copier tout le code source avant d'installer les dépendances invalide le cache Docker à chaque modification du code, rendant les builds lents. | Copier d'abord requirements.txt, lancer pip install, puis copier le reste du code source (COPY . .).|
| 4 | `ENV DB_PASSWORD=...` |Faille de sécurité critique : les secrets en dur dans le Dockerfile sont visibles dans l'historique des couches (docker history) et via docker inspect. | Supprimer cette ligne. Injecter le mot de passe à l'exécution via les variables d'environnement de Compose ou un gestionnaire de secrets.|
| 5 | Exécution utilisateur | Par défaut, le conteneur s'exécute en tant que root. En cas de faille dans l'application, l'attaquant a les privilèges maximaux dans le conteneur.| Créer un utilisateur non-privilégié (ex: appuser) et basculer vers lui avec l'instruction USER appuser avant le CMD.|
| 6 | Optimisation / Nettoyage | L'installation de pip conserve son cache, et le WORKDIR est déclaré tardivement, ce qui est une mauvaise pratique de lecture.|Déplacer WORKDIR /app juste après le FROM. Ajouter --no-cache-dir à la commande pip install. |

2. **Proposer une version corrigée et optimisée du Dockerfile :**

```dockerfile
# 1. Utiliser une image de base légère et avec un tag de version fixe
FROM python:3.11-slim

# 2. Définir le répertoire de travail dès le début
WORKDIR /app

# 3. Copier uniquement le fichier de dépendances pour optimiser le cache Docker
COPY requirements.txt .

# 4. Installer les dépendances sans garder le cache, puis nettoyer (si apt était utilisé)
RUN pip3 install --no-cache-dir -r requirements.txt

# 5. Copier le reste du code source de l'application
COPY . .

# 6. Créer un utilisateur non-root pour des raisons de sécurité
RUN useradd -m appuser
USER appuser

# 7. La variable DB_PASSWORD doit être passée à l'exécution (via docker-compose), pas ici.
CMD ["python3", "app.py"]
```

---

### Exercice 4 — Multi-stage et CI/CD (10 min)

1. **Expliquer le principe d'un build *multi-stage* et ses deux principaux avantages.**

> **Réponse :**
> Le build multi-stage consiste à utiliser plusieurs instructions FROM dans un même Dockerfile. La première étape (le "builder") contient tous les outils de compilation et les dépendances de développement. La seconde étape (l'image finale) est une image minimale dans laquelle on ne copie (COPY --from=builder) que les artefacts compilés ou nécessaires à l'exécution.
Avantages :
Réduction drastique de la taille de l'image finale (pas d'outils de build, de code source ou de fichiers temporaires).
Sécurité améliorée : la surface d'attaque est réduite et les secrets ou outils de compilation ne sont pas présents dans l'image livrée en production.

2. **Replacer dans un ordre logique les 5 opérations CI/CD suivantes :**  
   `docker push`, `déploiement`, `push du code`, `tests automatisés`, `docker build`.

> **Ordre chronologique :**  
> 1.  push du code (le développeur envoie ses modifications sur le dépôt Git).
> 2.  tests automatisés (le pipeline CI vérifie que le code fonctionne et respecte les standards).
> 3.  docker build (si les tests passent, l'image Docker est construite).
> 4.  docker push (l'image construite est envoyée vers un registre d'images, ex: Docker Hub, GitLab Registry).
> 5.  déploiement (le système de déploiement récupère cette image spécifique et la lance en production).

3. **Pourquoi dit-on que Docker rend le déploiement reproductible ? Pourquoi éviter le tag `latest` pour les images déployées ?**

> **Réponse :**
> Docker rend le déploiement reproductible car il empaquette l'application avec toutes ses dépendances, bibliothèques système et sa configuration dans une image immuable. Elle s'exécutera donc exactement de la même manière sur la machine du développeur, le serveur CI et la production.
Il faut éviter le tag latest car c'est un tag mutable (il peut pointer vers une image différente à chaque nouveau build). Cela brise la reproductibilité, rend les rollbacks (retours en arrière) impossibles ou dangereux, et peut introduire des régressions inattendues en production. Il faut toujours utiliser des tags de version sémantique (ex: v1.2.3) ou des hash de commit Git.

4. **Docker Compose peut-il remplacer Kubernetes pour une application de grande taille ? Justifier.**

> **Réponse :**  
Non. Docker Compose est conçu pour orchestrer des conteneurs sur une seule machine hôte (idéal pour le développement, les tests ou de très petits déploiements).
Pour une application de grande taille, Kubernetes est nécessaire car il offre des fonctionnalités natives de cluster multi-nœuds que Compose ne possède pas : le mise à l'échelle automatique (auto-scaling), l'auto-guérison (redémarrage ou replanification automatique des pods en cas de panne matérielle), le déploiement continu sans interruption (rolling updates), et une gestion avancée du réseau et des secrets à l'échelle.
---

## Partie 2 : Travaux Pratiques (TP - 80 min)

> ⚠️ **Attention :** Travailler dans le dossier `~/tp4/etudiants-api`. Avant de commencer, s'assurer de libérer les ports 5000 et 8080 (`docker ps -a`).

### Étape A — Construire l'application Flask + PostgreSQL (20 min)

Fichiers fournis dans le projet :

- **`requirements.txt`**
  ```text
  Flask==3.1.2
  psycopg2-binary==2.9.10
  ```

- **`app.py`**
  ```python
  import os
  import time
  import psycopg2
  from flask import Flask, jsonify

  app = Flask(__name__)
  DSN = os.environ.get("DATABASE_URL", "postgresql://postgres:secret@db:5432/postgres")

  def get_conn():
      for _ in range(10):
          try:
              return psycopg2.connect(DSN)
          except psycopg2.OperationalError:
              time.sleep(1)
      raise RuntimeError("Base indisponible")

  @app.route("/")
  def accueil():
      return "API etudiants operationnelle"

  @app.route("/init")
  def init():
      with get_conn() as conn, conn.cursor() as cur:
          cur.execute("CREATE TABLE IF NOT EXISTS etudiants (id SERIAL PRIMARY KEY, nom TEXT NOT NULL)")
          return "Table creee"

  @app.route("/ajouter/<nom>")
  def ajouter(nom):
      with get_conn() as conn, conn.cursor() as cur:
          cur.execute("INSERT INTO etudiants (nom) VALUES (%s)", (nom,))
          return nom + " ajoute"

  @app.route("/etudiants")
  def liste():
      with get_conn() as conn, conn.cursor() as cur:
          cur.execute("SELECT id, nom FROM etudiants ORDER BY id")
          return jsonify(cur.fetchall())

  if __name__ == "__main__":
      app.run(host="0.0.0.0", port=5000)
  ```

- **`Dockerfile`**
  ```dockerfile
  FROM python:3.11-slim
  WORKDIR /app
  COPY wheels /wheels
  COPY requirements.txt .
  RUN pip install --no-cache-dir --no-index --find-links=/wheels -r requirements.txt
  COPY app.py .
  RUN adduser --disabled-password --gecos "" appuser
  USER appuser
  EXPOSE 5000
  CMD ["python", "app.py"]
  ```

- **`docker-compose.yml`**
  ```yaml
  services:
    api:
      build: .
      ports:
        - "5000:5000"
      environment:
        DATABASE_URL: postgresql://postgres:secret@db:5432/postgres
      depends_on:
        db:
          condition: service_healthy
    db:
      image: postgres:15
      environment:
        POSTGRES_PASSWORD: secret
      volumes:
        - data_db:/var/lib/postgresql/data
      healthcheck:
        test: ["CMD-SHELL", "pg_isready -U postgres"]
        interval: 3s
        timeout: 3s
        retries: 10
  volumes:
    data_db:
  ```

**Commandes à exécuter :**
```bash
docker compose config
docker compose up -d --build
docker compose ps
curl http://localhost:5000/init
curl http://localhost:5000/ajouter/Aya
curl http://localhost:5000/ajouter/Youssef
curl http://localhost:5000/etudiants
docker compose logs -f api
```

#### 🔍 Compte-rendu Étape A :
1. **Observer la colonne d'état de `db` avec `docker compose ps`. À quel moment le statut `healthy` apparaît-il ?**
> **Observations :**
> Le statut healthy n'apparaît pas immédiatement au démarrage. Le conteneur db affiche d'abord Up. Il faut attendre environ 30 secondes (le temps que le healthcheck réussisse 10 fois toutes les 3 secondes) pour voir Up (healthy). Cela signifie que PostgreSQL a fini son initialisation interne et accepte réellement les connexions TCP.

2. **Comparer ce comportement avec le `depends_on: [db]` classique de l'exercice 2 du TD.**
> **Explications :**
> Avec depends_on: [db] (syntaxe simple), Docker Compose attend uniquement que le conteneur db soit démarré (Up), mais pas que le service PostgreSQL soit prêt. L'API peut donc tenter une connexion avant que la base ne soit initialisée, causant une erreur "Connection refused". Avec condition: service_healthy, Compose bloque le démarrage de l'API jusqu'à ce que la base soit officiellement opérationnelle, garantissant ainsi une connexion fiable dès le lancement.

---

### Étape B — Persistance des données (10 min)

**Commandes à exécuter :**
```bash
docker compose down
docker compose up -d
curl http://localhost:5000/etudiants

docker compose down -v
docker compose up -d
curl http://localhost:5000/etudiants
curl http://localhost:5000/init
curl http://localhost:5000/etudiants
```

#### 🔍 Compte-rendu Étape B :
1. **Comparer le contenu de la table après `down` puis après `down -v` :**
> **Résultat après `docker compose down` :**
> La commande curl http://localhost:5000/etudiants retourne les données précédemment ajoutées (ex: [["Aya",1],["Youssef",2]]). Les données sont conservées car le volume nommé data_db est indépendant du cycle de vie des conteneurs et n'a pas été supprimé.
> 
> **Résultat après `docker compose down -v` :**
> La base de données est entièrement réinitialisée. Si on interroge /etudiants sans avoir appelé /init au préalable, la requête échoue car la base est vide.

2. **Noter le message obtenu si vous interrogez `/etudiants` juste après `down -v` (avant `/init`) et expliquer son origine :**
> **Message d'erreur / Code HTTP :**
> Message d'erreur / Code HTTP :
Erreur 500 Internal Server Error (avec un message Flask/psycopg2 indiquant relation "etudiants" does not exist).
> **Explication :**
> L'option -v a définitivement détruit le volume data_db contenant les anciennes données. Au redémarrage (up -d), le conteneur PostgreSQL a initialisé une base de données toute neuve et vide. Comme la route /init (qui contient la commande SQL CREATE TABLE) n'a pas encore été exécutée, la table etudiants n'existe pas physiquement. La requête SELECT de la route /etudiants échoue donc immédiatement.

---

### Étape C — Panne de la base et tolérance de l'API (10 min)

**Commandes à exécuter :**
```bash
docker compose stop db
curl -m 20 http://localhost:5000/etudiants
docker compose start db
curl http://localhost:5000/etudiants
docker compose logs api | tail -n 20
docker compose exec db psql -U postgres -c "SELECT count(*) FROM etudiants;"
```

#### 🔍 Compte-rendu Étape C :
1. **Quel est le résultat de la requête lorsque PostgreSQL est arrêté ?**
> **Résultat :**
> > La commande curl -m 20 http://localhost:5000/etudiants met environ 10 secondes à répondre, puis retourne une erreur *500 Internal Server Error* avec le message "Base indisponible".


2. **Que se passe-t-il après le redémarrage de la base (`docker compose start db`) ?**
> **Résultat :**
> La fonction get_conn() essaie de se connecter 10 fois avec une pause d'une seconde (time.sleep(1)) entre chaque essai. Cela permet à l'API de survivre temporairement à une panne courte de la base de données ou à un démarrage lent de PostgreSQL, au lieu de crasher immédiatement à la première tentative échouée.

3. **Expliquer le rôle de la boucle de tentatives présente dans la fonction `get_conn` de `app.py` :**
> **Explication :**
> > La commande curl http://localhost:5000/etudiants fonctionne à nouveau normalement et retourne les données, prouvant que l'API s'est reconnectée avec succès.

---

### Étape D — Ajouter un proxy Nginx (15 min)

1. **Créer le fichier `nginx.conf` :**
```nginx
server {
    listen 80;
    location / {
        proxy_pass http://api:5000;
    }
}
```

2. **Modifier `docker-compose.yml` :** Supprimer la section `ports` du service `api` et ajouter le service `proxy` :
```yaml
  proxy:
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf:ro
    depends_on:
      - api
```

3. **Exécuter les commandes suivantes :**
```bash
docker compose up -d
curl http://localhost:8080/etudiants
curl -m 3 http://localhost:5000/etudiants
docker compose ps
```

#### 🔍 Compte-rendu Étape D :
1. **Comparer l'accès à l'API via le port 8080 et via le port 5000 :**
> **Résultat via `localhost:8080` :**
> curl http://localhost:8080/etudiants fonctionne et retourne les données après initialisation. En revanche, curl -m 3
> **Résultat via `localhost:5000` :**  
http://localhost:5000/etudiants échoue avec une erreur de connexion ("Could not connect to server"). Cela confirme que la section ports a bien été supprimée du service api : l'API est désormais isolée et n'est accessible que via le proxy.
2. **Expliquer le rôle de Nginx, le type de montage utilisé pour `nginx.conf` et l'intérêt de l'option `:ro` :**
> **Explications :**  
Nginx agit comme un *reverse proxy* (mandataire inverse). Il écoute sur le port 80 de son conteneur (mappé sur le port 8080 de l'hôte) et transfère toutes les requêtes reçues vers http://api:5000 via le réseau interne Docker. Cela masque l'architecture interne et centralise l'accès.
> > Le montage ./nginx.conf:/etc/nginx/conf.d/default.conf:ro est un *bind mount* (montage lié). L'option :ro (read-only) monte le fichier en *lecture seule* dans le conteneur. Cela empêche le processus Nginx de modifier accidentellement notre fichier de configuration local, améliorant ainsi la sécurité.
---

### Étape E — Build multi-stage (15 min)

Dans `~/tp4/multistage`, créer deux Dockerfiles :

- **`Dockerfile.single`**
  ```dockerfile
  FROM nginx:alpine
  RUN dd if=/dev/zero of=/tmp/gros_fichier bs=1M count=50 \
      && echo "<h1>Site statique</h1>" > /usr/share/nginx/html/index.html
  ```

- **`Dockerfile.multi`**
  ```dockerfile
  FROM alpine AS build
  RUN mkdir /site \
      && dd if=/dev/zero of=/tmp/gros_fichier bs=1M count=50 \
      && echo "<h1>Site statique</h1>" > /site/index.html

  FROM nginx:alpine
  COPY --from=build /site/index.html /usr/share/nginx/html/index.html
  ```

**Commandes à exécuter :**
```bash
docker build -f Dockerfile.single -t site-single:1.0 .
docker build -f Dockerfile.multi -t site-multi:1.0 .
docker images | grep site-
docker run -d --name s1 -p 8083:80 site-multi:1.0
curl http://localhost:8083
docker run --rm site-multi:1.0 ls /tmp
docker run --rm site-single:1.0 ls -lh /tmp
```

#### 🔍 Compte-rendu Étape E :

1. **Remplir le tableau comparatif :**

| Image | Taille (Ordre de grandeur) | Contenu du dossier `/tmp` |
|-------|----------------------------|---------------------------|
| `site-single:1.0` | 146 Mo|Présent (gros_fichier de 50 Mo) |
| `site-multi:1.0` |94 Mo | Absent (dossier vide)|

2. **En vous appuyant sur vos observations, expliquer l'intérêt du multi-stage dans un projet réel (Node.js, Go, Java, C++) :**
> **Explications :**  
> L'observation montre que l'image multi-stage est plus légère (~94 Mo contre ~146 Mo) et, surtout, qu'elle ne contient pas le fichier temporaire de 50 Mo généré lors de la construction. 
> Dans un projet réel (Node.js, Go, Java, C++), l'intérêt est majeur : 
> 1. *Réduction drastique de la taille* : On utilise une première image lourde (avec compilateurs, SDK, node_modules) uniquement pour la compilation (AS build), puis on copie uniquement l'artefact final (binaire ou fichiers statiques) dans une seconde image minimale (ex: alpine).
> 2. *Sécurité accrue* : L'image de production ne contient pas les outils de développement, réduisant ainsi la surface d'attaque.
> 3. *Propreté* : Les fichiers temporaires de compilation (comme notre gros_fichier) sont définitivement exclus de l'image finale, ce qui accélère les déploiements (docker pull) et économise l'espace disque.
---

### Étape F — Sécurité et nettoyage (10 min)

**Commandes à exécuter :**
```bash
docker compose exec api whoami
docker run --rm alpine whoami
docker compose exec api touch /etc/test
docker compose exec api sh -c 'echo $DATABASE_URL'
docker inspect $(docker compose ps -q api) | grep -i DATABASE_URL
docker rm -f s1
docker compose down -v
docker system df
```

#### 🔍 Compte-rendu Étape F :
1. **Quel est l'utilisateur de l'API vs l'utilisateur par défaut de l'image Alpine ?**
> **Utilisateur API :**   appuser (utilisateur non-privilégié créé spécifiquement dans le Dockerfile).
> **Utilisateur Alpine :**  > root (administrateur système par défaut des conteneurs Linux).  


2. **Interpréter le résultat de la commande `touch /etc/test` dans le conteneur API :**
> **Résultat & Explication :**
>  La commande retourne *Permission denied*. Cela confirme que l'utilisateur appuser n'a pas les droits d'écriture sur les répertoires système protégés comme /etc. En cas de compromission de l'application (ex: injection de code), l'attaquant ne pourra pas modifier la configuration système ni installer de logiciels malveillants persistants, limitant ainsi considérablement la surface d'attaque (principe du moindre privilège).

3. **Que constatez-vous en observant la sortie de `docker inspect` concernant `DATABASE_URL` ? Quelles précautions faut-il prendre pour les secrets en production ?**
> **Constat :**  La variable DATABASE_URL (contenant le mot de passe secret) apparaît *en clair* dans la configuration JSON du conteneur affichée par docker inspect. Toute personne ayant accès au démon Docker peut lire ce secret.
> **Recommandations de sécurité :**  > Il ne faut jamais écrire de vrais mots de passe ou clés API en dur dans le fichier docker-compose.yml. En production, il faut utiliser :
> - Un fichier .env externe (impérativement ajouté au .gitignore).
> - Docker Secrets (si on utilise Docker Swarm).
> - Un gestionnaire de secrets externe dédié (comme HashiCorp Vault, AWS Secrets Manager ou Azure Key Vault).

---

### 📦 Livrable à rendre
À la fin de la séance, vous devez fournir :
1. Ce fichier Markdown dûment complété.
2. Le dossier `etudiants-api` contenant : `Dockerfile`, `app.py`, `requirements.txt`, `docker-compose.yml`, et `nginx.conf`.
   [etudiants-api.zip](https://github.com/user-attachments/files/34601331/etudiants-api.zip)

