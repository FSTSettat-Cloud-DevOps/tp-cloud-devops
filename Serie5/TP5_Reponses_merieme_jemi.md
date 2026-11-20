# TP n°5 — Docker Compose : premiers pas — Fiche de réponses

**Module :** Cloud Computing, Virtualisation & DevOps — FST Settat, Université Hassan 1er
**Enseignant :** Pr. Abdelfattah Abassi

| | |
|---|---|
| **Nom** | *Boughija_jemi* |
| **Prénom** | *Nada_Meriem* |
| **Groupe / Filière** | *IRISTI* |
| **Date** | *02/11/2026* |

---

## Comment remplir ce fichier

1. Renommer le fichier en `TP5_Reponses_NOM_Prenom.md`.
2. Ouvrir le fichier dans un éditeur de texte (VS Code, par exemple ; l'aperçu Markdown permet de voir le rendu).
3. **Ne pas modifier les titres.** Écrire chaque réponse **à la place** de la ligne `*(écrire votre réponse ici)*`.
4. **Sorties de terminal :** les copier-coller **à l'intérieur** des blocs de code prévus (entre les deux lignes de trois apostrophes inversées).
5. **Captures d'écran :** enregistrer l'image dans un dossier `images/` placé à côté de ce fichier, puis remplacer le nom dans la ligne `![...](images/...)`.
6. Rendre le fichier **et** le dossier `images/` (par exemple dans une archive `.zip`).

> Exemple de réponse attendue : une à trois phrases claires, avec les mots de la question. Une commande copiée sans explication n'est pas une réponse.

---

## Partie 1 — Mon premier fichier Compose

### Trace 1.1 — état du service

Coller ici la sortie de `docker compose ps` (étape 1.4, service démarré) :

```

CONTAINER ID   IMAGE         COMMAND    CREATED       STATUS                   PORTS     NAMES
744d15f7a541   hello-world   "/hello"   2 hours ago   Exited (0) 2 hours ago             infallible_keldysh
PS C:\Users\fghjklmù> docker compose version
Docker Compose version v5.6.0
```

Coller ici la sortie de `docker network ls` (étape 1.4) :

```
NETWORK ID     NAME                  DRIVER    SCOPE
a7fda918d13d   bridge                bridge    local
c41e533e4875   host                  host      local
837660030ba1   none                  null      local
40c40a72a9f0   tp5-compose_default   bridge    local
```

### Q1.1 — En plus du conteneur, quel autre objet Docker a été créé par `docker compose up` ? Quel est son nom ?

**Réponse :**

Un réseau Docker a été créé automatiquement. Son nom est tp5-compose_default (format : nomdudossier_default).

### Q1.2 — Quelle est la différence entre `docker compose stop` et `docker compose down` ?

**Réponse :**

docker compose stop : arrête les conteneurs mais les conserve (on peut les redémarrer avec docker compose start).
docker compose down : arrête ET supprime les conteneurs + le réseau créé. Les données non volumées sont perdues.

---

## Partie 2 — Deux services qui communiquent

### Trace 2.1 — état des services

Coller ici la sortie de `docker compose ps` (étape 2.2) :

```
NAME                    IMAGE         COMMAND                  SERVICE   CREATED          STATUS          PORTS
tp5-compose-adminer-1   adminer       "entrypoint.sh docke…"   adminer   32 seconds ago   Up 28 seconds   0.0.0.0:8081->8080/tcp, [::]:8081->8080/tcp
tp5-compose-db-1        postgres:15   "docker-entrypoint.s…"   db        32 seconds ago   Up 28 seconds   5432/tcp
```

### Trace 2.2 — capture d'Adminer

Capture d'écran d'Adminer connecté à la base (étape 2.4) :

<img width="1583" height="617" alt="partie2_adminer png" src="https://github.com/user-attachments/assets/1ca48c9f-819a-45c2-a105-6643c7fb1180" />
### Q2.1 — Dans Adminer, pourquoi écrit-on `db` comme serveur et non `localhost` ?

**Réponse :**

Parce que les services Docker Compose communiquent entre eux via le réseau Docker interne créé automatiquement. Chaque service est joignable par son nom de service (ici db) qui est résolu en adresse IP par le DNS interne de Docker. localhost pointerait vers le conteneur Adminer lui-même, pas vers la base de données.
### Q2.2 — Lequel de ces deux services publie un port vers l'hôte ? Pourquoi le service `db` n'en a-t-il pas besoin ici ?

**Réponse :**

Seul le service adminer publie un port (8081:8080) car c'est lui qui doit être accessible depuis le navigateur Windows. Le service db n'a pas besoin de publier de port car il n'est utilisé que par Adminer (et potentiellement d'autres services) via le réseau interne Docker. Exposer la base de données directement sur l'hôte serait un risque de sécurité inutile.
---

## Partie 3 — Conserver les données avec un volume

### Trace 3.1 — données avant la suppression des conteneurs

Coller ici la sortie du dernier `SELECT * FROM etudiants;` de l'étape 3.3 :

```
PS C:\Users\fghjklmù\tp5-compose> docker compose exec db psql -U postgres -c "SELECT * FROM etudiants;"
 id | nom
----+------
  1 | Sara
(1 row)
```

### Trace 3.2 — données après `docker compose down` puis `up`

Coller ici la sortie du `SELECT * FROM etudiants;` de l'étape 3.4 :

```
PS C:\Users\fghjklmù\tp5-compose> docker compose exec db psql -U postgres -c "SELECT * FROM etudiants;"
 id | nom
----+------
  1 | Sara
(1 row)
```

### Trace 3.3 — volumes existants

Coller ici la sortie de `docker volume ls` (étape 3.5) :

```
DRIVER    VOLUME NAME
local     d785cadfc68f7a3cb9b1b72626c5117393753f1dff06ba539b61c2f3518a80a2
local     tp5-compose_data_db
```

### Q3.1 — Pourquoi les données sont-elles toujours là après `docker compose down` puis `up` ?

**Réponse :**

Parce que les données de PostgreSQL sont stockées dans un volume Docker nommé (data_db) qui est indépendant du cycle de vie des conteneurs. docker compose down supprime les conteneurs et le réseau, mais pas les volumes nommés. Quand le conteneur est recréé, il remonte le même volume et retrouve les données.

### Q3.2 — Que se serait-il passé sans la ligne `volumes` dans le service `db` ?

**Réponse :**

Sans volume, les données auraient été stockées dans le système de fichiers éphémère du conteneur. Après docker compose down, le conteneur est supprimé et toutes les données sont perdues définitivement 

---

## Partie 4 — Sortir le mot de passe avec un fichier `.env`

### Trace 4.1 — configuration interprétée

Coller ici la sortie de `docker compose config` (étape 4.3). **Masquer le mot de passe** si ce n'est pas la valeur d'exemple :

```
name: tp5-compose
services:
  adminer:
    image: adminer
    networks:
      default: null
    ports:
      - mode: ingress
        target: 8080
        published: "8081"
        protocol: tcp
  db:
    environment:
      POSTGRES_PASSWORD: secret
    image: postgres:15
    networks:
      default: null
    volumes:
      - type: volume
        source: data_db
        target: /var/lib/postgresql/data
        volume: {}
networks:
  default:
    name: tp5-compose_default
volumes:
  data_db:
    name: tp5-compose_data_db
```

### Q4.1 — Quel est l'intérêt d'un fichier `.env` plutôt que d'écrire le mot de passe dans `docker-compose.yml` ?

**Réponse :**

L'utilisation d'un fichier .env permet de séparer la configuration sensible du code. Cela offre deux avantages majeurs :
Sécurité : Les mots de passe et secrets ne sont pas écrits en clair dans le fichier docker-compose.yml.
Flexibilité : On peut adapter facilement les variables d'environnement (comme le mot de passe ou le port) selon l'environnement (développement, test, production) sans avoir à modifier le fichier YAML lui-même.

### Q4.2 — Pourquoi ne faut-il pas envoyer le fichier `.env` sur un dépôt Git partagé ?

**Réponse :**

Le fichier .env contient des informations sensibles en clair (comme les mots de passe, clés API, etc.). S'il est poussé sur un dépôt Git public ou partagé, n'importe qui ayant accès au dépôt pourrait récupérer ces identifiants et compromettre la sécurité de la base de données ou du système. C'est pour cette raison qu'on l'ajoute systématiquement au fichier .gitignore.
---

## Partie 5 — Ajouter sa propre application

### Trace 5.1 — état des trois services

Coller ici la sortie de `docker compose ps` (étape 5.3) :

```
NAME                    IMAGE             COMMAND                  SERVICE   CREATED          STATUS          PORTS
tp5-compose-adminer-1   adminer           "entrypoint.sh docke…"   adminer   41 minutes ago   Up 41 minutes   0.0.0.0:8081->8080/tcp, [::]:8081->8080/tcp
tp5-compose-api-1       tp5-compose-api   "python app.py"          api       24 seconds ago   Up 22 seconds   0.0.0.0:5000->5000/tcp, [::]:5000->5000/tcp
tp5-compose-db-1        postgres:15       "docker-entrypoint.s…"   db        41 minutes ago   Up 41 minutes   5432/tcp
```

### Trace 5.2 — réponse de l'API

Coller ici la sortie de `curl http://localhost:5000` (étape 5.3) :

```
StatusCode        : 200
StatusDescription : OK
Content           : Bonjour depuis Docker Compose!
RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 30
                    Content-Type: text/html; charset=utf-8
                    Date: Mon, 02 Nov 2026 17:44:00 GMT
                    Server: Werkzeug/3.1.9 Python/3.11.18

                    Bonjour depuis Docker Comp...
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 30], [Content-Type, text/html; charset=utf-8], [Date, Mon, 02 Nov 2026 17:44:00
                    GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 30
```

### Trace 5.3 — résolution du nom `db`

Coller ici la sortie de la commande de l'étape 5.4 :

```
172.18.0.3
```

### Trace 5.4 — effet de `--build`

Coller ici les sorties de `curl` **avant** puis **après** `--build` (étape 5.5) :

```

StatusCode        : 200
StatusDescription : OK
Content           : Bonjour depuis Docker Compose!
RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 30
                    Content-Type: text/html; charset=utf-8
                    Date: Mon, 02 Nov 2026 18:36:20 GMT
                    Server: Werkzeug/3.1.9 Python/3.11.18

                    Bonjour depuis Docker Comp...
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 30], [Content-Type, text/html; charset=utf-8], [Date, Mon, 02 Nov 2026 18:36:20
                    GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 30

StatusCode        : 200
StatusDescription : OK
Content           : Modification testée avec succès
RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 33
                    Content-Type: text/html; charset=utf-8
                    Date: Mon, 02 Nov 2026 18:37:23 GMT
                    Server: Werkzeug/3.1.9 Python/3.11.18

                    Modification testée avec s...
Forms             : {}
Headers           : {[Connection, close], [Content-Length, 33], [Content-Type, text/html; charset=utf-8], [Date, Mon, 02 Nov 2026 18:37:23
                    GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 33

```

### Q5.1 — Quelle est la différence entre `image: postgres:15` et `build: ./api` ?

**Réponse :**

image: postgres:15 télécharge et utilise une image pré-construite depuis un registre (Docker Hub). build: ./api demande à Docker de construire une nouvelle image localement à partir du code source et du Dockerfile situés dans le dossier ./api.
### Q5.2 — À quoi sert `depends_on: - db` ? Garantit-il que la base est prête, ou seulement que son conteneur a été démarré avant ?

**Réponse :**

Cela indique à Docker Compose de démarrer le conteneur db avant le conteneur api. Cela garantit uniquement que le conteneur db est démarré, mais pas que le service PostgreSQL à l'intérieur est entièrement initialisé et prêt à accepter des connexions.

### Q5.3 — Pourquoi `docker compose up -d` seul n'a-t-il pas pris en compte la modification de `app.py` ? Quelle option faut-il ajouter ?

**Réponse :**

Il n'a pas pris en compte la modification car il a utilisé l'image déjà construite (mise en cache). Il faut ajouter l'option --build (commande : docker compose up -d --build) pour forcer la reconstruction de l'image avec le nouveau code.

---

## Partie 6 — Nettoyage et vérification finale

### Trace 6.1 — après `docker compose down` (volume conservé)

Coller ici la sortie de `docker volume ls` (étape 6.1) :

```
DRIVER    VOLUME NAME
local     d785cadfc68f7a3cb9b1b72626c5117393753f1dff06ba539b61c2f3518a80a2
local     tp5-compose_data_db
```

### Trace 6.2 — vérification finale

Coller ici les sorties de `docker ps -a`, `docker volume ls` et `docker network ls` (étape 6.3), après `docker compose down -v` :

```
CONTAINER ID   IMAGE         COMMAND    CREATED        STATUS                    PORTS     NAMES
744d15f7a541   hello-world   "/hello"   29 hours ago   Exited (0) 29 hours ago             infallible_keldysh

DRIVER    VOLUME NAME
local     d785cadfc68f7a3cb9b1b72626c5117393753f1dff06ba539b61c2f3518a80a2

NETWORK ID     NAME      DRIVER    SCOPE
30b582fbbb13   bridge    bridge    local
c41e533e4875   host      host      local
837660030ba1   none      null      local

PS C:\Users\fghjklmù\tp5-compose> docker compose down -v
[+] down 1/1
 ✔️ Volume tp5-compose_data_db Removed

```

### Q6.1 — Quelle option de `docker compose down` supprime les volumes ? Pourquoi doit-on l'utiliser avec précaution pour une base de données réelle ?

**Réponse :**

L'option -v (ou --volumes) supprime les volumes nommés déclarés dans le fichier Compose. On doit l'utiliser avec une extrême précaution en production car elle efface définitivement toutes les données de la base de données (utilisateurs, commandes, etc.), ce qui est irréversible sans sauvegarde préalable.

---

## Fichiers finaux

### `docker-compose.yml` final

```yaml
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - data_db:/var/lib/postgresql/data
  adminer:
    image: adminer
    ports:
      - "8081:8080"
  api:
    build: ./api
    ports:
      - "5000:5000"
    depends_on:
      - db

volumes:
  data_db:
```

### `api/Dockerfile`

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

### Fichier `.env` (nom de la variable uniquement, **sans la valeur**)

```
POSTGRES_PASSWORD=********
```

---

## Conclusion (5 lignes maximum)

Comparer le lancement de l'application avec Docker Compose et avec les commandes `docker run` du TP n°4 : qu'est-ce qui est plus simple ? Qu'est-ce qui reste à votre avis difficile ?

Docker Compose simplifie considérablement la gestion de plusieurs conteneurs par rapport aux longues commandes docker run du TP4. Un seul fichier YAML décrit l'ensemble de l'architecture (services, réseaux, volumes, variables d'environnement), ce qui rend le projet reproductible et partageable. Les commandes up, down, logs et ps remplacent avantageusement les multiples docker run, docker stop, docker rm et docker network create. Enfin, Compose gère automatiquement le réseau interne entre services, ce qui facilite grandement la communication entre conteneurs.

---

## Auto-évaluation

Cocher les cases (remplacer `[ ]` par `[x]`) :

- [x] Mon `docker-compose.yml` démarre les trois services (`db`, `adminer`, `api`) avec une seule commande
- [x] J'ai vérifié que les données de la base survivent à `docker compose down`
- [x] Je sais expliquer pourquoi un service joint un autre par son nom
- [x] J'ai répondu à toutes les questions (Q1.1 à Q6.1) avec mes propres mots
- [x] J'ai collé toutes les traces demandées et ajouté la capture d'Adminer
- [x] Je n'ai pas inclus mon vrai fichier `.env`
