import sys
from SeedExtractor import SeedExtractor
from SeedSerializer import JsonSerializer, CsvSerializer


modelPath = "./ModelTraining"
distanceThreshold = 100


if (len(sys.argv) != 3):
    print("utilisation : main.py texte_source texte_sortie")
    exit()

extractor = SeedExtractor(modelPath)
print("Extracting seeds...")
seedList = extractor.extract(sys.argv[1])
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
        serializer = CsvSerializer(sys.argv[2])
    case "json":
        serializer = JsonSerializer(sys.argv[2])
    case _:
        serializer = CsvSerializer(sys.argv[2])


print("Writing output to", serializer.filename)
serializer.write(seedList)
