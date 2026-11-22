# TP : Introduction à Kubernetes

## Déploiement, exposition et mise à l'échelle d'une application Web

**Université Hassan I -- Faculté des Sciences et Techniques de Settat**\
**Module :** Cloud Computing et DevOps\
**Enseignant :** Pr. Abdelfattah Abassi

------------------------------------------------------------------------

## Identification de l'étudiant(e)

-   **Nom :** boughija
-   **Prénom :** nada
-   **Filière :** IRISTI
-   **Groupe :** binome
-   **Identifiant GitHub :**
-   **Date du TP :**18/11/2026

> **Consigne :** Répondez à toutes les questions dans les espaces
> prévus. Lorsque la question demande une observation, indiquez le
> résultat réellement obtenu sur votre ordinateur. Ajoutez les captures
> d'écran demandées dans le dossier `preuves/`.

------------------------------------------------------------------------

# Préparation de l'environnement

Après avoir démarré Minikube, exécuté `kubectl cluster-info` et
`kubectl get nodes`, répondez aux questions suivantes.

### 1. Qu'est-ce qu'un cluster Kubernetes ?

**Réponse :**

```{=html}
Un ensemble de machines (nœuds) qui travaillent ensemble pour exécuter des applications conteneurisées. Il comprend un plan de contrôle (Control Plane) qui gère l'état souhaité du cluster et des nœuds de travail (Worker Nodes) qui hébergent les Pods contenant les conteneurs de l'application.
```
### 2. Que représente un nœud (Node) ?

**Réponse :**

```{=html}
Une machine physique ou virtuelle (dans notre cas, un conteneur Docker via Minikube) sur laquelle les Pods sont exécutés. Chaque nœud contient les services nécessaires pour faire tourner les Pods : kubelet (agent de communication), container runtime (Docker/containerd) et kube-proxy (gestion réseau).
```
### 3. Quelle est la différence générale entre Docker et Kubernetes ?

**Réponse :**

```{=html}
Docker est un outil de conteneurisation qui permet de créer et d'exécuter des conteneurs individuellement ou via Compose sur une seule machine. Kubernetes est un orchestrateur qui gère automatiquement le déploiement, la mise à l'échelle, la résilience (auto-réparation) et la mise en réseau de centaines ou milliers de conteneurs répartis sur plusieurs machines.
```
### 4. Quel est le rôle de `kubectl` ?

**Réponse :**

```{=html}
C'est l'outil en ligne de commande qui sert d'interface pour communiquer avec l'API Server du cluster Kubernetes. Il permet de créer, inspecter, modifier et supprimer des ressources (Pods, Deployments, Services, etc.) en envoyant des requêtes REST à l'API Server.
```

------------------------------------------------------------------------

# Partie 1 -- Découverte du cluster

Commandes utilisées : `kubectl get nodes`,
`kubectl describe node minikube`, `kubectl get pods -A` et
`kubectl get namespaces`.

### 1. Combien de nœuds contient votre cluster ?

**Réponse :** Le cluster contient un seul nœud nommé minikube. C'est le comportement normal d'un environnement local Minikube, qui simule un cluster à nœud unique pour le développement et les tests.

### 2. Quel est le statut du nœud ?

**Réponse :** Le statut du nœud est Ready. Cela indique que le nœud est sain, que le kubelet communique correctement avec l'API Server, et qu'il est prêt à accepter et à exécuter des Pods.

### 3. Relever trois Pods du namespace `kube-system`.

**Réponse :** D'après la commande kubectl get pods -A, voici trois Pods du namespace kube-system (les noms exacts peuvent varier légèrement à cause des identifiants aléatoires) :

-   Pod 1 :coredns-559f6c778d-7lhdj
-   Pod 2 :etcd-minikube
-   Pod 3 :kube-apiserver-minikube

### 4. Quel est le rôle du namespace `kube-system` ?

**Réponse :** Le namespace kube-system est réservé aux composants internes du plan de contrôle (Control Plane) et aux services essentiels au fonctionnement même du cluster Kubernetes (comme l'API Server, le Scheduler, etcd, CoreDNS, etc.). Il ne doit pas être utilisé pour déployer des applications utilisateur.

------------------------------------------------------------------------

# Partie 2 -- Premier déploiement Nginx

Après avoir créé le Deployment `nginx-app` et exécuté les commandes
d'observation :

### 1. Combien de Pods ont été créés ?

**Réponse :** 1 Pod a été créé. Son nom est nginx-app-594c6dfcf4-g5qbw et son statut est Running (1/1 READY).

### 2. Quel est le rôle du ReplicaSet ?

**Réponse :** Le rôle du ReplicaSet est de veiller en permanence à ce que le nombre de Pods spécifié dans le Deployment (ici, 1) soit maintenu en état de fonctionnement. Si un Pod est supprimé ou tombe en panne, le ReplicaSet en recrée automatiquement un nouveau pour respecter l'état souhaité.

### 3. Le Deployment exécute-t-il directement le conteneur ?

**Réponse :** Non. Le Deployment est une couche d'abstraction de haut niveau. Il crée et gère un ReplicaSet, et c'est ce ReplicaSet qui est responsable de la création et de la gestion des Pods (qui eux-mêmes hébergent les conteneurs).

### 4. Quelle est la différence entre un Pod et un conteneur Docker ?

**Réponse :** Un conteneur Docker est une instance isolée d'une image qui exécute un processus. Un Pod est la plus petite unité déployable dans Kubernetes. C'est une enveloppe logique qui peut contenir un ou plusieurs conteneurs Docker qui partagent le même espace de noms réseau (même adresse IP) et le même stockage.

## Observation d'un Pod

Après avoir exécuté `kubectl describe pod NOM_DU_POD` et
`kubectl logs NOM_DU_POD`, complétez le tableau.

  Information demandée   Résultat observé
  ---------------------- ------------------
  Nom du Pod   nginx-app-594c6dfcf4-g5qbw          
  Statut du Pod    Running      
  Image utilisée  nginx       

------------------------------------------------------------------------

# Partie 3 -- Exposer l'application avec un Service

Après avoir créé le Service avec
`kubectl expose deployment nginx-app --type=NodePort --port=80`, puis
exécuté `minikube service nginx-app` :

### 1. Pourquoi éviter d'utiliser directement l'adresse IP d'un Pod pour accéder à l'application ?

**Réponse :** L'adresse IP d'un Pod est éphémère. Si le Pod est supprimé, redémarré ou recréé (par exemple lors d'une mise à jour ou d'une panne), il obtiendra automatiquement une nouvelle adresse IP. Utiliser directement cette IP rendrait l'application inaccessible après chaque changement.

### 2. Quel est le rôle du Service ?

**Réponse :** Le Service fournit un point d'accès réseau stable et permanent (une adresse IP fixe nommée ClusterIP et un nom DNS) vers un ensemble de Pods dynamiques. Il agit comme un équilibreur de charge interne qui route le trafic vers les Pods sains correspondant à ses sélecteurs (labels).

### 3. Quelle est la différence entre ClusterIP et NodePort ?

**Réponse :** ClusterIP (valeur par défaut) : Rend le Service accessible uniquement à l'intérieur du cluster Kubernetes (par les autres Pods).
NodePort : Expose le Service sur un port statique (compris entre 30000 et 32767, ici 32092) sur chaque nœud du cluster, permettant un accès à l'application depuis l'extérieur du cluster (par exemple, depuis ton navigateur Windows via http://127.0.0.1:57719 ou http://192.168.49.2:32092).

### 4. Quel port est utilisé par Nginx dans le conteneur ?

**Réponse :** Le port 80. Cela est confirmé par le champ TargetPort: 80/TCP et l'Endpoint: 10.244.0.4:80 dans la sortie de kubectl describe service.

## Observation du Service

  Information demandée                    Résultat observé
  --------------------------------------- ------------------
  Nom du Service                          nginx-app
  Type du Service                         NodePort
  Port du Service                         80
  Port cible (`targetPort`), si affiché   80
  Port NodePort, si affiché               32092

------------------------------------------------------------------------

# Partie 4 -- Scaling et auto-réparation

Après avoir exécuté `kubectl scale deployment nginx-app --replicas=3` :

### 1. Combien de Pods sont maintenant en fonctionnement ?

**Réponse :** 3 Pods sont maintenant en fonctionnement (statut Running), comme demandé par la commande kubectl scale deployment nginx-app --replicas=3. On peut le voir avec les noms : nginx-app-594c6dfcf4-b4vxn, nginx-app-594c6dfcf4-g5qbw et nginx-app-594c6dfcf4-q5zm5.

### 2. Pourquoi peut-on avoir besoin de plusieurs réplicas d'une application ?

**Réponse :** Pour assurer la haute disponibilité (si un Pod plante, les autres continuent de servir les utilisateurs sans interruption), la répartition de charge (le trafic est divisé entre plusieurs instances pour éviter la surcharge) et la montée en charge (scalabilité horizontale pour gérer un plus grand nombre de requêtes simultanées).

## Test de l'auto-réparation

Après avoir supprimé un Pod avec `kubectl delete pod NOM_DU_POD`,
observez les Pods avec `kubectl get pods -w`.

### 3. Pourquoi Kubernetes a-t-il créé un nouveau Pod ?

**Réponse :** Parce que le contrôleur (ReplicaSet) surveille en permanence l'état du cluster. Lorsqu'il a détecté que le nombre de Pods actifs était inférieur au nombre désiré spécifié dans le Deployment (3), il a automatiquement ordonné la création d'un nouveau Pod pour respecter l'état souhaité (c'est le principe d'auto-réparation ou self-healing).

### 4. Quel composant veille au nombre de Pods souhaité ?

**Réponse :** Le ReplicaSet (qui est géré par le Deployment Controller).

### 5. Le nouveau Pod possède-t-il nécessairement le même nom que l'ancien ?

**Réponse :** Non. Le nom du Pod est généré dynamiquement par Kubernetes en ajoutant un suffixe aléatoire (hash) au nom du ReplicaSet. Le nouveau Pod aura donc un nom différent (par exemple, si on supprime g5qbw, le nouveau pourrait s'appeler nginx-app-594c6dfcf4-xyz12).

### 6. Que se passerait-il si deux Pods étaient supprimés ?

**Réponse :** Kubernetes détecterait immédiatement l'écart (il n'en resterait qu'1 au lieu de 3) et lancerait la création de deux nouveaux Pods simultanément pour revenir à l'état désiré de 3 réplicas.

## Relevé de l'observation

  Élément                             Résultat
  ----------------------------------- ----------
  Nom du Pod supprimé                 nginx-app-594c6dfcf4-g5qbw
  Nom du Pod créé en remplacement     nginx-app-594c6dfcf4-kbsd7
  Nombre de Pods après remplacement   3

------------------------------------------------------------------------

# Partie 5 -- Déploiement avec des fichiers YAML

Après avoir créé `deployment.yaml` et `service.yaml`, puis appliqué les
fichiers avec `kubectl apply` :

### 1. Pourquoi le nombre de Pods est-il passé à quatre après la modification de `replicas: 2` en `replicas: 4` ?

**Réponse :** Parce que nous avons modifié le champ replicas de 2 à 4 dans le fichier deployment.yaml. La commande kubectl apply a détecté ce changement et a mis à jour l'état du cluster pour correspondre à la nouvelle configuration déclarative, en créant automatiquement deux Pods supplémentaires.

### 2. Quel est l'intérêt de `kubectl apply` ?

**Réponse :** Il permet une gestion déclarative des ressources (Infrastructure as Code). Les fichiers YAML peuvent être versionnés  et réutilisés. Kubernetes compare l'état actuel avec le fichier et applique uniquement les modifications nécessaires sans recréer la ressource de zéro.

### 3. Quelle différence peut-on faire entre `kubectl create` et `kubectl apply` ?

**Réponse :** kubectl create est impératif : il tente de créer la ressource une seule fois. Si la ressource existe déjà, la commande échoue avec une erreur.
kubectl apply est déclaratif : il crée la ressource si elle n'existe pas, ou la met à jour de manière incrémentale si elle existe déjà, en appliquant les changements du fichier YAML.

### 4. Pourquoi les labels du template doivent-ils correspondre au selector ?

**Réponse :** Le champ selector indique au Deployment quels Pods il est responsable de gérer. Les labels définis dans le template sont apposés sur les Pods créés. S'ils ne correspondent pas exactement, le Deployment ne pourra pas identifier les Pods qu'il vient de créer, ce qui empêchera le ReplicaSet de les gérer (mise à l'échelle, auto-réparation) et provoquera une erreur de validation.


## Analyse des fichiers YAML

Complétez le tableau suivant.

  Champ YAML        Rôle / signification
  ----------------- ----------------------
  `apiVersion`      apps/v1
  `kind`           Deployment
  `metadata`        name: nginx-yaml
  `spec`            Bloc contenant replicas, selector, template
  `replicas`        4
  `selector`        matchLabels: app: nginx-yaml
  `template`        Bloc contenant metadata et spec avec containers
  `containers`      Liste avec - name: nginx
  `image`           nginx:latest
  `containerPort`   80

------------------------------------------------------------------------

# Exercices d'application

## Exercice 1 -- Modifier le déploiement

| Vérification                              | Résultat observé |
| ----------------------------------------- | ------------------ |
| Nombre de réplicas demandé (`replicas`)   | 5 |
| Nombre de Pods obtenu                     | 5 Pods en statut `Running` (pour le déploiement `nginx-yaml`) |
| Adresses IP des Pods                      | `10.244.0.8`, `10.244.0.9`, `10.244.0.10`, `10.244.0.11`, `10.244.0.12` |
| Nom du Pod supprimé                       | `nginx-yaml-64c748bc84-7vfjx` |
| Nom du Pod recréé                         | `nginx-yaml-64c748bc84-wd9m6` |

**Comment avez-vous vérifié le remplacement du Pod ?**

Réponse : J'ai exécuté `kubectl get pods` avant et après la suppression. Après avoir lancé `kubectl delete pod nginx-yaml-64c748bc84-7vfjx`, j'ai relancé `kubectl get pods` et j'ai constaté que le Pod supprimé avait été immédiatement remplacé par un nouveau Pod nommé `nginx-yaml-64c748bc84-wd9m6` (avec un âge de seulement 23 secondes), tout en maintenant le nombre total de Pods à 5. Cela confirme le mécanisme d'auto-réparation du ReplicaSet.

## Exercice 2 -- Modifier le port du Service

| Vérification                                         | Résultat observé |
| ---------------------------------------------------- | ------------------ |
| Ancien NodePort                                      | 30080 |
| Nouveau NodePort                                     | 30081 |
| Accès à Nginx après modification (réussi / échoué)   | Réussi |

**Décrivez brièvement le résultat obtenu :**

Après avoir modifié le champ `nodePort` de `30080` à `30081` dans le fichier `service.yaml` et appliqué la modification avec `kubectl apply`, la commande `kubectl get services` a confirmé que le service `nginx-yaml-service` écoutait désormais sur le port `80:30081/TCP`. La commande `minikube service nginx-yaml-service` a ouvert le navigateur sur l'URL `http://192.168.49.2:30081` (et via le tunnel `http://127.0.0.1:58393`), affichant correctement la page "Welcome to nginx!". La modification est donc effective et fonctionnelle.

## Exercice 3 -- Questions de compréhension

### 1. Un Pod est-il équivalent à un conteneur Docker ?
**Réponse :** Non. Un Pod est l'unité atomique de déploiement dans Kubernetes. C'est une enveloppe logique qui peut contenir un ou plusieurs conteneurs Docker partageant le même espace de noms réseau (même adresse IP) et le même stockage. Le conteneur est l'unité d'exécution, tandis que le Pod est l'unité de gestion.

### 2. Peut-on avoir plusieurs conteneurs dans un même Pod ?
**Réponse :** Oui. C'est une fonctionnalité courante (par exemple, le pattern "sidecar"), où un conteneur principal exécute l'application et un conteneur secondaire gère des tâches annexes comme la collecte de logs ou le proxy, les deux partageant les ressources du Pod.

### 3. Quelle est la différence entre Deployment et ReplicaSet ?
**Réponse :** Le **ReplicaSet** est un contrôleur de bas niveau qui garantit qu'un nombre spécifié de Pods identiques est toujours en cours d'exécution. Le **Deployment** est une abstraction de plus haut niveau qui gère les ReplicaSets. Il ajoute des fonctionnalités essentielles comme les mises à jour progressives (rolling updates) et les retours en arrière (rollbacks).

### 4. Que se passe-t-il lorsqu'un Pod géré par un Deployment est supprimé manuellement ?
**Réponse :** Le ReplicaSet associé détecte immédiatement que le nombre de Pods actifs est inférieur au nombre désiré (`replicas`). Il ordonne alors automatiquement la création d'un nouveau Pod pour remplacer celui qui a été supprimé, assurant ainsi l'auto-réparation (self-healing) du système.

### 5. Quel est le rôle d'un Service ?
**Réponse :** Un Service fournit un point d'accès réseau stable et permanent (adresse IP fixe et nom DNS) vers un ensemble de Pods dynamiques. Il agit comme un équilibreur de charge interne, découplant l'accès à l'application des adresses IP éphémères des Pods individuels.

### 6. Pourquoi utiliser un fichier YAML plutôt que plusieurs commandes ?
**Réponse :** Les fichiers YAML permettent une gestion **déclarative** et **versionnable** de l'infrastructure (Infrastructure as Code). Cela garantit la reproductibilité, permet de suivre l'historique des modifications via Git, facilite le partage en équipe, et rend les déploiements idempotents avec `kubectl apply`.

### 7. Un Deployment demande cinq réplicas, mais seulement trois Pods fonctionnent. Que va essayer de faire Kubernetes ?
**Réponse :** Le contrôleur (ReplicaSet) va détecter l'écart entre l'état souhaité (5) et l'état actuel (3). Il va automatiquement tenter de créer deux nouveaux Pods pour combler ce manque. Si les Pods échouent à démarrer (ex: image introuvable), Kubernetes continuera d'essayer indéfiniment et enregistrera des événements d'erreur visibles via `kubectl describe deployment`.

---

# Bilan du TP

## 1. Difficultés rencontrées
**Réponse :**
- **Installation des outils :** La commande `winget` n'était pas reconnue sur mon système Windows 11. De plus, le téléchargement de Minikube via `Invoke-WebRequest` a été bloqué (erreur de connexion abandonnée), probablement par l'antivirus ou le pare-feu.
- **Démarrage du cluster :** Après l'installation manuelle, la commande `docker ps` retournait systématiquement une erreur `500 Internal Server Error` sur le pipe `dockerDesktopLinuxEngine`, empêchant Minikube de démarrer (`PROVIDER_DOCKER_NOT_RUNNING`).
- **Interface Docker :** La nouvelle interface de Docker Desktop rendait l'accès aux options de dépannage moins évident.

## 2. Solutions adoptées
**Réponse :**
- **Pour les outils :** Téléchargement manuel des exécutables `kubectl.exe` et `minikube.exe` via le navigateur web, placés directement dans le dossier utilisateur (`C:\Users\fghjklmù\`).
- **Pour l'erreur Docker 500 :** 
  1. Exécution de `wsl --shutdown` pour arrêter proprement le sous-système Linux.
  2. Passage à l'ancienne interface de Docker Desktop via le lien "Go to classic Settings".
  3. Accès à l'onglet **Troubleshoot** via les trois petits points `⋮` en bas à gauche.
  4. Utilisation de l'option **Restart Docker Desktop** (et au besoin "Clean up data"), ce qui a rétabli le fonctionnement normal du moteur.
- **Pour les modifications YAML :** Utilisation de la commande PowerShell `(Get-Content ...) -replace ... | Set-Content` pour modifier les fichiers rapidement sans ouvrir d'éditeur graphique.

## 3. Conclusion
**Réponse :**
Ce TP m'a permis de maîtriser les concepts fondamentaux de l'orchestration de conteneurs avec Kubernetes. J'ai compris la distinction entre Docker (gestion unitaire) et Kubernetes (gestion de cluster), ainsi que les rôles complémentaires des Pods, Deployments, ReplicaSets et Services. J'ai pu observer concrètement les mécanismes puissants de mise à l'échelle (scaling) et d'auto-réparation (self-healing). Enfin, la transition des commandes impératives vers la gestion déclarative avec des fichiers YAML m'a initié aux bonnes pratiques de l'Infrastructure as Code, essentielles dans les environnements DevOps modernes. Malgré les défis techniques liés à l'environnement Windows, j'ai réussi à mener à bien toutes les étapes du déploiement.
## 4. Les captures 
<img width="839" height="304" alt="01-cluster" src="https://github.com/user-attachments/assets/9468f187-b7c8-4f10-a3ba-53f13c4d8eb2" />
<img width="613" height="415" alt="02-deployment" src="https://github.com/user-attachments/assets/4c1104c9-24a7-485b-834a-1886380ce62a" />
<img width="959" height="352" alt="03-nginx png" src="https://github.com/user-attachments/assets/5b985968-0e8e-4425-9b9c-d744caba2bec" />
<img width="917" height="105" alt="04-scaling" src="https://github.com/user-attachments/assets/920e96da-ca7c-488c-b73e-bc7a064eb45c" />
<img width="496" height="107" alt="05-auto-reparation" src="https://github.com/user-attachments/assets/db8d7eb3-692a-4d81-b00d-50429a66a88b" />




