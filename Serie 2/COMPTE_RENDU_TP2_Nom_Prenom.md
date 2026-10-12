
# Compte rendu — TP 1–2 : Premier contact avec une infrastructure Cloud locale

**Module :** Concepts fondamentaux du Cloud Computing  
**Établissement :** FST de Settat — Université Hassan 1er  
**Enseignant :** Pr. A. ABASSI

> **Consignes**
> - Complétez toutes les sections avec vos propres observations.
> - Remplacez les textes entre crochets (`[À compléter]`) par vos réponses.
> - Insérez les captures d'écran demandées dans les emplacements prévus.
> - Ne mettez pas de captures inventées : les résultats doivent provenir de votre propre machine.
> - Enregistrez ce fichier sous `COMPTE_RENDU_TP1-2_Nom_Prenom.md`.
> - Dans GitHub, ajoutez ce fichier et les captures dans le dépôt ou dossier prévu par l'enseignant.

## 1. Informations sur l'étudiant

- **Nom et prénom :** [À compléter]
- **Filière / groupe :** [À compléter]
- **Date de réalisation :** [À compléter]
- **Système hôte :** [Windows / macOS / Linux]
- **Version de VirtualBox :** [À compléter]
- **Version de Vagrant :** [À compléter]

## 2. Préparation de l'environnement

### 2.1 Vérification de Vagrant

Commande exécutée :

```powershell
vagrant --version
```

**Version affichée :** [À compléter]

### 2.2 Ajout de la box locale

Nom du fichier fourni par l'enseignant : `ubuntu-trusty64.box`

Commandes exécutées :

```powershell
vagrant box add ubuntu/trusty64 ubuntu-trusty64.box
vagrant box list
```

**Résultat observé :** [Décrire brièvement le résultat.]

**Capture d'écran — liste des boxes :**

![Capture : vagrant box list](captures/01-vagrant-box-list.png)

> Déposez votre capture dans le dossier `captures/` avec le nom `01-vagrant-box-list.png`. Adaptez le chemin de l'image si nécessaire.

### 2.3 Question de réflexion — modèle IaaS

**Question :** Pourquoi peut-on considérer une machine virtuelle VirtualBox comme une illustration simplifiée du modèle IaaS ?

**Réponse :**  
[Expliquez en quelques phrases le rôle de la machine virtuelle, les ressources qu'elle utilise et ce que l'utilisateur peut administrer.]

## 3. Étape 1 — Découverte de la VM et du modèle IaaS

### 3.1 Création et configuration

Dossier de travail utilisé : `[À compléter]`

Le fichier `Vagrantfile` a été configuré avec les paramètres suivants :

| Paramètre | Valeur configurée |
|---|---|
| Box | `ubuntu/trusty64` |
| Nom d'hôte | `vm-tp1-cloud` |
| Adresse IP privée | `192.168.56.110` |
| Mémoire | `1024 MB` |
| Nombre de CPU | `1` |
| Provider | `virtualbox` |

**Avez-vous rencontré un problème lors de la création ou du démarrage de la VM ?**  
[Non / Oui, décrire le problème et sa solution.]

### 3.2 État de la machine virtuelle

Commande exécutée :

```bash
vagrant status
```

**État observé :** [À compléter]

**Capture d'écran — état de la VM :**

![Capture : vagrant status](captures/02-vagrant-status.png)

### 3.3 Identification de l'utilisateur et de la machine

Depuis la VM, commandes exécutées :

```bash
whoami
hostname
hostname -I
```

| Élément | Résultat observé |
|---|---|
| Utilisateur courant (`whoami`) | [À compléter] |
| Nom de la machine (`hostname`) | [À compléter] |
| Adresse(s) IP (`hostname -I`) | [À compléter] |

**Capture d'écran — identité de la VM :**

![Capture : utilisateur, nom et IP](captures/03-identite-vm.png)

### 3.4 Ressources virtuelles

Commandes exécutées :

```bash
uname -a
lscpu
free -h
df -h
```

Complétez le tableau à partir des résultats réellement affichés.

| Ressource | Valeur observée | Valeur configurée ou remarque |
|---|---|---|
| Système / noyau (`uname -a`) | [À compléter] | Ubuntu Trusty 14.04 fourni dans la box |
| CPU (`lscpu`) | [À compléter] | 1 CPU configuré |
| Mémoire (`free -h`) | [À compléter] | 1024 MB configurés ; la mémoire visible peut différer légèrement |
| Disque (`df -h`) | [À compléter] | [Indiquer la taille/partition observée] |
| Réseau | [À compléter] | IP privée prévue : `192.168.56.110` |

**Capture d'écran — ressources de la VM :**

![Capture : ressources de la VM](captures/04-ressources-vm.png)

### 3.5 Interprétation

1. Pourquoi les ressources affichées dans Ubuntu sont-elles des ressources **virtuelles** ?

   **Réponse :** [À compléter]

2. Quel est l'intérêt de limiter la VM à 1 CPU et 1024 MB de mémoire dans ce TP ?

   **Réponse :** [À compléter]

## 4. Étape 2 — Réseau virtuel et accès SSH

### 4.1 Adresse IP de la VM

Commandes exécutées dans Ubuntu :

```bash
hostname -I
ip addr show
```

- **Utilisateur SSH prévu :** [À compléter]
- **Adresse IP de la VM observée :** [À compléter]
- **Interface réseau concernée :** [À compléter]

### 4.2 Vérification du serveur SSH

Commandes exécutées :

```bash
sudo service ssh status
sudo netstat -tlnp | grep :22
```

- **État du service SSH :** [À compléter]
- **Le port 22 est-il en écoute ?** [Oui / Non]
- **Si le service n'était pas actif, quelle commande avez-vous utilisée ?** [À compléter]

**Capture d'écran — état du serveur SSH :**

![Capture : service SSH](captures/05-ssh-status.png)

### 4.3 Test SSH depuis le système hôte

Depuis PowerShell (Windows) ou le terminal de l'hôte, commande testée :

```powershell
ssh vagrant@192.168.56.110
```

- **Résultat obtenu :** [Connexion réussie / Échec]
- **Message affiché ou difficulté rencontrée :** [À compléter]
- **Solution appliquée, le cas échéant :** [À compléter]

**Capture d'écran — test de connectivité :**

![Capture : ping et test du port 22](captures/06-tests-reseau-ssh.png)

Sur Windows, les commandes utiles sont :

```powershell
ping 192.168.56.110
Test-NetConnection 192.168.56.110 -Port 22
```

- **Résultat de `ping` :** [À compléter]
- **Valeur de `TcpTestSucceeded` :** [True / False / Non applicable]

> Si `ssh vagrant@192.168.56.110` ne fonctionne pas directement, ne prétendez pas que le test a réussi. Notez le résultat obtenu et expliquez la différence avec `vagrant ssh`, qui utilise la configuration SSH et la clé gérées par Vagrant.

### 4.4 Compréhension de SSH

**Question :** Quelle est la différence entre les commandes suivantes ?

```bash
ssh vagrant@192.168.56.110
vagrant ssh
```

**Réponse :**  
[Comparez la cible indiquée, la configuration utilisée et la gestion de la clé SSH.]

## 5. Étape 3 — Sécurité, pare-feu UFW et utilisateurs

### 5.1 État initial du pare-feu

Commande :

```bash
sudo ufw status
```

- **Résultat observé :** [À compléter]
- **UFW était-il installé et actif ?** [À compléter]

### 5.2 Autorisation du port SSH et activation d'UFW

Commandes exécutées :

```bash
sudo ufw allow 22/tcp
sudo ufw status numbered
sudo ufw enable
sudo ufw status verbose
```

**Résultat observé :** [Décrire les règles affichées et l'état du pare-feu.]

### 5.3 Blocage du port 8080

Commande exécutée :

```bash
sudo ufw deny 8080/tcp
sudo ufw status numbered
```

**Règle observée pour le port 8080 :** [À compléter]

**Capture d'écran — règles UFW :**

![Capture : règles UFW](captures/07-ufw-regles.png)

**Question :** Pourquoi est-il nécessaire de conserver une règle autorisant le port 22 lorsque l'administration de la VM est réalisée par SSH ?

**Réponse :**  
[Expliquez le rôle du port 22 et le risque de bloquer l'accès d'administration.]

### 5.4 Création d'un groupe et d'un utilisateur

Commandes exécutées :

```bash
sudo groupadd cloud-admin
sudo adduser operateur-cloud
sudo usermod -aG cloud-admin operateur-cloud
groups operateur-cloud
```

- **Groupe créé :** [À compléter]
- **Utilisateur créé :** [À compléter]
- **Groupes affichés par `groups operateur-cloud` :** [À compléter]

**Capture d'écran — utilisateur et groupe :**

![Capture : création utilisateur et groupe](captures/08-utilisateur-groupe.png)

**Question :** En quoi cette manipulation illustre-t-elle le principe du moindre privilège ?

**Réponse :**  
[Expliquez pourquoi les droits doivent être attribués selon les besoins, sans donner systématiquement tous les privilèges.]

## 6. Étape 4 — Provisionnement automatisé avec Vagrant

### 6.1 Préparation du projet

Commandes exécutées sur le système hôte :

```powershell
mkdir tp-cloud-vagrant
cd tp-cloud-vagrant
vagrant init ubuntu/trusty64
vagrant box list
```

**La box `ubuntu/trusty64` était-elle présente localement ?** [Oui / Non]

### 6.2 Configuration du `Vagrantfile`

Collez ci-dessous le contenu final de votre fichier `Vagrantfile` ou vérifiez qu'il correspond à la configuration demandée.

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "vm-tp1-cloud"

  config.vm.network "private_network",
    ip: "192.168.56.110"

  config.vm.provider "virtualbox" do |vb|
    vb.name = "vm-tp1-cloud"
    vb.memory = 1024
    vb.cpus = 1
  end
end
```

**Avez-vous modifié un paramètre ?** [Non / Oui, préciser lequel et pourquoi.]

### 6.3 Déploiement et vérification

Commandes exécutées :

```bash
vagrant up
vagrant status
vagrant ssh
```

Dans la VM :

```bash
whoami
hostname
hostname -I
```

- **Le déploiement a-t-il réussi ?** [À compléter]
- **État final de la VM :** [À compléter]
- **Résultats des commandes de vérification :** [À compléter]

**Capture d'écran — déploiement (`vagrant up`) :**

![Capture : vagrant up](captures/09-vagrant-up.png)

**Capture d'écran — connexion (`vagrant ssh`) :**

![Capture : vagrant ssh](captures/10-vagrant-ssh.png)

### 6.4 Arrêt et suppression

Commandes étudiées ou exécutées :

```bash
vagrant halt
vagrant destroy -f
```

1. Que fait `vagrant halt` ?

   **Réponse :** [À compléter]

2. Que fait `vagrant destroy -f` ?

   **Réponse :** [À compléter]

3. `vagrant destroy -f` supprime-t-il la box `ubuntu/trusty64` ? Justifiez.

   **Réponse :** [À compléter]

> **Attention :** `vagrant destroy -f` supprime la VM gérée par ce projet. Ne l'exécutez qu'après avoir terminé les vérifications et conservé les captures nécessaires.

### 6.5 Infrastructure as Code (IaC)

**Question :** En quoi le fichier `Vagrantfile` illustre-t-il le concept d'Infrastructure as Code ?

**Réponse :**  
[Expliquez comment la configuration de la machine est décrite dans un fichier réutilisable et comment Vagrant l'applique.]

## 7. Comparaison entre le Cloud local et le Cloud public

Complétez la colonne **Observations / différences** avec vos propres explications.

| Concept | Cloud local du TP | Exemple dans un Cloud public | Observations / différences |
|---|---|---|---|
| Machine virtuelle | VirtualBox | Google Compute Engine / Amazon EC2 / Azure VM | [À compléter] |
| Réseau virtuel | Réseau privé VirtualBox | VPC / Virtual Network | [À compléter] |
| Pare-feu | UFW | Règles de pare-feu Cloud / Security Groups | [À compléter] |
| Accès distant | SSH | SSH / console du fournisseur | [À compléter] |
| Gestion des identités et droits | Utilisateurs et groupes Linux | IAM | [À compléter] |
| Provisionnement | Vagrant | Console, API ou Terraform | [À compléter] |
| Infrastructure physique | Ordinateur local | Datacenters du fournisseur | [À compléter] |
| Scalabilité | Limitée par les ressources du poste | Ressources potentiellement extensibles selon l'offre | [À compléter] |
| Facturation | Pas de facturation d'un service Cloud public pour cette VM locale | Facturation selon le service et l'utilisation | [À compléter] |

## 8. Questions de réflexion — réponses personnelles

Répondez avec des phrases complètes et justifiez vos réponses lorsque c'est nécessaire.

1. **Pourquoi une machine virtuelle peut-elle être considérée comme une ressource IaaS ?**  
   Réponse : [À compléter]

2. **Quel est le rôle de VirtualBox dans cette infrastructure ?**  
   Réponse : [À compléter]

3. **Quel est le rôle de Vagrant ?**  
   Réponse : [À compléter]

4. **Quelle est la différence entre une box Vagrant et une machine virtuelle ?**  
   Réponse : [À compléter]

5. **Pourquoi l'enseignant peut-il distribuer une seule box `ubuntu-trusty64.box` à toute la classe ?**  
   Réponse : [À compléter]

6. **Quelle commande permet d'ajouter une box locale à Vagrant ?**  
   Réponse : [À compléter]

7. **Quelle commande permet de vérifier que la box est disponible localement ?**  
   Réponse : [À compléter]

8. **Comment avez-vous obtenu l'adresse IP de la VM ?**  
   Réponse : [À compléter]

9. **Quelle commande permet de vérifier le fonctionnement du serveur SSH sous Ubuntu Trusty ?**  
   Réponse : [À compléter]

10. **Quelle est la différence entre `ssh vagrant@192.168.56.110` et `vagrant ssh` ?**  
    Réponse : [À compléter]

11. **Pourquoi faut-il autoriser le port 22 avant d'activer UFW ?**  
    Réponse : [À compléter]

12. **En quoi Vagrant illustre-t-il l'Infrastructure as Code ?**  
    Réponse : [À compléter]

13. **Quelle différence existe-t-il entre une infrastructure locale VirtualBox et une infrastructure Cloud publique telle que GCP ?**  
    Réponse : [À compléter]

## 9. Difficultés rencontrées

Décrivez les erreurs réellement rencontrées et les solutions que vous avez essayées.

| Difficulté / message d'erreur | Cause identifiée ou hypothèse | Solution appliquée | Résultat |
|---|---|---|---|
| [À compléter] | [À compléter] | [À compléter] | [Résolu / Non résolu] |
| [À compléter] | [À compléter] | [À compléter] | [Résolu / Non résolu] |

Si vous n'avez rencontré aucune difficulté, indiquez-le explicitement.

## 10. Conclusion personnelle

En 5 à 10 lignes, résumez ce que vous avez appris sur la virtualisation, Vagrant, le réseau virtuel, SSH, UFW, les utilisateurs Linux et l'automatisation d'une infrastructure.

**Conclusion :**  
[À compléter]

## 11. Vérification avant dépôt sur GitHub

- [ ] Les informations de l'étudiant sont complétées.
- [ ] Les tableaux contiennent les résultats observés.
- [ ] Les questions de réflexion ont toutes une réponse.
- [ ] Les captures d'écran proviennent de ma propre machine.
- [ ] Les images référencées dans le Markdown sont présentes dans `captures/`.
- [ ] Les difficultés rencontrées sont décrites honnêtement.
- [ ] Le fichier est enregistré sous `COMPTE_RENDU_TP1-2_Nom_Prenom.md`.
- [ ] Le compte rendu et les captures sont déposés dans mon dépôt GitHub conformément aux consignes de l'enseignant.
