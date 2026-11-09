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
> **Nom :**  
> **Prénom :**  
> **Groupe / Filère :**  
> **Date :**  

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
# Votre réponse ici :
```

2. **On considère que le Dockerfile de l'API se trouve dans le dossier courant. Comment demander à Compose de construire cette image ?**

> **Réponse :**  

3. **Faut-il également déclarer le réseau créé au début dans le fichier Compose ? Justifier votre réponse.**

> **Réponse :**  

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

2. **Que garantit exactement `depends_on` ? Que ne garantit-il pas ? Quel risque cela crée-t-il pour l'API au démarrage ?**

> **Réponse :**  

3. **Quelle est la différence entre `docker compose down` et `docker compose down -v` ? Laquelle conserve les données de la base ?**

> **Réponse :**  

4. **Comment l'API joint-elle la base de données sur le réseau ?**

> **Réponse :**  

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
| 1 | `FROM ubuntu:latest` | | |
| 2 | `RUN apt-get update` | | |
| 3 | `COPY . /app` | | |
| 4 | `ENV DB_PASSWORD=...` | | |
| 5 | Exécution utilisateur | | |
| 6 | Optimisation / Nettoyage | | |

2. **Proposer une version corrigée et optimisée du Dockerfile :**

```dockerfile
# Proposer votre Dockerfile corrigé ici
```

---

### Exercice 4 — Multi-stage et CI/CD (10 min)

1. **Expliquer le principe d'un build *multi-stage* et ses deux principaux avantages.**

> **Réponse :**  

2. **Replacer dans un ordre logique les 5 opérations CI/CD suivantes :**  
   `docker push`, `déploiement`, `push du code`, `tests automatisés`, `docker build`.

> **Ordre chronologique :**  
> 1.  
> 2.  
> 3.  
> 4.  
> 5.  

3. **Pourquoi dit-on que Docker rend le déploiement reproductible ? Pourquoi éviter le tag `latest` pour les images déployées ?**

> **Réponse :**  

4. **Docker Compose peut-il remplacer Kubernetes pour une application de grande taille ? Justifier.**

> **Réponse :**  

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

2. **Comparer ce comportement avec le `depends_on: [db]` classique de l'exercice 2 du TD.**
> **Explications :**  

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
> **Résultat après `docker compose down -v` :**  

2. **Noter le message obtenu si vous interrogez `/etudiants` juste après `down -v` (avant `/init`) et expliquer son origine :**
> **Message d'erreur / Code HTTP :**  
> **Explication :**  

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

2. **Que se passe-t-il après le redémarrage de la base (`docker compose start db`) ?**
> **Résultat :**  

3. **Expliquer le rôle de la boucle de tentatives présente dans la fonction `get_conn` de `app.py` :**
> **Explication :**  

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
> **Résultat via `localhost:5000` :**  

2. **Expliquer le rôle de Nginx, le type de montage utilisé pour `nginx.conf` et l'intérêt de l'option `:ro` :**
> **Explications :**  

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
| `site-single:1.0` | | |
| `site-multi:1.0` | | |

2. **En vous appuyant sur vos observations, expliquer l'intérêt du multi-stage dans un projet réel (Node.js, Go, Java, C++) :**
> **Explications :**  

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
> **Utilisateur API :**  
> **Utilisateur Alpine :**  

2. **Interpréter le résultat de la commande `touch /etc/test` dans le conteneur API :**
> **Résultat & Explication :**  

3. **Que constatez-vous en observant la sortie de `docker inspect` concernant `DATABASE_URL` ? Quelles précautions faut-il prendre pour les secrets en production ?**
> **Constat :**  
> **Recommandations de sécurité :**  

---

### 📦 Livrable à rendre
À la fin de la séance, vous devez fournir :
1. Ce fichier Markdown dûment complété.
2. Le dossier `etudiants-api` contenant : `Dockerfile`, `app.py`, `requirements.txt`, `docker-compose.yml`, et `nginx.conf`.
