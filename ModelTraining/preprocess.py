import spacy
from spacy.tokens import DocBin
import ast

nlp = spacy.blank("fr")


with open("entrainement.txt", 'r', encoding="utf-8") as file:
    # Read the contents of the file
    contents = file.read()
    # Split the contents by the delimiter (e.g., comma)
    training_data = ast.literal_eval(contents)
# Now, my_list contains the items from the text file as a list


# the DocBin will store the example documents
db = DocBin()
pt = 0
for text, annotations in training_data:
    doc = nlp(text)
    ents = []
    for start, end, label in annotations:
        if label not in ["9"]:
            try:
                span = doc.char_span(start, end, label=label)
                ents.append(span)
                doc.ents = ents
            except TypeError:  # error  ex tag cut a word
                print(f"({start}, {end}, '{label}')")
                exit
    db.add(doc)
db.to_disk("./train.spacy")
