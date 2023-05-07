import spacy
from spacy import displacy
import sys
from spacy.lang.fr import  French
#check arg number
if (len(sys.argv) != 2):
    print("utilisation : NameExtractSpacy.py texte_source")
    exit()

# load the pre-trained languages model

#nlp=spacy.load('fr_core_news_sm')# fr rapide extraction nom echec
# nlp=spacy.load('fr_dep_news_trf') # fr lent extraction nom echec

# nlp = spacy.load("en_core_web_trf") #eng lent résultat bon
#nlp = spacy.load('en_core_web_sm') # eng rapide résultat mauvais

#nlp = spacy.load("fr_dep_news_trf")
config = spacy.Config().from_disk("../ModelTraining/config.cfg")
nlp = French.from_config(config) 
nlp.from_disk("../ModelTraining/output/model-best")
# define some text to analyze
text= open(sys.argv[1],"r",encoding="utf-8")

# use spaCy's NER module to identify named entities in the text
doc = nlp(text.read())

#if an entity is not in nameList and its label is 'PERSON' print it
nameList =[]
nb=0

# for entity in doc.ents:
#     try:
#         if entity.text not in nameList:
#             print(entity.text, entity.label_)
#             nameList.append(entity.text)
#             nb+=1
#     except UnicodeEncodeError:
#         continue
# print (nb, "lignes")


colors = {"0": "#F3F4ED", "1": "#F28482", "2": "#96BB7C", "3": "#76b5c5", "4": "#abdbe3", "5": "#D6EFC7", "6": "#F5CAC3", "7": "#7D1F35", "8": "#158467", "9": "#22577A"}
options = { "colors": colors}
displacy.serve(doc, style="ent", options=options)