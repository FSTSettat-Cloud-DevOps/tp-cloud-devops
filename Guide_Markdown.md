# Guide Markdown pour les rapports de TP

> **Public cible :** étudiants en informatique, Cloud, Virtualisation, DevOps et développement logiciel  
> **Objectif :** apprendre à rédiger un rapport technique propre dans un fichier `.md` et à l'afficher correctement sur GitHub.

---

## 1. Qu'est-ce que Markdown ?

**Markdown** est un langage de balisage léger qui permet de mettre en forme un document avec des caractères simples.

Un fichier Markdown porte généralement l'extension :

```text
.md
```

Exemple :

```text
README.md
rapport.md
Guide_Markdown.md
```

L'intérêt de Markdown pour les TP informatiques est qu'il permet de mélanger facilement :

- du texte ;
- des commandes ;
- du code source ;
- des captures d'écran ;
- des tableaux ;
- des liens ;
- des listes ;
- des résultats et des explications.

Les fichiers Markdown sont particulièrement adaptés à **GitHub**.

---

# 2. Créer un fichier Markdown

On peut créer un fichier avec un éditeur comme :

- Visual Studio Code ;
- Notepad++ ;
- GitHub directement dans le navigateur ;
- Typora ;
- Obsidian ;
- ou un simple éditeur de texte.

Exemple :

```text
rapport.md
```

Pour un TP, on peut organiser les fichiers ainsi :

```text
Serie1/
├── README.md
├── rapport.md
├── images/
│   ├── vm.png
│   ├── reseau.png
│   └── resultat.png
└── scripts/
    ├── script1.py
    └── script2.sh
```

---

# 3. Les titres

Markdown utilise le symbole `#` pour créer les titres.

## Syntaxe

```markdown
# Titre niveau 1

## Titre niveau 2

### Titre niveau 3

#### Titre niveau 4

##### Titre niveau 5

###### Titre niveau 6
```

## Exemple

```markdown
# Série 1 - Virtualisation

## 1. Installation de VirtualBox

### 1.1 Création de la machine virtuelle

### 1.2 Configuration réseau
```

Le nombre de `#` détermine le niveau du titre.

> **Conseil :** utilisez un seul `#` pour le titre principal du document, puis `##`, `###`, etc. pour les différentes parties.

---

# 4. Paragraphes et retours à la ligne

Un paragraphe normal s'écrit simplement :

```markdown
Ceci est un premier paragraphe.

Ceci est un deuxième paragraphe.
```

Une ligne vide permet de créer un nouveau paragraphe.

Pour forcer un retour à la ligne, on peut terminer une ligne avec deux espaces.

```markdown
Première ligne.  
Deuxième ligne.
```

---

# 5. Texte en gras

Pour écrire en **gras**, utilisez deux étoiles `**`.

```markdown
**texte en gras**
```

Résultat :

**texte en gras**

Exemple :

```markdown
La commande **ip addr** permet d'afficher les interfaces réseau.
```

---

# 6. Texte en italique

Pour écrire en *italique*, utilisez une étoile de chaque côté.

```markdown
*texte en italique*
```

Résultat :

*texte en italique*

---

# 7. Gras et italique

Pour obtenir du ***gras italique*** :

```markdown
***texte en gras et italique***
```

---

# 8. Texte barré

Pour barrer un texte :

```markdown
~~texte barré~~
```

Résultat :

~~texte barré~~

Exemple :

```markdown
~~Cette commande est incorrecte.~~
```

---

# 9. Code dans une phrase

Lorsqu'une commande apparaît dans une phrase, utilisez des accents graves :

```markdown
La commande `ip addr` permet d'afficher les interfaces réseau.
```

Résultat :

La commande `ip addr` permet d'afficher les interfaces réseau.

Autres exemples :

```markdown
Utilisez `python --version` pour connaître la version de Python.

Le fichier `README.md` contient les informations principales du projet.

La commande `git status` permet de consulter l'état du dépôt.
```

---

# 10. Blocs de code

Pour afficher plusieurs lignes de code, utilisez trois accents graves.

## Exemple simple

````markdown
```text
Bonjour
Bienvenue dans le TP
```
````

## Code Python

````markdown
```python
nom = "Ahmed"
print("Bonjour", nom)
```
````

## Commandes Linux

````markdown
```bash
sudo apt update
sudo apt install python3
python3 --version
```
````

## PowerShell

````markdown
```powershell
Get-Process
Get-Service
```
````

## Windows CMD

````markdown
```cmd
ipconfig
ping 8.8.8.8
```
````

## Dart

````markdown
```dart
void main() {
  print("Bonjour Flutter");
}
```
````

> **Important :** indiquez le langage après les trois accents graves lorsque cela est possible. GitHub pourra alors appliquer une coloration syntaxique au code.

---

# 11. Listes à puces

Utilisez `-`, `*` ou `+`.

Exemple :

```markdown
- Python
- Dart
- Flutter
- Git
- GitHub
```

Résultat :

- Python
- Dart
- Flutter
- Git
- GitHub

---

# 12. Listes numérotées

Utilisez des nombres suivis d'un point.

```markdown
1. Installer VirtualBox
2. Télécharger Ubuntu
3. Créer la machine virtuelle
4. Configurer le réseau
5. Démarrer la machine
```

Résultat :

1. Installer VirtualBox
2. Télécharger Ubuntu
3. Créer la machine virtuelle
4. Configurer le réseau
5. Démarrer la machine

---

# 13. Listes imbriquées

On peut créer des sous-listes avec des espaces.

```markdown
- Virtualisation
  - VirtualBox
  - VMware
  - Hyper-V
- Cloud
  - AWS
  - Azure
  - Google Cloud
```

Résultat :

- Virtualisation
  - VirtualBox
  - VMware
  - Hyper-V
- Cloud
  - AWS
  - Azure
  - Google Cloud

---

# 14. Cases à cocher

Les cases à cocher sont très pratiques pour les TP.

## Syntaxe

```markdown
- [ ] Tâche non terminée
- [x] Tâche terminée
```

Exemple :

```markdown
## Vérification

- [x] VirtualBox installé
- [x] Ubuntu installé
- [x] Réseau configuré
- [ ] Test SSH
- [ ] Capture d'écran réalisée
```

Résultat :

- [x] VirtualBox installé
- [x] Ubuntu installé
- [x] Réseau configuré
- [ ] Test SSH
- [ ] Capture d'écran réalisée

---

# 15. Liens hypertextes

## Syntaxe

```markdown
[Texte du lien](URL)
```

Exemple :

```markdown
[GitHub](https://github.com)
```

Autre exemple :

```markdown
[Documentation Python](https://docs.python.org/)
```

On peut également écrire :

```markdown
Consultez la [documentation officielle de Python](https://docs.python.org/).
```

---

# 16. Images

## Syntaxe

```markdown
![Description de l'image](chemin/image.png)
```

Exemple :

```markdown
![Machine virtuelle Ubuntu](images/vm.png)
```

Il est recommandé d'organiser les captures dans un dossier :

```text
images/
├── vm.png
├── reseau.png
├── ssh.png
└── resultat.png
```

Puis dans le fichier Markdown :

```markdown
![Création de la VM](images/vm.png)
```

> **Conseil :** donnez des noms explicites aux images, par exemple `configuration_reseau.png` plutôt que `image1.png`.

---

# 17. Images avec un texte alternatif

Le texte entre crochets est appelé **texte alternatif**.

```markdown
![Configuration réseau de la machine virtuelle](images/reseau.png)
```

Si l'image ne peut pas être affichée, ce texte peut être utilisé pour décrire son contenu.

---

# 18. Citations

Pour créer une citation, utilisez `>`.

```markdown
> Cette commande permet d'afficher la configuration réseau.
```

Résultat :

> Cette commande permet d'afficher la configuration réseau.

On peut également avoir plusieurs lignes :

```markdown
> Première information.
> Deuxième information.
```

---

# 19. Ligne horizontale

Pour séparer deux parties du document :

```markdown
---
```

Exemple :

```markdown
## Partie 1

Contenu de la partie 1.

---

## Partie 2

Contenu de la partie 2.
```

---

# 20. Tableaux

Les tableaux sont très utiles pour présenter les caractéristiques d'une machine virtuelle.

## Syntaxe

```markdown
| Élément | Valeur |
|---|---|
| Système | Ubuntu 24.04 |
| RAM | 4 Go |
| CPU | 2 |
| Disque | 30 Go |
```

Résultat :

| Élément | Valeur |
|---|---|
| Système | Ubuntu 24.04 |
| RAM | 4 Go |
| CPU | 2 |
| Disque | 30 Go |

---

# 21. Tableau avec plusieurs colonnes

```markdown
| Étudiant | OS | RAM | Résultat |
|---|---|---:|---|
| Étudiant 1 | Ubuntu | 4 Go | OK |
| Étudiant 2 | Ubuntu | 8 Go | OK |
| Étudiant 3 | Windows | 8 Go | OK |
```

La notation `---:` permet d'aligner une colonne à droite.

On peut également utiliser :

```markdown
|---|
```

pour un alignement à gauche, et :

```markdown
|:---:|
```

pour centrer.

Exemple :

```markdown
| Nom | Note | Résultat |
|:---|:---:|---:|
| Ahmed | 16 | Validé |
| Sara | 14 | Validé |
```

---

# 22. Commentaires invisibles

On peut écrire un commentaire qui ne sera pas affiché dans le rendu :

```markdown
<!-- Ceci est un commentaire -->
```

Le commentaire reste présent dans le fichier source mais n'apparaît pas sur GitHub.

---

# 23. Afficher les caractères Markdown

Certains caractères ont une signification particulière.

Par exemple :

```markdown
# titre
```

crée un titre.

Si vous voulez afficher réellement le caractère `#`, vous pouvez utiliser `\` :

```markdown
\# Ceci n'est pas un titre
```

De même :

```markdown
\*texte\*
```

permet d'afficher :

\*texte\*

---

# 24. Code avec des accents graves

Si votre code contient lui-même des accents graves, utilisez quatre accents graves autour du bloc.

Exemple :

`````markdown
````text
Voici du texte contenant ``` du code.
````
`````

Cette technique est rarement nécessaire dans un rapport classique, mais elle peut être utile pour expliquer Markdown.

---

# 25. Émojis

GitHub permet également d'utiliser des émojis.

Exemples :

```markdown
✅ Installation terminée

❌ Erreur

⚠️ Attention

💡 Remarque
```

Cela peut rendre un rapport plus lisible, mais il ne faut pas en abuser dans un rapport académique.

---

# 26. Formules mathématiques

Selon la plateforme utilisée, les formules peuvent être prises en charge avec une syntaxe de type LaTeX.

Exemple :

```markdown
$E = mc^2$
```

Pour une formule affichée sur une ligne séparée :

```markdown
$$
E = mc^2
$$
```

> **Attention :** le support exact des formules peut dépendre de l'outil utilisé pour afficher le fichier Markdown.

---

# 27. Structure recommandée d'un rapport de TP

Pour vos TP, vous pouvez utiliser la structure suivante :

```markdown
# Série 1 - Virtualisation

## 1. Objectif

Présenter l'objectif du TP.

## 2. Environnement de travail

| Élément | Valeur |
|---|---|
| Système hôte | Windows 11 |
| Hyperviseur | VirtualBox |
| Système invité | Ubuntu 24.04 |
| RAM | 4 Go |
| CPU | 2 |
| Disque | 30 Go |

## 3. Installation

### 3.1 Installation de VirtualBox

Décrire les étapes réalisées.

### 3.2 Création de la machine virtuelle

Décrire la configuration choisie.

![Configuration de la VM](images/vm.png)

## 4. Configuration réseau

### 4.1 Commande utilisée

```bash
ip addr
```

### 4.2 Résultat

![Configuration réseau](images/reseau.png)

### 4.3 Explication

Expliquer le résultat obtenu.

## 5. Test

```bash
ping 8.8.8.8
```

Résultat :

![Test réseau](images/ping.png)

## 6. Difficultés rencontrées

- Problème 1 : ...
- Solution : ...

## 7. Conclusion

Présenter les principaux résultats du TP.
```

---

# 28. Exemple complet de rapport

Voici un exemple simple que vous pouvez utiliser comme modèle.

```markdown
# TP 1 - Découverte de la virtualisation

## 1. Objectif

L'objectif de ce TP est de créer une machine virtuelle Ubuntu avec VirtualBox et de tester sa configuration réseau.

## 2. Environnement

| Élément | Valeur |
|---|---|
| Système hôte | Windows 11 |
| Hyperviseur | VirtualBox |
| Système invité | Ubuntu 24.04 |
| RAM | 4 Go |
| CPU | 2 |
| Disque | 30 Go |

## 3. Création de la machine virtuelle

La machine virtuelle a été créée avec VirtualBox.

![Création de la VM](images/vm.png)

## 4. Configuration réseau

La commande suivante a été exécutée :

```bash
ip addr
```

Cette commande permet d'afficher les interfaces réseau de la machine.

Résultat :

![Résultat de ip addr](images/ip-addr.png)

## 5. Test de connexion

La commande suivante permet de tester la connexion :

```bash
ping 8.8.8.8
```

Résultat :

```text
64 bytes from 8.8.8.8: icmp_seq=1 ttl=117 time=25 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=117 time=24 ms
```

La machine peut communiquer avec Internet.

## 6. Difficultés rencontrées

> Une erreur est apparue lors de la configuration réseau.

La solution consistait à vérifier le mode réseau de VirtualBox.

## 7. Vérification

- [x] Machine virtuelle créée
- [x] Ubuntu installé
- [x] Réseau configuré
- [x] Test `ping` effectué
- [x] Captures ajoutées

## 8. Conclusion

Ce TP nous a permis de découvrir la création d'une machine virtuelle et la configuration de base de son réseau.
```

---

# 29. Organisation recommandée pour un TP GitHub

Pour un travail rendu sur GitHub, nous recommandons :

```text
Serie1/
│
├── README.md
│
├── images/
│   ├── vm.png
│   ├── reseau.png
│   └── ping.png
│
└── scripts/
    ├── script1.sh
    └── script2.py
```

Le fichier `README.md` doit contenir le rapport principal.

---

# 30. Bonnes pratiques pour les étudiants

## 30.1 Utiliser des titres

Évitez un document contenant uniquement de longs paragraphes.

Préférez :

```markdown
# TP 1

## 1. Objectif

## 2. Installation

## 3. Configuration

## 4. Tests

## 5. Résultats

## 6. Difficultés

## 7. Conclusion
```

---

## 30.2 Expliquer les commandes

Ne faites pas uniquement :

```bash
ip addr
```

Il faut expliquer :

> La commande `ip addr` permet d'afficher les interfaces réseau et leurs adresses IP.

---

## 30.3 Ajouter les preuves

Une manipulation doit être accompagnée, lorsque cela est pertinent, d'une preuve :

- capture d'écran ;
- résultat d'une commande ;
- fichier généré ;
- sortie du programme.

Exemple :

```markdown
### Résultat

![Résultat de la commande](images/resultat.png)
```

---

## 30.4 Ne pas utiliser des captures inutiles

Une capture doit apporter une information.

Évitez :

```text
capture1.png
capture2.png
capture3.png
capture4.png
capture5.png
```

Préférez :

```text
creation_vm.png
configuration_reseau.png
test_ping.png
installation_python.png
resultat_script.png
```

---

# 31. Markdown et GitHub

GitHub affiche automatiquement les fichiers Markdown.

Par exemple :

```text
README.md
```

sera affiché directement comme une page lorsqu'on ouvre le dépôt.

Cela permet à l'enseignant de consulter rapidement :

1. le rapport ;
2. les commandes ;
3. les résultats ;
4. les captures ;
5. le code source.

---

# 32. Commandes Markdown essentielles à retenir

| Élément | Syntaxe |
|---|---|
| Titre 1 | `# Titre` |
| Titre 2 | `## Titre` |
| Gras | `**texte**` |
| Italique | `*texte*` |
| Gras + italique | `***texte***` |
| Barré | `~~texte~~` |
| Code inline | `` `code` `` |
| Bloc de code | ` ``` ` |
| Liste | `- élément` |
| Liste numérotée | `1. élément` |
| Case cochée | `- [x]` |
| Case vide | `- [ ]` |
| Lien | `[texte](URL)` |
| Image | `![texte](image.png)` |
| Citation | `> texte` |
| Ligne horizontale | `---` |
| Tableau | `\| colonne \| colonne \|` |
| Commentaire | `<!-- commentaire -->` |

---

# 33. Exercice d'entraînement

Créez un fichier :

```text
exercice_markdown.md
```

et réalisez les tâches suivantes.

### Tâche 1

Créer un titre :

```text
Mon premier rapport Markdown
```

### Tâche 2

Créer une section :

```text
1. Mon environnement
```

### Tâche 3

Créer un tableau contenant :

- Système d'exploitation ;
- RAM ;
- CPU ;
- Disque.

### Tâche 4

Ajouter une commande Linux :

```bash
uname -a
```

### Tâche 5

Expliquer cette commande dans un paragraphe.

### Tâche 6

Ajouter une capture d'écran dans le dossier :

```text
images/
```

### Tâche 7

Créer une liste de vérification :

```markdown
- [x] Installation
- [x] Configuration
- [ ] Test
- [ ] Conclusion
```

### Tâche 8

Ajouter une conclusion.

---

# 34. Exercice final : créer un rapport de TP

Créez l'arborescence suivante :

```text
TP-Markdown/
├── README.md
└── images/
    └── resultat.png
```

Votre `README.md` doit contenir obligatoirement :

- un titre principal ;
- au moins trois sections ;
- un paragraphe ;
- une liste ;
- une liste numérotée ;
- un tableau ;
- une commande dans un bloc de code ;
- une image ;
- un lien ;
- une citation ;
- une case à cocher ;
- une conclusion.

---

# 35. Checklist finale

Avant de rendre votre TP, vérifiez :

- [ ] Le fichier principal s'appelle `README.md` ou `rapport.md`.
- [ ] Les titres sont correctement organisés.
- [ ] Les commandes sont dans des blocs de code.
- [ ] Chaque commande importante est expliquée.
- [ ] Les résultats sont présentés.
- [ ] Les captures d'écran sont lisibles.
- [ ] Les images sont dans un dossier `images/`.
- [ ] Les liens fonctionnent.
- [ ] Les tableaux sont correctement formatés.
- [ ] Le rapport possède une conclusion.
- [ ] Le dépôt GitHub est correctement organisé.

---

# 36. Résumé

Markdown est particulièrement adapté aux travaux pratiques informatiques car il permet de présenter dans un même document :

```text
Texte
  +
Commandes
  +
Code
  +
Captures d'écran
  +
Tableaux
  +
Résultats
  +
Explications
```

Pour vos travaux GitHub, les éléments les plus importants à maîtriser sont :

```markdown
# Titres

**Gras**

*Italique*

`commande`

```bash
commande
```

- Liste

1. Liste numérotée

- [ ] Case à cocher

[Lien](https://exemple.com)

![Image](images/image.png)

> Citation

| Tableau | Valeur |
|---|---|
| Exemple | Test |
```

**Objectif final :** produire un rapport technique clair, structuré, reproductible et facile à consulter sur GitHub.
