import sys
from SeedExtractor import SeedExtractor
from SeedSerializer import JsonSerializer, CsvSerializer


modelPath = "./ModelTraining"


if (len(sys.argv) != 3):
    print("utilisation : main.py texte_source texte_sortie")
    exit()

extractor = SeedExtractor(modelPath)
print("Extracting seeds...")
seedList = extractor.extract(sys.argv[1])
print("Extraction complete, found {} seeds".format(len(seedList)))


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
