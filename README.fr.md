# Projet Dessin Turtle pour Calculatrice NumWorks

Ce projet vous permet de dessiner des images sur la calculatrice NumWorks en utilisant la bibliothèque graphique Turtle. Le projet consiste à convertir une image en une séquence de commandes Turtle basées sur des correspondances de couleurs.

## Prérequis

- Python 3.x
- Calculatrice NumWorks
- Bibliothèque PIL (Pillow)
- Bibliothèque graphique Turtle

## Configuration

1. **Cloner le Dépôt :**

   ```bash
   git clone https://github.com/votre-nom-utilisateur/numworks-turtle-art.git
   cd numworks-turtle-art
   ```

2. **Installer les Dépendances :**

   Assurez-vous d'avoir Python 3.x installé. Ensuite, installez les bibliothèques requises avec pip :

   ```bash
   pip install Pillow
   ```

   La bibliothèque `turtle` est généralement incluse avec Python par défaut.

## Utilisation

### 1. Préparez Votre Image

- Placez votre image désirée (par exemple `phryge.png`) dans le répertoire du projet.

### 2. Générer les Lettres de Couleur

Exécutez le script suivant pour générer la correspondance des couleurs (`color_letters.txt`) à partir de votre image :

```bash
python exportstring.py
```

Ce script va créer une correspondance des couleurs avec des lettres et les sauvegarder dans `color_letters.txt`.

### 3. Dessinez sur la Calculatrice NumWorks

1. Copiez le contenu de `color_letters.txt` et les couleurs dans le tableau dans `code_numworks.py` sur votre calculatrice.
2. Exportez cela sur la calculatrice à l'aide de l'outil en ligne Numworks.

3. Si vous voulez dessiner cela sur l'ordinateur, utilisez le fichier `tortue.py` et exécutez-le avec Python. (assurez-vous de copier les couleurs dans le tableau du fichier Python d'abord)

### 4. Exécutez le Dessin Turtle

Sur votre calculatrice NumWorks, exécutez le script `turtle_drawing.py`. Ce script va interpréter les lettres de couleur à partir de `color_letters.txt` et dessiner l'image correspondante en utilisant la bibliothèque graphique Turtle.

## Remarques Additionnelles

- Assurez-vous que l'image que vous utilisez (`phryge.png` dans l'exemple) est dimensionnée de manière appropriée pour les dimensions de l'écran de la calculatrice NumWorks (`320x240`).