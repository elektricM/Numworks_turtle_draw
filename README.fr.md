# Dessin Turtle pour la Calculatrice NumWorks
- [English](README.md)
- [Français](README.fr.md)

Ce projet vous permet de dessiner des images sur la calculatrice NumWorks en utilisant la bibliothèque graphique Turtle. Le projet consiste à convertir une image en une séquence de commandes Turtle basées sur des correspondances de couleurs.

## Utilisation

### Option 1 : Utiliser l'Exécutable GUI

1. **Télécharger l'Exécutable GUI** :

   Téléchargez la dernière version depuis la [page des releases](https://github.com/elektricM/Numworks_turtle_draw/releases).

2. **Exécuter l'Exécutable** :

   Exécutez l'exécutable et suivez les instructions dans l'interface graphique pour sélectionner votre image et générer le script Python pour la calculatrice NumWorks.

### Option 2 : Exécution Manuelle avec Python

## Prérequis

- Python 3.x
- Calculatrice NumWorks
- Bibliothèque PIL (Pillow)
- Bibliothèque graphique Turtle
- Tkinter (pour la version GUI)
- pyperclip (pour la fonctionnalité du presse-papiers)

## Installation

1. **Cloner le Dépôt** :

   ```bash
   git clone https://github.com/elektricM/Numworks_turtle_draw.git
   cd Numworks-turtle-draw
   ```

2. **Installer les Dépendances** :

   Assurez-vous d'avoir Python 3.x installé. Ensuite, installez les bibliothèques requises en utilisant pip :

   ```bash
   pip install pillow
   pip install pyperclip
   pip install turtle
   pip install tk
   ```

## Utilisation

### Option 1 : Utiliser le Script GUI

- Utilisez le script `automatic_gui.py` pour générer la correspondance des couleurs et le script Python pour la calculatrice NumWorks en utilisant l'interface graphique.

### Option 2 : Exécution Manuelle avec Python

### 1. Préparer Votre Image

- Placez l'image désirée (par exemple, `example.png`) dans le répertoire du projet.

### 2. Générer les Lettres de Couleur

Exécutez le script suivant pour générer la correspondance des couleurs (`color_letters.txt`) à partir de votre image :

```bash
python exportstring.py
```

Ce script créera une correspondance des couleurs en lettres et les enregistrera dans `color_letters.txt`.

### 3. Dessiner sur la Calculatrice NumWorks

1. Copiez le contenu de `color_letters.txt` et les couleurs dans le tableau vers `code_numworks.py` sur votre calculatrice.
2. Exportez cela sur la calculatrice en utilisant l'outil en ligne de NumWorks.

3. Si vous souhaitez dessiner cela sur le PC, utilisez le fichier `tortue.py` et exécutez-le avec Python. (Assurez-vous de copier les couleurs dans le tableau dans le fichier Python d'abord)

### 4. Exécuter le Dessin Turtle

Sur votre calculatrice NumWorks, exécutez le script `turtle_drawing.py`. Ce script interprétera les lettres de couleur de `color_letters.txt` et dessinera l'image correspondante en utilisant les graphiques Turtle.

## Notes Additionnelles

- Assurez-vous que l'image que vous utilisez (`example.png` dans l'exemple) est de la taille appropriée pour les dimensions de l'écran de la calculatrice NumWorks (`320x240`) et ne contient pas trop de couleurs.

---