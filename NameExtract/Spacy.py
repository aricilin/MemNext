import spacy
from spacy import displacy
import sys
from spacy.lang.fr import French
import webbrowser
from spacy.tokens import Doc



# check arg number
if (len(sys.argv) != 2):
    print("utilisation : NameExtractSpacy.py texte_source")
    exit()

# load the pre-trained languages model

# nlp=spacy.load('fr_core_news_sm')# fr rapide extraction nom echec
# nlp=spacy.load('fr_dep_news_trf') # fr lent extraction nom echec

# nlp = spacy.load("en_core_web_trf") #eng lent résultat bon
# nlp = spacy.load('en_core_web_sm') # eng rapide résultat mauvais

# nlp = spacy.load("fr_dep_news_trf")
config = spacy.Config().from_disk("../ModelTraining/config.cfg")
nlp = French.from_config(config)
nlp.from_disk("../ModelTraining/output/model-best")
# define some text to analyze
text = open(sys.argv[1], "r", encoding="utf-8")

filepath = sys.argv[1]
filename = filepath.split('/')[len(filepath.split('/'))-1]
foutput = f"output/{filename}"

tuplelist = []
outputlist=[]
sentences = list(filter(lambda x : x != '', text.read().split('\n\n')))


listdoc=[]
for sentence in sentences:
    doc = nlp(sentence)
    for ent in doc.ents:
        tuple = (ent.start_char, ent.end_char, ent.label_)
        tuplelist.append(tuple)
    listdoc.append(doc)
    outputlist.append((sentence,tuplelist))
    tuplelist=[]

fulldoc= Doc.from_docs(listdoc)

with open(foutput, "w", encoding="utf-8") as f:
    f.write(str(outputlist))

try :#save in training seedmarker
    foutput = f"../SeedMarker/training/extracted/{filename}"
    with open(foutput, "w", encoding="utf-8") as f:
        f.write(str(outputlist))
except FileNotFoundError:
    exit


# seeds colors option
colors = {"0": "#F3F4ED", "1": "#F28482", "2": "#96BB7C", "3": "#76b5c5", "4": "#abdbe3",
          "5": "#D6EFC7", "6": "#F5CAC3", "7": "#7D1F35", "8": "#158467", "9": "#22577A"}
options = {"colors": colors}

# auto opening of web browser
url = "http://localhost:5000/"
webbrowser.open(url)

server = displacy.serve(fulldoc, style="ent", options=options)
