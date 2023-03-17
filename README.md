# Projet MemNext

Outil d'extraction de graines d'information à partir de données textuelles.


## Installation

Il faut au préalable avoir installé la librairie spaCy :

```
pip install -U pip setuptools wheel
pip install -U spacy
```

Puis installer les modèles souhaités, par exemple pour du français :

```
python -m spacy download fr_core_news_lg
```


## Usage

Lancer le script `main.py` avec pour arguments le texte d'entrée et le fichier de sortie dans lequel écrire les graines :

```
python main.py texte_entree.txt fichier_graines.(json|csv)
```

## Documentation du projet

Voir le wiki :[https://gitlab.com/mem-next/projet-memnext/-/wikis/home](https://gitlab.com/mem-next/projet-memnext/-/wikis/home)

## Documentation technique du code

[https://mem-next.gitlab.io/projet-memnext/](https://mem-next.gitlab.io/projet-memnext/)
