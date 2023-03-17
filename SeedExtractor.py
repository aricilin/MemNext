from Seed import Seed
import spacy

class SeedExtractor:


    def __init__(self):
        """
        Constructor

        """

    def extract(self, inputText):
        """
        Extracts a list of seeds from given text.

        :param inputText: Text to extract seeds from.
        :type inputText: str
        :return: A list of seeds.
        :rtype: list[Seed]

        """
        #nlp = spacy.load("fr_core_news_sm")
        nlp = spacy.load("fr_core_news_lg")

        print(nlp.get_pipe("ner").labels)

        text = open(inputText,"r")

        doc = nlp(text.read())

        nameList = []
        seedList = []
        seedNumber = 0

        print("Found {} seeds".format(seedNumber), end='\r')

        for entity in doc.ents:
            if entity.text not in nameList:
                #print(entity.text, entity.label_)
                
                seedName = entity.text.replace("\n", " ")

                match entity.label_:
                    case "PER":
                        seed = Seed(quality=1, name=seedName)

                    case "ORG":
                        seed = Seed(quality=6, name=seedName)

                    case _:
                        seed = Seed(quality=0, name=seedName)
                
                seedList.append(seed)
                seedNumber += 1
                print("Found {} seeds".format(seedNumber), end='\r')

                nameList.append(entity.text)
        
        print("Found {} seeds".format(seedNumber))


        return seedList


        

        





    def write(self, seedList, file, format):
        """
        Write a list of seeds to a file in the specified format

        :param seedList: Seeds to write
        :type seedList: list[Seed]
        :param file: File to write to
        :type file: str
        :param format: File format
        :type inputText: str
        :return: None
        :rtype: None

        """

    
