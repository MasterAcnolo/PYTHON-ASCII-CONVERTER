# Convertisseur d'Image en ASCII

Ce projet est une application web qui permet de convertir des images en art ASCII. Il utilise Flask pour le backend et PIL (Pillow) pour la manipulation des images.


## Fichiers principaux

- `converter.py`: Script Python pour convertir une image en art ASCII via la ligne de commande.
- `Site/site.py`: Application Flask pour convertir des images en art ASCII via une interface web.
- `Site/templates/index.html`: Template HTML pour l'interface utilisateur de l'application web.

## Installation

1. Clonez le dépôt:
    ```sh
    git clone https://github.com/MasterAcnolo/PYTHON-ASCII-CONVERTER
    ```

2. Installez les dépendances:
    ```sh
    pip install flask pillow
    ```

## Utilisation

### Ligne de commande

Pour convertir une image en ASCII via la ligne de commande, exécutez `converter.py`:
```sh
python converter.py

```

Entrez le chemin de l'image lorsque demandé.(Chemin Absolu de préférence, sauf si éléments dans le dossier racine)

### Application Web
Pour lancer l'application web, exécutez `site.py`:

```python
python site.py
```

Ouvrez votre navigateur et allez à `http://127.0.0.1:5000` pour accéder à l'interface utilisateur.

### Fonctionnalités
1. Conversion d'image en ASCII avec différents jeux de caractères (classique, pixel, detailed).
2. Option pour générer de l'ASCII coloré.
3. Téléchargement du résultat en fichier .txt. <- A venir 

# Contribuer
Les contributions sont les bienvenues! Veuillez soumettre une pull request ou ouvrir une issue pour discuter des changements que vous souhaitez apporter.

# Licence

 Y'en a pas vraiment, faites vous plaisir ! 