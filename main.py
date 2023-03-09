from SeedExtractor import SeedExtractor
import sys




if (len(sys.argv) != 2):
    print("utilisation : main.py texte_source")
    exit()

extractor = SeedExtractor()

extractor.extract(sys.argv[1])