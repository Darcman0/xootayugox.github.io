---
date: 
  created: 2025-05-01
authors:
  - darc
title: "Connexion API Kobotoolbox vers Excel"
categories:
  - Enquêtes
  - Synchronisation
description: "Guide technique pour automatiser la récupération de données Kobotoolbox vers Excel via l'API V1, éliminant les exports manuels répétitifs."
---

# Connexion de l'API V1 de Kobotoolbox avec Microsoft Excel

![Illustration](../assets/kobo_api_v1/article_presentation_img.jpg){.img-center}

### Contexte et mise en œuvre
On connaît tous la routine : se connecter à Kobo, exporter, nettoyer, puis importer dans Excel. C'est long, c'est pénible, et on finit toujours par travailler sur une version obsolète de la base. 

L'astuce ici, c'est d'utiliser l'API V1 de Kobotoolbox pour créer un pont direct entre le serveur et Excel.

**1. Récupérer l'URL API**
Connectez-vous à votre compte Kobo et allez ici : [https://kc.kobotoolbox.org/api/v1/data](https://kc.kobotoolbox.org/api/v1/data).

Une nouvelle page s'ouvre, dans celle-ci vous aurez l’ensemble des formulaires que vous avez déployé.

![Formulaires déployés](../assets/kobo_api_v1/formulaire_deploye.png){.img-center}

À ce niveau, moi j'ai trois formulaires déployés dont l’ID est propre à chacun. En plus, il y a la description et le titre de chacun de ces formulaires, mais aussi l’URL menant à chacun des formulaires.

!!! tip "Astuce de navigation"
    Ne lisez pas tout le code manuellement. Utilisez `Ctrl+F` (ou `Cmd+F` sur Mac) dans votre navigateur et tapez le nom de votre formulaire pour isoler immédiatement son bloc de données.

Cliquez sur la flèche à côté de **GET**, sélectionnez **JSON**, et repérez l'URL du projet cible dans le bloc correspondant :
`https://kc.kobotoolbox.org/api/v1/data/1964678?format=json`

![Fenetre API](../assets/kobo_api_v1/fenetre_API.png)

![Selection JSON](../assets/kobo_api_v1/API_json.png)

**2. Configuration dans Excel**

1. Ouvrez Excel, allez dans **Données** > **À partir du Web**.
2. Collez l'URL.

!!! danger "Le détail qui tue"
    Il faut impérativement remplacer le `?format=json` à la fin de l'URL par `.xlsx`. Si vous oubliez, Excel va chercher à lire du code JSON au lieu d'un tableau structuré, et ça ne fonctionnera pas.

![Configuration Web](../assets/kobo_api_v1/from_web_config.png)

Excel vous montre un aperçu. Sélectionnez la feuille, cliquez sur **Charger**.

!!! success "Chargement réussi"
    Si vous voyez vos données apparaître dans la feuille Excel, le pont est établi.

![Chargement des feuilles](../assets/kobo_api_v1/sheets_select.png)

**3. Optimisation et gestion des accès**

* **Nettoyage :** Utilisez **Power Query** (Données > Requêtes et connexions) pour virer les colonnes inutiles et typer vos dates/coordonnées.
* **Actualisation :** Dans les "Propriétés de la requête", cochez "Actualiser lors de l'ouverture".
* **Erreurs de connexion :** Si ça bloque, vérifiez les partages sur Kobo.

!!! warning "Le piège classique"
    Si Excel rejette la connexion, c'est presque toujours parce que le projet est en accès "Privé". Allez dans **Paramètres > Partage** sur Kobo et vérifiez que :
    - "N'importe qui peut afficher ce formulaire" est coché.
    - "N'importe qui peut afficher les soumissions" est coché.

![Autorisations Kobo](../assets/kobo_api_v1/kobo_autorisation.png)

### Résultats
Vos données sont liées au serveur Kobo. Plus besoin d'exporter à la main : retournez dans l'onglet **Données** d'Excel, cliquez sur **Actualiser tout**, et votre rapport se met à jour.

![Données chargées](../assets/kobo_api_v1/kobo_sync_RT.png)

### Pour aller plus loin
* [Documentation officielle de l'API Kobotoolbox](https://support.kobotoolbox.org/api.html)
* Si les données sont confidentielles, laissez le projet privé et configurez une "Basic Auth" dans Excel avec vos identifiants Kobo au lieu d'ouvrir le partage public.
