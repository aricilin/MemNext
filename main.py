import sys
from SeedExtractor import SeedExtractor
from SeedSerializer import JsonSerializer, CsvSerializer
import spacy
from spacy import displacy
import webbrowser
from spacy.tokens import Doc


modelPath = "./ModelTraining"
distanceThreshold = 100


if (len(sys.argv) != 4):
    print("utilisation : main.py texte_source seeds_file links_file")
    exit()

extractor = SeedExtractor(modelPath)
print("Extracting seeds...")
seedList, fulldoc = extractor.extract(sys.argv[1])
print("Extraction complete, found {} seeds".format(len(seedList)))

relationList = []
for i in range(len(seedList)):
    for j in range(i+1, len(seedList)):
        dist = seedList[i].distance(seedList[j])
        if dist > 0 and dist < distanceThreshold:
            relationList.append((seedList[i].key, seedList[j].key))

print("Linking complete, found {} relations".format(len(relationList)))

output_file_extension = sys.argv[2].split(".")[-1].lower()
match output_file_extension:
    case "csv":
        serializer = CsvSerializer(sys.argv[2], sys.argv[3])
    case "json":
        serializer = JsonSerializer(sys.argv[2], sys.argv[3])
    case _:
        serializer = CsvSerializer(sys.argv[2], sys.argv[3])


print("Writing output to", serializer.filename, ", ", serializer.filename_links)
serializer.write(seedList)
serializer.writeLinks(relationList)


# seeds colors option
colors = {"0": "#F3F4ED", "1": "#F28482", "2": "#96BB7C", "3": "#76b5c5", "4": "#abdbe3",
          "5": "#D6EFC7", "6": "#F5CAC3", "7": "#7D1F35", "8": "#158467", "9": "#22577A"}
options = {"colors": colors}

# auto opening of web browser
url = "http://localhost:5000/"
webbrowser.open(url)

server = displacy.serve(fulldoc, style="ent", options=options)

