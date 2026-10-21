# Consignes de réalisation et de dépôt des TP/TD sur GitHub

## 1. Objectif

Pour **chaque TP**, chaque étudiant doit créer un dossier portant son nom dans le dépôt GitHub indiqué par l'enseignant. À l'intérieur de ce dossier, il faut créer un sous-dossier nommé `reponses` qui contiendra toutes les réponses aux questions du TP.

Respectez exactement la structure demandée afin que l'enseignant puisse retrouver facilement votre travail.

## 2. Structure obligatoire

Exemple pour un étudiant appelé `Abdellah_Nom` :

```text
TP/
├── README.md
├── Abdellah_Nom/
│   └── reponses/
│       ├── reponses.md
│       ├── exercice1.dart
│       └── exercice2.dart
└── ...
```

- `Abdellah_Nom/` : remplacez ce nom par votre propre nom et prénom, sans accents ni espaces si possible. Exemple : `Salma_ElAmrani`.
- `reponses/` : dossier qui contient les réponses du TP.
- `reponses.md` : fichier texte Markdown dans lequel vous répondez aux questions théoriques et expliquez vos résultats.
- Les fichiers de code (`.dart`, `.py`, `.html`, etc.) sont à ajouter si les exercices le demandent.

**Important :** réalisez cette structure pour chaque TP, dans le dépôt ou l'emplacement indiqué par l'enseignant.

## 3. Méthode A — Créer les dossiers directement sur le site GitHub

### Étape 1 — Ouvrir le dépôt

1. Connectez-vous à votre compte sur [GitHub](https://github.com).
2. Ouvrez le dépôt du TP communiqué par l'enseignant.
3. Vérifiez que vous êtes dans le bon dépôt et, si nécessaire, dans le dossier correspondant au TP.

### Étape 2 — Créer votre dossier personnel

1. Cliquez sur **Add file** (Ajouter un fichier).
2. Choisissez **Create new file** (Créer un nouveau fichier).
3. Dans le champ du nom du fichier, saisissez votre nom suivi d'une barre oblique et d'un nom de fichier, par exemple :

   `Abdellah_Nom/README.md`

   Remplacez `Abdellah_Nom` par votre nom et prénom.

4. Dans la zone de contenu, écrivez par exemple :

   `Dossier personnel de [Votre nom et prénom] pour le TP.`

5. Descendez jusqu'à **Commit changes**.
6. Ajoutez un message, par exemple `Création de mon dossier personnel`.
7. Validez avec **Commit changes**.

GitHub crée le dossier grâce au fichier placé à l'intérieur. Un dossier vide ne peut pas être enregistré seul sur GitHub.

### Étape 3 — Créer le sous-dossier `reponses`

1. Ouvrez votre dossier personnel.
2. Cliquez sur **Add file**, puis **Create new file**.
3. Dans le champ du nom du fichier, saisissez :

   `reponses/reponses.md`

4. Dans le contenu, préparez votre fichier de réponses, par exemple :

   ```markdown
   # Réponses au TP

   **Nom et prénom :** Votre nom et prénom  
   **Groupe :** Votre groupe  
   **TP :** Numéro ou titre du TP

   ## Exercice 1

   Réponse :

   ## Exercice 2

   Réponse :
   ```

5. Cliquez sur **Commit changes** pour enregistrer le fichier.

Le sous-dossier `reponses` sera créé automatiquement.

### Étape 4 — Ajouter les fichiers de code ou autres réponses

Si le TP demande du code :

1. Ouvrez le dossier `reponses`.
2. Cliquez sur **Add file** puis **Create new file** pour créer un fichier texte/code, ou utilisez **Upload files** pour téléverser un fichier existant depuis votre ordinateur.
3. Donnez au fichier un nom explicite, par exemple `exercice1.dart`, `exercice2.py` ou `resultats.txt`.
4. Enregistrez les changements avec **Commit changes**.

Rangez les fichiers de réponse dans `reponses/`, et non à côté de votre dossier personnel.

## 4. Méthode B — Préparer les dossiers sur votre ordinateur puis les envoyer

Cette méthode est pratique si vous avez plusieurs fichiers à remettre.

1. Sur votre ordinateur, créez un dossier portant votre nom, par exemple `Abdellah_Nom`.
2. À l'intérieur, créez le dossier `reponses`.
3. Dans `reponses`, créez `reponses.md` et ajoutez vos fichiers de code et résultats.
4. Ouvrez le dépôt GitHub du TP.
5. Naviguez jusqu'à l'emplacement où les dossiers des étudiants doivent être déposés.
6. Cliquez sur **Add file** puis **Upload files**.
7. Sélectionnez les fichiers à envoyer. Selon l'interface GitHub, le téléversement d'un dossier complet peut ne pas être proposé : dans ce cas, ouvrez le dossier local et téléversez son contenu en conservant la structure demandée, ou utilisez GitHub Desktop.
8. Vérifiez que les fichiers apparaissent au bon emplacement, puis cliquez sur **Commit changes**.

**Attention :** vérifiez toujours l'arborescence après le téléversement. Le résultat doit être `VotreNom/reponses/...`, et non des fichiers directement à la racine du dépôt.

## 5. Exemple de fichier `reponses.md`

Copiez ce modèle et complétez-le :

```markdown
# Réponses au TP

- **Nom et prénom :** 
- **Groupe :** 
- **Module :** 
- **TP :** 

## Exercice 1

### Réponse

Écrivez votre réponse ici.

### Explication

Expliquez brièvement votre démarche si cela est demandé.

## Exercice 2

### Réponse

Écrivez votre réponse ici.

### Code ou résultat

Ajoutez ici le résultat attendu ou indiquez le fichier associé, par exemple `exercice2.dart`.
```

## 6. Vérification avant de terminer

Avant de considérer votre travail comme remis, vérifiez les points suivants :

- [ ] Mon dossier porte mon nom et mon prénom.
- [ ] Mon dossier contient un sous-dossier nommé exactement `reponses`.
- [ ] Toutes mes réponses sont dans `reponses/`.
- [ ] Mon fichier `reponses.md` est complété.
- [ ] Les fichiers de code portent des noms clairs et ont les bonnes extensions.
- [ ] J'ai enregistré mes changements avec **Commit changes**.
- [ ] J'ai vérifié sur GitHub que les fichiers sont visibles au bon emplacement.

## 7. Règles à respecter

1. Ne modifiez pas et ne supprimez pas les fichiers d'un autre étudiant.
2. Ne déposez pas vos réponses à la racine du dépôt.
3. Utilisez un seul dossier personnel par étudiant et par TP.
4. Pour un nouveau TP, suivez les consignes de l'enseignant : créez votre dossier dans l'emplacement prévu pour ce TP.
5. Si vous ne pouvez pas créer ou modifier des fichiers, il peut s'agir d'un problème de droits d'accès. Contactez l'enseignant au lieu de modifier les paramètres du dépôt.
6. N'attendez pas la dernière minute pour vérifier votre dépôt.

**Livrable attendu :** un dossier à votre nom contenant un dossier `reponses` avec votre fichier `reponses.md` et, si nécessaire, les fichiers de code et de résultats.
