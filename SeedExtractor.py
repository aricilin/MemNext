from Seed import Seed
import spacy
from spacy.lang.fr import  French

class SeedExtractor:


    def __init__(self, modelPath):
        """
        Constructor

        """
        config = spacy.Config().from_disk("{}/config.cfg".format(modelPath))
        nlp = French.from_config(config) 
        nlp.from_disk("{}/output/model-best".format(modelPath))
        self.nlp = nlp


    def extract(self, inputText):
        """
        Extracts a list of seeds from given text.

        :param inputText: Text to extract seeds from.
        :type inputText: str
        :return: A list of seeds.
        :rtype: list[Seed]

        """
        text = open(inputText,"r")

        doc = self.nlp(text.read())

        nameList = []
        seedList = []
        seedNumber = 0

        print("Found {} seeds".format(seedNumber), end='\r')

        for entity in doc.ents:
            if entity.text not in nameList:
                #print(entity.text, entity.label_)
                
                seedName = entity.text.replace("\n", " ")

                match entity.label_:
                    case "1":
                        seed = Seed(quality=1,
                                    key=str(seedNumber),
                                    name=seedName,
                                    _position_start=entity.start,
                                    _position_end=entity.end
                        )

                    case "2":
                        seed = Seed(quality=2,
                                    key=str(seedNumber),
                                    name=seedName,
                                    _position_start=entity.start,
                                    _position_end=entity.end
                        )

                    case "3":
                        seed = Seed(quality=3,
                                    key=str(seedNumber),
                                    name=seedName,
                                    _position_start=entity.start,
                                    _position_end=entity.end
                        )
                    
                    case "4":
                        seed = Seed(quality=4,
                                    key=str(seedNumber),
                                    name=seedName,
                                    _position_start=entity.start,
                                    _position_end=entity.end
                        )

                    case "5":
                        seed = Seed(quality=5,
                                    key=str(seedNumber),
                                    name=seedName,
                                    _position_start=entity.start,
                                    _position_end=entity.end
                        )

                    case "6":
                        seed = Seed(quality=6,
                                    key=str(seedNumber),
                                    name=seedName,
                                    _position_start=entity.start,
                                    _position_end=entity.end
                        )

                    case "7":
                        seed = Seed(quality=7,
                                    key=str(seedNumber),
                                    name=seedName,
                                    _position_start=entity.start,
                                    _position_end=entity.end
                        )

                    case "8":
                        seed = Seed(quality=8,
                                    key=str(seedNumber),
                                    name=seedName,
                                    _position_start=entity.start,
                                    _position_end=entity.end
                        )

                    case "9":
                        seed = Seed(quality=9,
                                    key=str(seedNumber),
                                    name=seedName,
                                    _position_start=entity.start,
                                    _position_end=entity.end
                        )

                    case _:
                        seed = Seed(quality=0,
                                    key=str(seedNumber),
                                    name=seedName,
                                    _position_start=entity.start,
                                    _position_end=entity.end
                        )
                
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

    
