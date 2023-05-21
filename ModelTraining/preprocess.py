import spacy
from spacy.tokens import DocBin
import ast
import os,glob,sys

nlp = spacy.blank("fr")

""" 
with open("entrainement.txt", 'r', encoding="utf-8") as file:
    # Read the contents of the file
    contents = file.read()
    # Split the contents by the delimiter (e.g., comma)
    training_data = ast.literal_eval(contents)
# Now, my_list contains the items from the text file as a list
 """
training_data=[]
os.chdir("input")
for file in glob.glob("*.txt"):
    with open(file,'r',encoding="utf-8")as f: 
        if len(training_data )==0:
            training_data = ast.literal_eval(f.read())
        else :
            training_data+=ast.literal_eval(f.read())
# the DocBin will store the example documents
db = DocBin()
pt = 0
for text, annotations in training_data:
    doc = nlp(text)
    ents = []
    for start, end, label in annotations:
        if label not in ["8","2","9"]:
            try:
                span = doc.char_span(start, end, label=label)
                ents.append(span)
                doc.ents = ents
            except TypeError:  # error  ex tag cut a word
                print(f"({start}, {end}, '{label}')")
                print("supprimez ou corrigez le tag (très souvent le tag coupe un mot)")
                break
    db.add(doc)
db.to_disk("../train.spacy")


