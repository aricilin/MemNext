from Seed import Seed
import spacy
import utils

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
        nlp = spacy.load("fr_core_news_sm")


        text = open(inputText,"r")

        doc = nlp(text.read())

        #if an entity is not in nameList and its label is 'PERSON' print it
        nameList = []
        for entity in doc.ents:
            if entity.text not in nameList:
                print(entity.text, entity.label_)
                nameList.append(entity.text)

        

        





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

    
