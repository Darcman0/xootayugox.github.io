---
date: 
  created: 2025-04-10
authors:
  - darc
categories:
  - Terrain

description: Retour d'expérience sur la cartographie de 2000 hectares de reboisements de mangrove pour WeForest dans le Sine-Saloum et la Casamance. 
---

# Cartographier 2 000 ha de mangroves pour WeForest : retour de terrain

Entre juillet 2025 et janvier 2026, j'ai participé à la cartographie aérienne de 2 000 hectares de reboisements de mangrove dans les îles du Sine-Saloum et en Casamance pour le compte de WeForest, via Earth Géomatique. 300 sites, plusieurs types de drones, des conditions de terrain extrêmes. Voici ce que j'en retiens.



<!-- more -->

---

## Le projet en chiffres

|Dénomination | Description| 
|------|------|
| Surface totale | 2 000 ha |
| Nombre de sites | 300 |
| Résolution orthophoto | 2 cm |
| Drones utilisés | DJI Air 2s, Mavic 3 Entreprise, Mavic 3 Mini Pro |
| Outil de suivi terrain | QField |
| Logiciel de traitement | Agisoft Metashape Professional |
| Gain de temps traitement | −20% grâce à l'automatisation |

---

## Les défis du terrain

### Accessibilité des sites

Le Sine-Saloum est un archipel de bolongs, de chenaux et de mangroves denses. Certains sites ne sont accessibles qu'en pirogue, avec du matériel drone à protéger de l'humidité et des éclaboussures.

**Solution :** Housses étanches pour les batteries et les télécommandes. Vols planifiés au plus tôt le matin pour éviter les vents de mer de l'après-midi.


### Couverture nuageuse

En saison des pluies, la couverture nuageuse peut invalider des orthophotos entières — les ombres créent des discontinuités radiométriques inutilisables pour la détection de changement.

**Solution :** Planification des vols par fenêtres météo (application Windy + observation locale). Re-vol systématique des zones affectées le jour suivant.

### Autonomie batterie sur zones étendues

Un site de 10–15 ha nécessite 2 à 3 batteries consécutives. La gestion des rotations de batteries en terrain isolé, sans accès à l'électricité, est un défi logistique réel.

**Solution :** Panneau solaire portable 100W + banque d'énergie 40 000 mAh pour recharge partielle en journée. Chargeur voiture branché sur le moteur de la pirogue.

---

## L'organisation des 300 sites avec QField

QField a été central dans la gestion de la mission. Voici notre workflow :

1. **Préparation dans QGIS** : création d'une couche de points pour les 300 sites, avec attributs (ID site, surface estimée, statut, date prévue, commentaires)
2. **Synchronisation sur QField** : chaque télépilote avait sa zone de sites assignée sur sa tablette
3. **Sur le terrain** : remplissage du statut (volé / à re-voler / problème technique), ajout de photos géolocalisées
4. **Synchronisation en fin de journée** : mise à jour de la base centrale via QFieldCloud

---

## Le traitement dans Metashape

Pour gagner du temps sur 300 lots d'images, j'ai mis en place un workflow semi-automatisé avec les scripts Python de Metashape :

```python
import Metashape
import os

doc = Metashape.app.document
chunk = doc.chunk

# Alignement des photos avec paramètres optimisés pour mangrove
chunk.matchPhotos(
    accuracy=Metashape.HighAccuracy,
    generic_preselection=True,
    reference_preselection=True
)
chunk.alignCameras()

# Nuage de points dense
chunk.buildDepthMaps(quality=Metashape.MediumQuality)
chunk.buildDenseCloud()

# Orthophoto 2 cm
chunk.buildOrthomosaic(
    surface=Metashape.ElevationData,
    resolution=0.02  # 2 cm
)

# Export automatique
output_path = "D:/WeForest/outputs/"
chunk.exportOrthomosaic(
    output_path + chunk.label + "_ortho.tif",
    image_format=Metashape.ImageFormatTIFF,
    resolution=0.02
)

print(f"Traitement terminé : {chunk.label}")
```

Ce script, appliqué via le batch processing de Metashape sur des dossiers organisés par site, a réduit le temps de traitement moyen de **20%** en éliminant les étapes manuelles répétitives.

---

## Ce que j'ai appris

!!! success "Ce qui a bien fonctionné "
    - QField pour le suivi en temps réel des 300 sites : indispensable
    - Les vols tôt le matin (6h–9h) : lumière rasante, vent faible, mangroves encore humides donc contraste maximal
    - Recouvrement frontal/latéral à 80%/70% : moins de trous dans les zones denses

!!! warning "Ce que je referais différemment "
    - Prévoir des GCP même sur des zones plates : la précision verticale s'en ressent
    - Documenter les sites problématiques dès le terrain plutôt qu'en post-traitement
    - Utiliser systématiquement le Mavic 3 Entreprise (RTK intégré) plutôt que l'Air 2s pour les zones critiques

---

*Mission réalisée avec Earth Géomatique pour WeForest, Sénégal, 2025.*  