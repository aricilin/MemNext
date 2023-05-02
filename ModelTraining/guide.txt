Remplir le fichier config depuis la base

python -m spacy init fill-config base_config.cfg config.cfg

Pour entrainer chemin train et chemin test (ici le même)

python -m spacy train config.cfg  --output output/   --paths.train ./train.spacy --paths.dev ./train.spacy


Pour evaluer 

python -m spacy evaluate output/model-best ./train.spacy  --output output/metrics.json



