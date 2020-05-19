# Extraction JSON de la Foire Aux Questions à destination des entreprises dans le contexte COVID-19

## Objet
Ce dépot contient les articles de la FAQ https://info-entreprises-covid19.economie.gouv.fr/ ainsi que le script servant à leur extraction.

## Format des données
Le fichier data.json se présente sous la forme d'une liste d'objets telle que celle-ci:
```json
[
  {
    "titre": "Article d'exemple pour la documentation",
    "content": [
      "ceci est la première page de l'article", 
      "<b>ici la deuxième</b>", 
      "<div>ces articles intègrent un peu de mise en forme HTML</div>"
      ],
    "chemin": [
      "Dossier à visiter dans la FAQ",
      "pour rejoindre l'article"]
  }
]
```

## License accordée pour les articles
Les données contenues dans le fichier data.json sont soumises à la Licence Ouvert v2.0
https://www.etalab.gouv.fr/wp-content/uploads/2017/04/ETALAB-Licence-Ouverte-v2.0.pdf

## License accordée pour le script stonly2json.py
Copyright © 05/19/2020, Christophe Ninucci

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

The Software is provided “as is”, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders X be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the Software.
Except as contained in this notice, the name of Christophe Ninucci shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from Christophe Ninucci.