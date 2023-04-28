import spacy
from spacy.tokens import DocBin
import ast

nlp = spacy.blank("en") 


with open("sample1.txt", 'r') as file:
    # Read the contents of the file
    contents = file.read()
    # Split the contents by the delimiter (e.g., comma)
    training_data = ast.literal_eval(contents)
# Now, my_list contains the items from the text file as a list



# the DocBin will store the example documents
db = DocBin()
for text, annotations in training_data:
    doc = nlp(text)
    ents = []
    for start, end, label in annotations:
        span = doc.char_span(start, end, label=label)
        ents.append(span)
    doc.ents = ents
    db.add(doc)
db.to_disk("./train.spacy") 