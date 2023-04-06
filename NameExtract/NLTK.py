import nltk
import sys

#check arg number
if (len(sys.argv) != 2):
    print("utilisation : NameExtractNLTK.py texte_source")
    exit()

# download the necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# define text to read

text= open(sys.argv[1],"r")
# use NLTK's word tokenizer to split the text into words
words = nltk.word_tokenize(text.read())

# use NLTK's part-of-speech tagger to tag each word with its part of speech
pos_tags = nltk.pos_tag(words)

# use NLTK's named entity recognizer to identify named entities in the text
chunks = nltk.ne_chunk(pos_tags)

# iterate over each chunk in the named entity tree
nameList =[]
nb=0
for chunk in chunks:
    # if the chunk is a named entity (NE), its label is 'PERSON' and it's not in nameList, print it
    if hasattr(chunk, 'label') and chunk.label() == 'PERSON' and chunk not in nameList:
        print(' '.join(c[0] for c in chunk))
        nameList.append(chunk)
        nb+=1
print(nb,  " lignes")
