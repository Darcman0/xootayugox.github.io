---
date: 
  created: 2025-05-19
authors:
  - darc
  - mDieng
categories:
  - Enquetes
  - Synchronisation
---

# Test 5


![](../assets/kobo_api_v1/article_presentation_img.jpg){.img-center}
---
Cela vous est-il déjà arrivé d’avoir la flemme de vous rendre sur le site de [Kobotoolbox](https://kc.kobotoolbox.org/) pour télécharger vos données issues de votre campagne de collecte?

Si oui, voici un **_tips_** qui vous fera gagner énormément de temps.

<!-- more -->

## API ?
Pour cela on utilisera la première version de l’API de Kobotoolbox. Parlons d’abord de ce que c’est une API. Une API (application programming interface ou « interface de programmation d'application ») est une interface logicielle qui permet de « connecter » un logiciel ou un service à un autre logiciel ou  service afin d'échanger des données et des fonctionnalités (il y’a certains lecteurs dès qu’ils ont vu **_programming_**, ils sont passés à autre chose 😆).

## Connexion au serveur de Kobotoolbox
Concrètement, on va connecter le serveur de _**Kobotoolbox**_ à un logiciel (ici Microsoft excel) pour recevoir de manière automatique les données collectées.

!!! warning "Il faut d’abord se connecter sur votre compte _**Kobotoolbox**_ et se rendre a l'addresse suivante :"
    https://kc.kobotoolbox.org/api/v1/data

Cet URL va nous permettre d’accéder à la fenêtre de programmation de l’API.

![alt](../assets/kobo_api_v1/fenetre_API.png)

Il faut maintenant faire clique gauche sur la flèche à droite de GET et sélectionner json

  ![](../assets/kobo_api_v1/API_json.png){.img-center}
 


Une nouvelle page s'ouvre, dans celle-ci vous aurez l’ensemble des formulaires que vous avez déployé

![](../assets/kobo_api_v1/formulaire_deploye.png){.img-center}

A ce niveau, moi j'ai trois formulaires déployés dont l’id est propre à chacun en plus il y a la description et le titre de chacun de ces formulaires mais aussi l’URL menant à chacun des formulaires.

!!! warning "Il faut copier l’URL du formulaire cible (dont on veut récupérer les données de manière automatique), ici moi je copie l’URL du projet : _**Test_api__V1**_"
    https://kc.kobotoolbox.org/api/v1/data/1964678?format=json

## Pont entre Excel et Kobotoolbox

- Ensuite ouvrir le logiciel Microsoft excel 

- Puis se rendre sur le menu data ou donnée ( en fonction de la langue du système)

- Cliquez sur From web ou à partir du web
  
![](../assets/kobo_api_v1/from_web_excel.png){.img-center}

!!! warning "Dans la nouvelle fenêtre qui s’ouvre, il faut collé l’URL qui a été auparavant copié à partir de la page de l’API." 
    Mais en écrivant à la place de **?format=json** : _**.XLSX**_ et cliquer sur OK

![](../assets/kobo_api_v1/from_web_config.png){.img-center}

Après cela une fenêtre permettant de voir les données de notre formulaire cible s’ouvre, faut sélectionner la feuille (avec les caractéres alphanumériques mélangés) et cliquer sur _LOAD_ 

![](../assets/kobo_api_v1/sheets_select.png)

!!! success "La magie devrait s'opérer 🎉"

![](../assets/kobo_api_v1/kobo_sync_RT.png)

Sinon, si un message d’erreur apparaît, il frauda juste se rendre sur votre compte Kobotoolbox et naviguer à partir du formulaire (dont vous voulez récupérer les données) vers **PARAMÈTRES** PUIS **Partage** et s’assurer que soit cochez les cases :

!!! warning "Bien cochez"
    !!! success "Cochez"
        N’importe qui peut afficher ce formulaire 
    
        N’importe qui peut afficher les soumissions de ce formulaire

![](../assets/kobo_api_v1/kobo_autorisation.png)

Essayez d'actualiser votre logiciel Excel à partir du menu Data ou Donnée et le tour devrait être joué. J’espère que vous y êtes parvenu. Sinon contactez moi, je serai ravie de vous aiguiller.