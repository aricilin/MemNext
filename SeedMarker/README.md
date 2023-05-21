 
# Guide d'utilisation

- prérequis [python 3.10](https://www.python.org/downloads/release/python-31011/) 
- installation des librairies nécessaires `pip install -r libraries_seedmarker.txt`
- execution du programme `python SeedMarker.py`
- sélection du fichier à traiter (txt, docx, pdf, odt, doc)(dans le cas d'un fichier non-txt une version txt sera créée dans le dossier temp)
- par question de lisibilité le texte est découpé en phrases/blocs on peut changer de blocs via les boutons `suivant` et `précédent`
- sélection d'une graine dans le texte via surlignage ou même simple clic dans le cas d'un mot
- enregistrement de la graine en cliquant sur le label associé

# Usage

Dans le dossier `training` les graines sont stockées en tuple (position de départ, position de fin, label).  
Ces graines sont associées à leur phrase d'origine dans le fichier commé comme le fichier source.  
Ainsi le fichier sera de la forme d'une liste de couple (phrase , liste de tuples(début,fin,label)).  
Dans le dossier `temp` sont stockés les fichiers .txt extraits des sources de type autre. 
