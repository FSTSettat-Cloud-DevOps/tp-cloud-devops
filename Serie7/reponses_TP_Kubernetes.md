# TP : Introduction à Kubernetes

## Déploiement, exposition et mise à l'échelle d'une application Web

**Université Hassan I -- Faculté des Sciences et Techniques de Settat**\
**Module :** Cloud Computing et DevOps\
**Enseignant :** Pr. Abdelfattah Abassi

------------------------------------------------------------------------

## Identification de l'étudiant(e)

-   **Nom :**
-   **Prénom :**
-   **Filière :**
-   **Groupe :**
-   **Identifiant GitHub :**
-   **Date du TP :**

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
<!-- Écrivez votre réponse ici. -->
```
### 2. Que représente un nœud (Node) ?

**Réponse :**

```{=html}
<!-- Écrivez votre réponse ici. -->
```
### 3. Quelle est la différence générale entre Docker et Kubernetes ?

**Réponse :**

```{=html}
<!-- Écrivez votre réponse ici. -->
```
### 4. Quel est le rôle de `kubectl` ?

**Réponse :**

```{=html}
<!-- Écrivez votre réponse ici. -->
```

------------------------------------------------------------------------

# Partie 1 -- Découverte du cluster

Commandes utilisées : `kubectl get nodes`,
`kubectl describe node minikube`, `kubectl get pods -A` et
`kubectl get namespaces`.

### 1. Combien de nœuds contient votre cluster ?

**Réponse :**

### 2. Quel est le statut du nœud ?

**Réponse :**

### 3. Relever trois Pods du namespace `kube-system`.

**Réponse :**

-   Pod 1 :
-   Pod 2 :
-   Pod 3 :

### 4. Quel est le rôle du namespace `kube-system` ?

**Réponse :**

------------------------------------------------------------------------

# Partie 2 -- Premier déploiement Nginx

Après avoir créé le Deployment `nginx-app` et exécuté les commandes
d'observation :

### 1. Combien de Pods ont été créés ?

**Réponse :**

### 2. Quel est le rôle du ReplicaSet ?

**Réponse :**

### 3. Le Deployment exécute-t-il directement le conteneur ?

**Réponse :**

### 4. Quelle est la différence entre un Pod et un conteneur Docker ?

**Réponse :**

## Observation d'un Pod

Après avoir exécuté `kubectl describe pod NOM_DU_POD` et
`kubectl logs NOM_DU_POD`, complétez le tableau.

  Information demandée   Résultat observé
  ---------------------- ------------------
  Nom du Pod             
  Statut du Pod          
  Image utilisée         

------------------------------------------------------------------------

# Partie 3 -- Exposer l'application avec un Service

Après avoir créé le Service avec
`kubectl expose deployment nginx-app --type=NodePort --port=80`, puis
exécuté `minikube service nginx-app` :

### 1. Pourquoi éviter d'utiliser directement l'adresse IP d'un Pod pour accéder à l'application ?

**Réponse :**

### 2. Quel est le rôle du Service ?

**Réponse :**

### 3. Quelle est la différence entre ClusterIP et NodePort ?

**Réponse :**

### 4. Quel port est utilisé par Nginx dans le conteneur ?

**Réponse :**

## Observation du Service

  Information demandée                    Résultat observé
  --------------------------------------- ------------------
  Nom du Service                          
  Type du Service                         
  Port du Service                         
  Port cible (`targetPort`), si affiché   
  Port NodePort, si affiché               

------------------------------------------------------------------------

# Partie 4 -- Scaling et auto-réparation

Après avoir exécuté `kubectl scale deployment nginx-app --replicas=3` :

### 1. Combien de Pods sont maintenant en fonctionnement ?

**Réponse :**

### 2. Pourquoi peut-on avoir besoin de plusieurs réplicas d'une application ?

**Réponse :**

## Test de l'auto-réparation

Après avoir supprimé un Pod avec `kubectl delete pod NOM_DU_POD`,
observez les Pods avec `kubectl get pods -w`.

### 3. Pourquoi Kubernetes a-t-il créé un nouveau Pod ?

**Réponse :**

### 4. Quel composant veille au nombre de Pods souhaité ?

**Réponse :**

### 5. Le nouveau Pod possède-t-il nécessairement le même nom que l'ancien ?

**Réponse :**

### 6. Que se passerait-il si deux Pods étaient supprimés ?

**Réponse :**

## Relevé de l'observation

  Élément                             Résultat
  ----------------------------------- ----------
  Nom du Pod supprimé                 
  Nom du Pod créé en remplacement     
  Nombre de Pods après remplacement   

------------------------------------------------------------------------

# Partie 5 -- Déploiement avec des fichiers YAML

Après avoir créé `deployment.yaml` et `service.yaml`, puis appliqué les
fichiers avec `kubectl apply` :

### 1. Pourquoi le nombre de Pods est-il passé à quatre après la modification de `replicas: 2` en `replicas: 4` ?

**Réponse :**

### 2. Quel est l'intérêt de `kubectl apply` ?

**Réponse :**

### 3. Quelle différence peut-on faire entre `kubectl create` et `kubectl apply` ?

**Réponse :**

### 4. Pourquoi les labels du template doivent-ils correspondre au selector ?

**Réponse :**

## Analyse des fichiers YAML

Complétez le tableau suivant.

  Champ YAML        Rôle / signification
  ----------------- ----------------------
  `apiVersion`      
  `kind`            
  `metadata`        
  `spec`            
  `replicas`        
  `selector`        
  `template`        
  `containers`      
  `image`           
  `containerPort`   

------------------------------------------------------------------------

# Exercices d'application

## Exercice 1 -- Modifier le déploiement

Effectuez les manipulations demandées dans le TP, puis consignez vos
observations.

  Vérification                              Résultat observé
  ----------------------------------------- ------------------
  Nombre de réplicas demandé (`replicas`)   
  Nombre de Pods obtenu                     
  Adresses IP des Pods                      
  Nom du Pod supprimé                       
  Nom du Pod recréé                         

**Comment avez-vous vérifié le remplacement du Pod ?**

Réponse :

## Exercice 2 -- Modifier le port du Service

Après avoir remplacé le NodePort `30080` par `30081`, appliqué la
modification et testé de nouveau l'accès à Nginx :

  Vérification                                         Résultat observé
  ---------------------------------------------------- ------------------
  Ancien NodePort                                      
  Nouveau NodePort                                     
  Accès à Nginx après modification (réussi / échoué)   

**Décrivez brièvement le résultat obtenu :**

## Exercice 3 -- Questions de compréhension

### 1. Un Pod est-il équivalent à un conteneur Docker ?

**Réponse :**

### 2. Peut-on avoir plusieurs conteneurs dans un même Pod ?

**Réponse :**

### 3. Quelle est la différence entre Deployment et ReplicaSet ?

**Réponse :**

### 4. Que se passe-t-il lorsqu'un Pod géré par un Deployment est supprimé manuellement ?

**Réponse :**

### 5. Quel est le rôle d'un Service ?

**Réponse :**

### 6. Pourquoi utiliser un fichier YAML plutôt que plusieurs commandes ?

**Réponse :**

### 7. Un Deployment demande cinq réplicas, mais seulement trois Pods fonctionnent. Que va essayer de faire Kubernetes ?

**Réponse :**

------------------------------------------------------------------------

# Bilan du TP

## 1. Difficultés rencontrées

Décrivez les difficultés rencontrées pendant le TP (installation,
démarrage du cluster, commandes, fichiers YAML, accès à Nginx, etc.).

**Réponse :**

## 2. Solutions adoptées

Indiquez les commandes, modifications ou démarches qui vous ont permis
de résoudre ces difficultés.

**Réponse :**

## 3. Conclusion

En quelques lignes, résumez les notions que vous avez apprises pendant
ce TP.

**Réponse :**

------------------------------------------------------------------------

# Liste de vérification avant le dépôt GitHub

-   [ ] Toutes les questions ont reçu une réponse.
-   [ ] Les résultats observés correspondent aux manipulations
    réellement effectuées.
-   [ ] Le fichier `deployment.yaml` est déposé.
-   [ ] Le fichier `service.yaml` est déposé.
-   [ ] La capture `preuves/01-cluster.png` est déposée.
-   [ ] La capture `preuves/02-deployment.png` est déposée.
-   [ ] La capture `preuves/03-nginx.png` est déposée.
-   [ ] La capture `preuves/04-scaling.png` est déposée.
-   [ ] La capture `preuves/05-auto-reparation.png` est déposée.
-   [ ] Le nom, le prénom, la filière, le groupe et l'identifiant GitHub
    sont renseignés.

**Important :** Les réponses doivent être personnelles et fondées sur
les résultats obtenus pendant le TP. Les captures d'écran doivent être
réalisées par l'étudiant ; elles ne remplacent ni les réponses ni les
fichiers YAML.
