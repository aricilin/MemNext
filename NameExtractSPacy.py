import spacy
import sys

#check arg number
if (len(sys.argv) != 2):
    print("utilisation : NameExtractSpacy.py texte_source")
    exit()

# load the pre-trained languages model

#nlp=spacy.load('fr_core_news_sm')# fr rapide extraction nom echec
#nlp=spacy.load('fr_dep_news_trf') # fr lent extraction nom echec

#nlp = spacy.load("en_core_web_trf") #eng lent résultat bon
#nlp = spacy.load('en_core_web_sm') # eng rapide résultat mauvais
nlp = spacy.load("fr_core_news_sm")
#nlp = spacy.load("fr_dep_news_trf")


# define some text to analyze
text= open(sys.argv[1],"r")

# use spaCy's NER module to identify named entities in the text
doc = nlp(text.read())

#if an entity is not in nameList and its label is 'PERSON' print it
nameList =[]

for entity in doc.ents:
    if entity.text not in nameList:
        print(entity.text, entity.label_)
        nameList.append(entity.text)
