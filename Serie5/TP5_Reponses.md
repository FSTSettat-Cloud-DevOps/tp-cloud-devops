# TP n°5 — Docker Compose : premiers pas — Fiche de réponses

**Module :** Cloud Computing, Virtualisation & DevOps — FST Settat, Université Hassan 1er
**Enseignant :** Pr. Abdelfattah Abassi

| | |
|---|---|
| **Nom** | *(à compléter)* |
| **Prénom** | *(à compléter)* |
| **Groupe / Filière** | *(à compléter)* |
| **Date** | *(à compléter)* |

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
(coller ici la sortie)
```

Coller ici la sortie de `docker network ls` (étape 1.4) :

```
(coller ici la sortie)
```

### Q1.1 — En plus du conteneur, quel autre objet Docker a été créé par `docker compose up` ? Quel est son nom ?

**Réponse :**

*(écrire votre réponse ici)*

### Q1.2 — Quelle est la différence entre `docker compose stop` et `docker compose down` ?

**Réponse :**

*(écrire votre réponse ici)*

---

## Partie 2 — Deux services qui communiquent

### Trace 2.1 — état des services

Coller ici la sortie de `docker compose ps` (étape 2.2) :

```
(coller ici la sortie)
```

### Trace 2.2 — capture d'Adminer

Capture d'écran d'Adminer connecté à la base (étape 2.4) :

![Capture Adminer connecté à PostgreSQL](images/partie2_adminer.png)

### Q2.1 — Dans Adminer, pourquoi écrit-on `db` comme serveur et non `localhost` ?

**Réponse :**

*(écrire votre réponse ici)*

### Q2.2 — Lequel de ces deux services publie un port vers l'hôte ? Pourquoi le service `db` n'en a-t-il pas besoin ici ?

**Réponse :**

*(écrire votre réponse ici)*

---

## Partie 3 — Conserver les données avec un volume

### Trace 3.1 — données avant la suppression des conteneurs

Coller ici la sortie du dernier `SELECT * FROM etudiants;` de l'étape 3.3 :

```
(coller ici la sortie)
```

### Trace 3.2 — données après `docker compose down` puis `up`

Coller ici la sortie du `SELECT * FROM etudiants;` de l'étape 3.4 :

```
(coller ici la sortie)
```

### Trace 3.3 — volumes existants

Coller ici la sortie de `docker volume ls` (étape 3.5) :

```
(coller ici la sortie)
```

### Q3.1 — Pourquoi les données sont-elles toujours là après `docker compose down` puis `up` ?

**Réponse :**

*(écrire votre réponse ici)*

### Q3.2 — Que se serait-il passé sans la ligne `volumes` dans le service `db` ?

**Réponse :**

*(écrire votre réponse ici)*

---

## Partie 4 — Sortir le mot de passe avec un fichier `.env`

### Trace 4.1 — configuration interprétée

Coller ici la sortie de `docker compose config` (étape 4.3). **Masquer le mot de passe** si ce n'est pas la valeur d'exemple :

```
(coller ici la sortie)
```

### Q4.1 — Quel est l'intérêt d'un fichier `.env` plutôt que d'écrire le mot de passe dans `docker-compose.yml` ?

**Réponse :**

*(écrire votre réponse ici)*

### Q4.2 — Pourquoi ne faut-il pas envoyer le fichier `.env` sur un dépôt Git partagé ?

**Réponse :**

*(écrire votre réponse ici)*

---

## Partie 5 — Ajouter sa propre application

### Trace 5.1 — état des trois services

Coller ici la sortie de `docker compose ps` (étape 5.3) :

```
(coller ici la sortie)
```

### Trace 5.2 — réponse de l'API

Coller ici la sortie de `curl http://localhost:5000` (étape 5.3) :

```
(coller ici la sortie)
```

### Trace 5.3 — résolution du nom `db`

Coller ici la sortie de la commande de l'étape 5.4 :

```
(coller ici la sortie)
```

### Trace 5.4 — effet de `--build`

Coller ici les sorties de `curl` **avant** puis **après** `--build` (étape 5.5) :

```
(coller ici les deux sorties)
```

### Q5.1 — Quelle est la différence entre `image: postgres:15` et `build: ./api` ?

**Réponse :**

*(écrire votre réponse ici)*

### Q5.2 — À quoi sert `depends_on: - db` ? Garantit-il que la base est prête, ou seulement que son conteneur a été démarré avant ?

**Réponse :**

*(écrire votre réponse ici)*

### Q5.3 — Pourquoi `docker compose up -d` seul n'a-t-il pas pris en compte la modification de `app.py` ? Quelle option faut-il ajouter ?

**Réponse :**

*(écrire votre réponse ici)*

---

## Partie 6 — Nettoyage et vérification finale

### Trace 6.1 — après `docker compose down` (volume conservé)

Coller ici la sortie de `docker volume ls` (étape 6.1) :

```
(coller ici la sortie)
```

### Trace 6.2 — vérification finale

Coller ici les sorties de `docker ps -a`, `docker volume ls` et `docker network ls` (étape 6.3), après `docker compose down -v` :

```
(coller ici les sorties)
```

### Q6.1 — Quelle option de `docker compose down` supprime les volumes ? Pourquoi doit-on l'utiliser avec précaution pour une base de données réelle ?

**Réponse :**

*(écrire votre réponse ici)*

---

## Fichiers finaux

### `docker-compose.yml` final

```yaml
(coller ici le contenu de votre docker-compose.yml)
```

### `api/Dockerfile`

```dockerfile
(coller ici le contenu de votre Dockerfile)
```

### Fichier `.env` (nom de la variable uniquement, **sans la valeur**)

```
POSTGRES_PASSWORD=********
```

---

## Conclusion (5 lignes maximum)

Comparer le lancement de l'application avec Docker Compose et avec les commandes `docker run` du TP n°4 : qu'est-ce qui est plus simple ? Qu'est-ce qui reste à votre avis difficile ?

*(écrire votre conclusion ici)*

---

## Auto-évaluation

Cocher les cases (remplacer `[ ]` par `[x]`) :

- [ ] Mon `docker-compose.yml` démarre les trois services (`db`, `adminer`, `api`) avec une seule commande
- [ ] J'ai vérifié que les données de la base survivent à `docker compose down`
- [ ] Je sais expliquer pourquoi un service joint un autre par son nom
- [ ] J'ai répondu à toutes les questions (Q1.1 à Q6.1) avec mes propres mots
- [ ] J'ai collé toutes les traces demandées et ajouté la capture d'Adminer
- [ ] Je n'ai pas inclus mon vrai fichier `.env`
