# déroulement

- téléchargement du fichier config de base
- update du fichier config
- preprocess des données
- entrainement du model via le jeu d'entrainement
- évaluation du model via le jeu de test

# Remplir le fichier config depuis la base

`python -m spacy init fill-config base_config.cfg config.cfg`

# pour préprocess les données 

utilisation du fichier preprocess.py


# Pour entrainer 

donner le chemin de deux fichiers préprocessés un entrainement et un évaluation 

`python -m spacy train config.cfg  --output output/   --paths.train ./train.spacy --paths.dev ./test.spacy`


# Pour evaluer 

ici le jeu de test est :  _./test.spacy_

`python -m spacy evaluate output/model-best ./test.spacy  --output output/metrics.json`



