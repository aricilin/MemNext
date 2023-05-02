# déroulement

- téléchargement du fichier config de base
- update du fichier config
- entrainement du model via le jeu d'entrainement
- évaluation du model via le jeu de test

# Remplir le fichier config depuis la base

`python -m spacy init fill-config base_config.cfg config.cfg`

# Pour entrainer chemin train et chemin test (ici le même)

`python -m spacy train config.cfg  --output output/   --paths.train ./train.spacy --paths.dev ./train.spacy`


# Pour evaluer 

ici le jeu de test est le jeu d'entrainement  _./train.spacy_

`python -m spacy evaluate output/model-best ./train.spacy  --output output/metrics.json`



