---
title: PyQGIS PDF Batch Exporter
description: Script d'automatisation pour générer des PDF de cartes depuis QGIS Atlas en batch.
image: ""
tags:
  - Python
  - PyQGIS
  - Automatisation
status: terminé
date: "2025-02"
link: https://github.com/darcman0
---

# PyQGIS PDF Batch Exporter

Script Python pour générer automatiquement des PDF de cartes depuis QGIS Atlas.

## Contexte

Développé lors d'un projet de cartographie pédologique couvrant 78 parcelles sur 3 régions du Sénégal. Générer 78 PDF manuellement était impossible — ce script automatise l'ensemble du processus.

## Fonctionnalités

- Export batch de toutes les pages d'un Atlas QGIS
- Nommage automatique par attribut de la couche de couverture
- Résolution configurable (300 DPI par défaut)
- Log CSV des exports réussis et échoués

## Utilisation

```python
from qgis.core import QgsProject, QgsLayoutExporter
import os

project = QgsProject.instance()
layout = project.layoutManager().layoutByName("Ma_Mise_en_Page")
atlas = layout.atlas()
atlas.setEnabled(True)

exporter = QgsLayoutExporter(layout)
settings = QgsLayoutExporter.PdfExportSettings()
settings.dpi = 300

atlas.beginRender()
atlas.first()
while True:
    feature = atlas.currentFeature()
    filename = f"output_{feature['id_parcelle']}.pdf"
    exporter.exportToPdf(filename, settings)
    if not atlas.next():
        break
atlas.endRender()
```

---

[Voir sur GitHub :fontawesome-brands-github:](https://github.com/darcman0){ .md-button .md-button--primary }
