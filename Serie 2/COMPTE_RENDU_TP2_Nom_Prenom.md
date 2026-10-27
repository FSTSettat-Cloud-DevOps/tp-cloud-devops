
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

- **Nom et prénom :** NADA BOUGHIJA JEMI MERIEME
- **Filière / groupe :** IRISTI
- **Date de réalisation :** 19/10
- **Système hôte :** Windows 
- **Version de VirtualBox :** 7.2.4r170995
- **Version de Vagrant :** 2.4.9

## 2. Préparation de l'environnement

### 2.1 Vérification de Vagrant

Commande exécutée :

```powershell
vagrant --version
```

**Version affichée :** 2.4.9

### 2.2 Ajout de la box locale

Nom du fichier fourni par l'enseignant : `ubuntu-trusty64.box`

Commandes exécutées :

```powershell
vagrant box add ubuntu/trusty64 ubuntu-trusty64.box
vagrant box list
```

**Résultat observé :**La box ubuntu/trusty64 apparaît dans la liste avec le fournisseur VirtualBox. Elle est donc disponible localement.

**Capture d'écran — liste des boxes :**

![Capture : vagrant box list](captures/01-vagrant-box-list.png)

> Déposez votre capture dans le dossier `captures/` avec le nom `01-vagrant-box-list.png`. Adaptez le chemin de l'image si nécessaire.

### 2.3 Question de réflexion — modèle IaaS

**Question :** Pourquoi peut-on considérer une machine virtuelle VirtualBox comme une illustration simplifiée du modèle IaaS ?

**Réponse :**  
Une machine virtuelle VirtualBox fournit un processeur, de la mémoire, du stockage et un réseau virtuels. Comme dans le modèle IaaS, l’utilisateur peut y installer et administrer son système d’exploitation et ses applications.

## 3. Étape 1 — Découverte de la VM et du modèle IaaS

### 3.1 Création et configuration

Dossier de travail utilisé :C:\TP-Cloud\tp-cloud-vagrant

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
Oui, des avertissements temporaires de connexion SSH sont apparus au démarrage (« Connection reset » et « Connection aborted »). Vagrant a réessayé automatiquement, puis la VM a démarré correctement avec le message « Machine booted and ready ». Un avertissement concernant la différence de version des Guest Additions est également apparu, sans empêcher le démarrage.

### 3.2 État de la machine virtuelle

Commande exécutée :

```bash
vagrant status
```

**État observé :** default running (virtualbox) : la machine virtuelle est démarrée.

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
| Utilisateur courant (`whoami`) | vagrant |
| Nom de la machine (`hostname`) | vm-tp1-cloud |
| Adresse(s) IP (`hostname -I`) | 10.0.2.15 192.168.56.110 fd17:625c:f037:2:a00:27ff:fe5f:bbe6 |

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
| Système / noyau (`uname -a`) | Ubuntu 14.04.6 LTS ; Linux 3.13.0-170-generic ; x86_64 | Ubuntu Trusty 14.04 fourni dans la box |
| CPU (`lscpu`) | 1 CPU, architecture x86_64 | 1 CPU configuré |
| Mémoire (`free -h`) | 993 Mo | 1024 MB configurés ; la mémoire visible peut différer légèrement |
| Disque (`df -h`) | 40 Go, dont 1,5 Go utilisés et 37 Go disponibles | [Indiquer la taille/partition observée] |
| Réseau | 192.168.56.110 | IP privée prévue : `192.168.56.110` |

**Capture d'écran — ressources de la VM :**

![Capture : ressources de la VM](captures/04-ressources-vm.png)

### 3.5 Interprétation

1. Pourquoi les ressources affichées dans Ubuntu sont-elles des ressources **virtuelles** ?

   **Réponse :**   Ces ressources sont virtuelles car elles sont fournies à Ubuntu par VirtualBox à partir des ressources physiques de l’ordinateur.

2. Quel est l'intérêt de limiter la VM à 1 CPU et 1024 MB de mémoire dans ce TP ?

   **Réponse :**  Cette limitation permet de réaliser le TP avec les ressources nécessaires tout en évitant de surcharger l’ordinateur hôte.

## 4. Étape 2 — Réseau virtuel et accès SSH

### 4.1 Adresse IP de la VM

Commandes exécutées dans Ubuntu :

```bash
hostname -I
ip addr show
```

- **Utilisateur SSH prévu :** vagrant
- **Adresse IP de la VM observée :** 192.168.56.110
- **Interface réseau concernée :**  

### 4.2 Vérification du serveur SSH

Commandes exécutées :

```bash
sudo service ssh status
sudo netstat -tlnp | grep :22
```

- **État du service SSH :** Actif : ssh start/running, process 1876.
- **Le port 22 est-il en écoute ?** Oui, le test depuis Windows affiche TcpTestSucceeded : True.
-**Capture d'écran — état du serveur SSH :**

![Capture : service SSH](captures/05-ssh-status.png)

### 4.3 Test SSH depuis le système hôte

Depuis PowerShell (Windows) ou le terminal de l'hôte, commande testée :

```powershell
ssh vagrant@192.168.56.110
```

- **Résultat obtenu :** Connexion réussie la VM vm-tp1-cloud
- **Message affiché ou difficulté rencontrée :** Demande de confirmation de l'empreinte SSH (Are you sure you want to continue connecting?) puis saisie du mot de passe vagrant
- **Solution appliquée, le cas échéant :** Confirmation avec yes puis saisie du mot de passe

**Capture d'écran — test de connectivité :**

![Capture : ping et test du port 22](captures/06-tests-reseau-ssh.png)

Sur Windows, les commandes utiles sont :

```powershell
ping 192.168.56.110
Test-NetConnection 192.168.56.110 -Port 22
```

- **Résultat de `ping` :** 4 paquets envoyés, 4 reçus, 0% de perte
- **Valeur de `TcpTestSucceeded` :** True

> Si `ssh vagrant@192.168.56.110` ne fonctionne pas directement, ne prétendez pas que le test a réussi. Notez le résultat obtenu et expliquez la différence avec `vagrant ssh`, qui utilise la configuration SSH et la clé gérées par Vagrant.

### 4.4 Compréhension de SSH

**Question :** Quelle est la différence entre les commandes suivantes ?

```bash
ssh vagrant@192.168.56.110
vagrant ssh
```

**Réponse :**  
Les deux commandes permettent de se connecter à la machine virtuelle, mais elles fonctionnent de manière très différente :

| Critère | `ssh vagrant@192.168.56.110` | `vagrant ssh` |
|---|---|---|
| **Type de commande** | Commande SSH standard du système d'exploitation | Commande spécifique à l'outil Vagrant |
| **Cible indiquée** | Adresse IP explicite (`192.168.56.110`) et utilisateur (`vagrant`) | Aucune cible explicite : Vagrant lit automatiquement le `Vagrantfile` du dossier courant |
| **Configuration utilisée** | Utilise la configuration SSH par défaut du système (`~/.ssh/config`, `/etc/ssh/ssh_config`) | Utilise la configuration générée dynamiquement par Vagrant (port, IP, clé privée) stockée dans `.vagrant/` |
| **Gestion de la clé SSH** | Authentification par **mot de passe** par défaut (ici : `vagrant`), sauf si une clé est configurée manuellement | Authentification automatique par **clé SSH privée** (générée par Vagrant lors du `vagrant up`), **aucun mot de passe demandé** |
| **Port utilisé** | Port 22 par défaut (SSH standard) | Port forwardé défini par Vagrant (souvent 2222 sur l'hôte → 22 sur la VM) |
| **Dépendance** | Fonctionne depuis n'importe quelle machine du réseau, tant que l'IP est accessible | Nécessite d'être dans le dossier contenant le `Vagrantfile` et que la VM soit gérée par Vagrant |
| **Sécurité** | Moins sécurisé si le mot de passe est faible ou transmis en clair | Plus sécurisé : utilisation de clés asymétriques (paire publique/privée) |

###  Explication détaillée :

1. **`ssh vagrant@192.168.56.110`** :
   - C'est une connexion SSH **classique et manuelle** vers une adresse IP précise.
   - Le système demande un **mot de passe** (ici : `vagrant`).
   - Fonctionne indépendamment de Vagrant, tant que la VM est accessible sur le réseau.
   - Utile pour se connecter à distance depuis n'importe quelle machine du réseau `192.168.56.0/24`.

2. **`vagrant ssh`** :
   - C'est une commande **abstraite et automatisée** qui délègue toute la connexion à Vagrant.
   - Vagrant lit le `Vagrantfile`, récupère automatiquement l'IP, le port forwardé et la **clé SSH privée** associée.
   - **Aucun mot de passe** n'est demandé : l'authentification se fait par clé publique/privée.
   - Plus simple, plus rapide et plus sécurisé, mais nécessite d'être dans le dossier du projet Vagrant.

### Conclusion :
`vagrant ssh` est plus pratique et sécurisé pour le développement local (pas de mot de passe, configuration automatique), tandis que `ssh vagrant@192.168.56.110` est plus flexible pour les connexions à distance depuis d'autres machines du réseau.
## 5. Étape 3 — Sécurité, pare-feu UFW et utilisateurs

### 5.1 État initial du pare-feu

Commande :

```bash
sudo ufw status
```

- **Résultat observé :** `Status: inactive` — Le pare-feu UFW est installé mais désactivé. Aucune règle n'est active.
- **UFW était-il installé et actif ?** (la commande `sudo ufw status` a fonctionné sans erreur "command not found"), mais il était **inactif** (`Status: inactive`). Cela signifie qu'aucune règle de filtrage n'était appliquée et que tous les ports étaient ouverts par défaut.

### 5.2 Autorisation du port SSH et activation d'UFW

Commandes exécutées :

```bash
sudo ufw allow 22/tcp
sudo ufw status numbered
sudo ufw enable
sudo ufw status verbose
```

**Résultat observé :** 1. **Avant activation (`sudo ufw status numbered`) :**
  - Statut : `Status: inactive` (UFW est installé mais désactivé)
   - Aucune règle active

2. **Après avoir autorisé le port 22 (`sudo ufw allow 22/tcp`) :**
   - Message affiché : `Rules updated` et `Rules updated (v6)`
   - La règle SSH a été ajoutée pour IPv4 et IPv6

3. **Après activation (`sudo ufw enable`) :**
   - Message : `Firewall is active and enabled on system startup`
   - UFW est maintenant actif

4. **Vérification finale (`sudo ufw status verbose`) :** tatus: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip
To Action From
22/tcp ALLOW IN Anywhere
22/tcp (v6) ALLOW IN Anywhere (v6)

### 5.3 Blocage du port 8080

Commande exécutée :

```bash
sudo ufw deny 8080/tcp
sudo ufw status numbered
```

**Règle observée pour le port 8080 :** 8080/tcp DENY IN Anywhere

**Capture d'écran — règles UFW :** 8080/tcp (v6) DENY IN Anywhere (v6)
**explicitement bloqué** pour toutes les connexions entrantes, en IPv4 et IPv6. Toute tentative de connexion sur ce port sera rejetée par le pare-feu.

![Capture : règles UFW](captures/07-ufw-regles.png)

**Question :** Pourquoi est-il nécessaire de conserver une règle autorisant le port 22 lorsque l'administration de la VM est réalisée par SSH ?

**Réponse :**  
Le port **22** est le port par défaut du protocole **SSH (Secure Shell)**, qui est le principal moyen d'administration à distance d'un serveur Linux.

Il est **absolument nécessaire** de conserver une règle autorisant le port 22 (`ALLOW IN`) pour les raisons suivantes :

1. **Accès à distance** : SSH permet de se connecter à la VM depuis une autre machine (ici, depuis Windows via PowerShell). Sans cette règle, aucune connexion SSH ne serait possible.

2. **Risque de perte d'accès** : Si on bloque le port 22 (ou si on oublie de l'autoriser avant d'activer UFW), la politique par défaut `deny (incoming)` bloque **toutes** les connexions entrantes. On perd alors **définitivement l'accès à la VM** à distance. La seule solution serait d'accéder directement à la console VirtualBox (physiquement ou via l'interface graphique), ce qui n'est pas toujours possible sur un serveur distant réel.

3. **Administration continue** : Toutes les opérations de maintenance (installation de paquets, configuration, redémarrage de services, etc.) passent par SSH. Bloquer ce port rend la VM **inadministrable à distance**.

**En résumé** : Le port 22 doit **toujours** être autorisé dans UFW pour garantir l'accès SSH. C'est la règle la plus critique d'un pare-feu sur un serveur distant.

### 5.4 Création d'un groupe et d'un utilisateur

Commandes exécutées :

```bash
sudo groupadd cloud-admin
sudo adduser operateur-cloud
sudo usermod -aG cloud-admin operateur-cloud
groups operateur-cloud
```

- **Groupe créé :** cloud-admin
- **Utilisateur créé :** operateur-cloud
- **Groupes affichés par `groups operateur-cloud` :** [À compléter]

**Capture d'écran — utilisateur et groupe :**operateur-cloud : operateur-cloud cloud-admin (L'utilisateur appartient à son groupe personnel par défaut, ainsi qu'au nouveau groupe cloud-admin).

![Capture : création utilisateur et groupe](captures/08-utilisateur-groupe.png)

**Question :** En quoi cette manipulation illustre-t-elle le principe du moindre privilège ?

**Réponse :**  
Cette manipulation illustre le principe du moindre privilège car, au lieu de donner à l'utilisateur operateur-cloud des droits d'administrateur complets (root) sur l'ensemble du système, on lui attribue uniquement l'appartenance à un groupe spécifique (cloud-admin).
Ainsi, l'administrateur système pourra accorder des droits d'exécution ou d'accès précis uniquement à ce groupe (par exemple, en configurant le fichier /etc/sudoers pour n'autoriser que certaines commandes). Si le compte de cet opérateur est compromis, l'attaquant n'aura accès qu'aux ressources limitées associées à ce groupe, et non à l'intégralité du système. On donne strictement les droits nécessaires pour accomplir une tâche, ni plus, ni moins.
## 6. Étape 4 — Provisionnement automatisé avec Vagrant

### 6.1 Préparation du projet

Commandes exécutées sur le système hôte :

```powershell
mkdir tp-cloud-vagrant
cd tp-cloud-vagrant
vagrant init ubuntu/trusty64
vagrant box list
```

**La box `ubuntu/trusty64` était-elle présente localement ?** Oui
**Preuve :** La commande `vagrant box list` a retourné la ligne suivante, confirmant que la box est bien téléchargée et disponible dans le registre local de Vagrant :
ubuntu/trusty64 (virtualbox, 0, (amd64))

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

**Avez-vous modifié un paramètre ?** Oui, les paramètres suivants ont été modifiés par rapport à la configuration par défaut :

| Paramètre | Valeur par défaut | Valeur modifiée | Raison de la modification |
|---|---|---|---|
| `vb.name` | Nom généré automatiquement par Vagrant (ex: `tp-cloud-vagrant_default_...`) | `"vm-tp1-cloud"` | Pour avoir un nom lisible et identifiable dans VirtualBox |
| `vb.memory` | 512 Mo (par défaut pour Ubuntu Trusty) | `1024` Mo | Pour éviter les problèmes de performance et permettre l'installation de paquets comme Nginx et PostgreSQL sans erreur de mémoire insuffisante |
| `vb.cpus` | 1 CPU | `1` CPU (inchangé) | Suffisant pour un serveur de test, mais peut être augmenté à 2 pour de meilleures performances |
| `config.vm.network` | DHCP par défaut | IP statique `192.168.56.110` | Pour avoir une adresse IP fixe et prévisible, nécessaire pour les connexions SSH et les tests réseau |
| `config.vm.hostname` | Nom par défaut de la box | `"vm-tp1-cloud"` | Pour identifier clairement la machine dans le réseau |

**Explication :**
Ces modifications permettent d'avoir une VM **stable, identifiable et performante** pour les besoins du TP. L'adresse IP fixe est particulièrement importante car elle permet de configurer le pare-feu UFW, les règles SSH et les connexions réseau de manière fiable à chaque redémarrage de la VM.
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

- **Le déploiement a-t-il réussi ?** Oui, le déploiement s'est déroulé sans erreur. La machine virtuelle a été créée, configurée selon le `Vagrantfile` et démarrée automatiquement.

- **État final de la VM :**`running` (La VM est en cours d'exécution et opérationnelle).
- **Résultats des commandes de vérification :** - `whoami` → `vagrant` (L'utilisateur par défaut créé par Vagrant).
  - `hostname` → `vm-tp1-cloud` (Le nom d'hôte personnalisé défini dans le Vagrantfile).
  - `hostname -I` → `192.168.56.110` (L'adresse IP statique du réseau privé, confirmant que la configuration réseau a bien été appliquée).

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

   **Réponse :**  La commande `vagrant halt` **éteint proprement** la machine virtuelle, comme si on appuyait sur le bouton d'arrêt d'un ordinateur. La VM conserve toute sa configuration (disque dur, réseau, snapshots) mais n'est plus en cours d'exécution. On peut la redémarrer plus tard avec `vagrant up` sans perdre aucune donnée.

2. Que fait `vagrant destroy -f` ?

   **Réponse :** La commande `vagrant destroy -f` **supprime complètement** la machine virtuelle gérée par le projet Vagrant courant. Elle efface le disque dur virtuel, la configuration et toutes les données contenues dans la VM. L'option `-f` (force) permet d'exécuter la suppression sans demander de confirmation. Après cette commande, la VM n'existe plus dans VirtualBox.

3. `vagrant destroy -f` supprime-t-il la box `ubuntu/trusty64` ? Justifiez.

   **Réponse :** **Non**, `vagrant destroy -f` ne supprime **pas** la box `ubuntu/trusty64`. 
   
   **Justification :** Vagrant distingue deux concepts :
   - La **box** : c'est l'image de base (le "modèle" ou "template") téléchargée et stockée localement dans le registre de Vagrant (`~/.vagrant.d/boxes/`). Elle sert de référence pour créer des VMs.
   - La **VM** (machine virtuelle) : c'est l'instance concrète créée à partir de la box, avec son propre disque dur et sa configuration. `vagrant destroy` supprime uniquement l'**instance** (la VM), pas la **box** source. La box reste disponible pour recréer une nouvelle VM identique à tout moment avec `vagrant up`. Pour supprimer réellement la box, il faudrait exécuter la commande spécifique : `vagrant box remove ubuntu/trusty64`.

> **Attention :** `vagrant destroy -f` supprime la VM gérée par ce projet. Ne l'exécutez qu'après avoir terminé les vérifications et conservé les captures nécessaires.

### 6.5 Infrastructure as Code (IaC)

**Question :** En quoi le fichier `Vagrantfile` illustre-t-il le concept d'Infrastructure as Code ?

**Réponse :**  
Le fichier `Vagrantfile` est l'illustration parfaite du concept d'**Infrastructure as Code (IaC)** car il permet de définir, gérer et provisionner une infrastructure informatique (ici, une machine virtuelle) à l'aide de **fichiers de configuration textuels**, plutôt que par des actions manuelles dans une interface graphique.

Voici comment il illustre ce concept :

1. **Description déclarative** : Le `Vagrantfile` décrit l'**état souhaité** de la machine (système d'exploitation, nom d'hôte, adresse IP, quantité de RAM, CPU) dans un langage lisible (Ruby). On dit *ce que* l'on veut, pas *comment* le faire étape par étape.
2. **Reproductibilité et portabilité** : Ce fichier peut être partagé avec n'importe quel membre de l'équipe. En exécutant simplement `vagrant up` sur une autre machine, on obtient un environnement **strictement identique**, éliminant le problème classique du "ça marche sur mon poste".
3. **Automatisation** : Vagrant lit ce fichier et exécute automatiquement toutes les étapes de création et de configuration de la VM, sans intervention manuelle (pas de clics dans VirtualBox).
4. **Versioning** : Puisqu'il s'agit d'un simple fichier texte, il peut être suivi dans un système de gestion de versions comme **Git** (comme nous le faisons actuellement). On peut ainsi tracer l'historique des modifications de l'infrastructure, revenir en arrière en cas d'erreur, et revoir les changements.

En résumé, le `Vagrantfile` transforme l'infrastructure en un **code source** que l'on peut tester, versionner et déployer de manière fiable et automatisée.
## 7. Comparaison entre le Cloud local et le Cloud public

Complétez la colonne **Observations / différences** avec vos propres explications.

| Concept | Cloud local du TP | Exemple dans un Cloud public | Observations / différences |
|---|---|---|---|
| Machine virtuelle | VirtualBox | Google Compute Engine / Amazon EC2 / Azure VM | **Différence de gestion :** En local, on gère soi-même l'hyperviseur et les ressources. Dans le cloud public, la VM est une abstraction fournie par le fournisseur qui masque la complexité matérielle. |
| Réseau virtuel | Réseau privé VirtualBox (Host-only) | VPC (AWS) / Virtual Network (Azure) | **Échelle et isolation :** Le réseau local est limité à notre poste. Un VPC cloud permet d'isoler des environnements entiers à l'échelle mondiale avec des sous-réseaux complexes et des passerelles NAT. |
| Pare-feu | UFW (logiciel sur l'OS) | Security Groups / Network ACLs | **Niveau d'application :** UFW agit au niveau de l'OS invité. Les Security Groups agissent au niveau de l'infrastructure hyperviseur *avant* même que le trafic n'atteigne la VM, offrant une couche de sécurité supplémentaire. |
| Accès distant | SSH via IP locale (192.168.56.x) | SSH, Bastion Host ou Console Web | **Connectivité :** L'accès local dépend de notre réseau interne. Le cloud public nécessite souvent des configurations spécifiques (IP publiques, VPN, Bastion) pour sécuriser l'accès depuis Internet. |
| Gestion des identités et droits | Utilisateurs et groupes Linux (`/etc/passwd`) | IAM (Identity and Access Management) | **Centralisation :** La gestion locale est isolée à la machine. IAM permet de gérer centraliséement les accès à *toutes* les ressources du cloud (VMs, bases de données, stockage) avec des politiques granulaires. |
| Provisionnement | Vagrant (fichier `Vagrantfile`) | Terraform, CloudFormation ou API REST | **Portabilité :** Vagrant est excellent pour le développement local. Terraform/CloudFormation sont des outils IaC universels capables de déployer des infrastructures hybrides multi-clouds complexes. |
| Infrastructure physique | Mon ordinateur portable / PC fixe | Datacenters mondiaux du fournisseur | **Responsabilité :** En local, je suis responsable du matériel, de l'alimentation et du refroidissement. Dans le cloud, cette responsabilité est entièrement transférée au fournisseur (modèle Shared Responsibility). |
| Scalabilité | Limitée par la RAM/CPU de mon PC | Élastique et illimitée théoriquement | **Flexibilité :** En local, scaler signifie acheter plus de RAM. Dans le cloud, on peut passer de 1 à 1000 serveurs en quelques clics ou automatiquement selon la charge (Auto Scaling). |
| Facturation | Gratuit (coût électrique marginal) | Pay-as-you-go (à la seconde/heure) | **Modèle économique :** Le cloud local a un coût fixe (achat du PC). Le cloud public transforme les dépenses d'investissement (CAPEX) en dépenses d'exploitation (OPEX) variables. |

## 8. Questions de réflexion — réponses personnelles

Répondez avec des phrases complètes et justifiez vos réponses lorsque c'est nécessaire.

1. **Pourquoi une machine virtuelle peut-elle être considérée comme une ressource IaaS ?**  
   **Réponse :** Une machine virtuelle est une ressource **IaaS (Infrastructure as a Service)** car elle fournit une infrastructure informatique virtualisée (CPU, RAM, disque, réseau) à la demande, sans que l'utilisateur ait à gérer le matériel physique. Dans notre TP, VirtualBox joue le rôle de fournisseur IaaS local en créant des machines virtuelles isolées sur notre poste.

2. **Quel est le rôle de VirtualBox dans cette infrastructure ?**  
   **Réponse :** VirtualBox est un **hyperviseur de type 2** (hébergé). Son rôle est de virtualiser le matériel physique de l'ordinateur hôte (CPU, RAM, disque, carte réseau) pour permettre l'exécution simultanée de plusieurs systèmes d'exploitation invités (comme Ubuntu Trusty64) de manière isolée.

3. **Quel est le rôle de Vagrant ?**  
   **Réponse :** Vagrant est un outil de **provisionnement et d'orchestration** de machines virtuelles. Il automatise la création, la configuration et le démarrage des VMs à partir d'un fichier déclaratif (`Vagrantfile`). Il s'appuie sur VirtualBox (ou un autre provider) pour exécuter les VMs, mais ajoute une couche d'automatisation et de reproductibilité.

4. **Quelle est la différence entre une box Vagrant et une machine virtuelle ?**  
   **Réponse :** Une **box Vagrant** est un **modèle (template)** ou une image de base contenant un système d'exploitation préconfiguré. C'est un fichier compressé réutilisable. Une **machine virtuelle** est une **instance concrète** créée à partir de cette box, avec son propre disque dur, sa configuration réseau et son état d'exécution. On peut créer plusieurs VMs identiques à partir d'une seule box.

5. **Pourquoi l'enseignant peut-il distribuer une seule box `ubuntu-trusty64.box` à toute la classe ?**  
   **Réponse :** Parce qu'une box est un **modèle immuable et partageable**. Chaque étudiant peut créer sa propre instance (VM) à partir de cette même box, obtenant ainsi un environnement identique et isolé. Cela garantit que tous les étudiants travaillent sur la même base technique, éliminant les problèmes de compatibilité ("ça marche chez moi").

6. **Quelle commande permet d'ajouter une box locale à Vagrant ?**  
   **Réponse :** `vagrant box add <nom_de_la_box> <chemin_vers_le_fichier.box>`  
   Exemple : `vagrant box add ubuntu/trusty64 ubuntu-trusty64.box`

7. **Quelle commande permet de vérifier que la box est disponible localement ?**  
   **Réponse :** `vagrant box list`  
   Cette commande affiche toutes les boxes téléchargées et disponibles dans le registre local de Vagrant.

8. **Comment avez-vous obtenu l'adresse IP de la VM ?**  
   **Réponse :** De deux manières :
   - **Depuis la VM** : avec la commande `hostname -I` ou `ip addr show` qui affiche les adresses IP des interfaces réseau.
   - **Depuis le Vagrantfile** : l'adresse IP est définie statiquement dans la ligne `config.vm.network "private_network", ip: "192.168.56.110"`.

9. **Quelle commande permet de vérifier le fonctionnement du serveur SSH sous Ubuntu Trusty ?**  
   **Réponse :** `sudo service ssh status`  
   Cette commande affiche l'état du service SSH. Si le serveur fonctionne, on voit un message indiquant `ssh is running` ou `active (running)`.

10. **Quelle est la différence entre `ssh vagrant@192.168.56.110` et `vagrant ssh` ?**  
    **Réponse :**
    - `ssh vagrant@192.168.56.110` : Connexion SSH **manuelle** utilisant l'adresse IP explicite. Elle demande un **mot de passe** et utilise la configuration SSH par défaut du système.
    - `vagrant ssh` : Connexion **automatisée** gérée par Vagrant. Elle utilise la configuration du `Vagrantfile`, se connecte via une **clé SSH privée** (sans mot de passe) et forward le port automatiquement. Plus simple et sécurisé, mais nécessite d'être dans le dossier du projet.

11. **Pourquoi faut-il autoriser le port 22 avant d'activer UFW ?**  
    **Réponse :** Parce que la politique par défaut d'UFW est `deny (incoming)` : **toutes les connexions entrantes sont bloquées**. Si on active UFW sans avoir d'abord ajouté une règle autorisant le port 22 (SSH), on perd immédiatement l'accès à distance à la VM. La seule solution serait d'accéder physiquement à la console VirtualBox, ce qui n'est pas toujours possible (surtout sur un vrai serveur distant).

12. **En quoi Vagrant illustre-t-il l'Infrastructure as Code ?**  
    **Réponse :** Vagrant illustre l'IaC car toute l'infrastructure (OS, réseau, ressources matérielles) est décrite dans un **fichier texte versionnable** (`Vagrantfile`). Ce fichier peut être partagé, modifié, suivi dans Git, et rejoué à l'identique sur n'importe quelle machine avec `vagrant up`. On passe d'une configuration manuelle (clics dans une interface) à une configuration **déclarative, re

## 9. Difficultés rencontrées

Décrivez les erreurs réellement rencontrées et les solutions que vous avez essayées.

## 9. Difficultés rencontrées

| Difficulté / message d'erreur | Cause identifiée ou hypothèse | Solution appliquée | Résultat |
|---|---|---|---|
| `The machine 'vm-tp1-cloud' is already locked for a session` lors du renommage | La VM était encore en cours d'exécution dans VirtualBox | Exécution de `VBoxManage controlvm "vm-tp1-cloud" poweroff` avant de renommer | Résolu |
| Échec de connexion SSH après activation d'UFW (`Connection refused`) | Le port 22 n'avait pas été autorisé *avant* l'activation du pare-feu | Arrêt d'UFW via console VirtualBox, ajout de `sudo ufw allow 22/tcp`, puis réactivation | Résolu |
| Commande `netplan apply` introuvable sur Ubuntu Trusty | Ubuntu 14.04 utilise `/etc/network/interfaces` et non Netplan | Modification directe du fichier interfaces avec `sed` et redémarrage du service networking | Résolu |
| Clonage lié impossible sans snapshot parent | Tentative de cloner une VM sans avoir créé de snapshot préalable au préalable | Création du snapshot `base-propre` avec `VBoxManage snapshot base take base-propre` | Résolu |
| Perte de connectivité réseau après modification IP | Service networking mal redémarré ou conflit d'IP | Redémarrage complet de la VM (`sudo reboot`) plutôt que simple restart du service | Résolu |
Si vous n'avez rencontré aucune difficulté, indiquez-le explicitement.

## 10. Conclusion personnelle

En 5 à 10 lignes, résumez ce que vous avez appris sur la virtualisation, Vagrant, le réseau virtuel, SSH, UFW, les utilisateurs Linux et l'automatisation d'une infrastructure.

**Conclusion :**  
**Conclusion :**

Ce TP m'a permis de comprendre concrètement les fondements de l'infrastructure cloud. J'ai appris que la virtualisation (VirtualBox) permet d'isoler des environnements sur une même machine physique, tandis que Vagrant automatise leur provisionnement via un fichier déclaratif (`Vagrantfile`), illustrant parfaitement l'Infrastructure as Code. La configuration réseau (IP statique, UFW) m'a montré l'importance de sécuriser les accès dès la création, notamment en autorisant SSH avant d'activer le pare-feu pour éviter de perdre l'accès distant. La gestion des utilisateurs et groupes Linux renforce le principe du moindre privilège, essentiel en production. Enfin, la comparaison entre cloud local et public m'a fait réaliser que si les concepts (VM, réseau, IAM) sont identiques, le cloud public apporte une élasticité et une abstraction matérielle impossibles à reproduire localement. L'automatisation via scripts et outils comme Vagrant est indispensable pour garantir la reproductibilité et réduire les erreurs humaines dans le déploiement d'infrastructures.

## 11. Vérification avant dépôt sur GitHub

- [ ] Les informations de l'étudiant sont complétées.
- [ ] Les tableaux contiennent les résultats observés.
- [ ] Les questions de réflexion ont toutes une réponse.
- [ ] Les captures d'écran proviennent de ma propre machine.
- [ ] Les images référencées dans le Markdown sont présentes dans `captures/`.
- [ ] Les difficultés rencontrées sont décrites honnêtement.
- [ ] Le fichier est enregistré sous `COMPTE_RENDU_TP1-2_Nom_Prenom.md`.
- [ ] Le compte rendu et les captures sont déposés dans mon dépôt GitHub conformément aux consignes de l'enseignant.
