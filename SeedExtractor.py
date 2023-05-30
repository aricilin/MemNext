from Seed import Seed
import spacy
from spacy import displacy
import sys
from spacy.lang.fr import French
import webbrowser
from spacy.tokens import Doc

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
        text = open(inputText, "r", encoding="utf-8")

        #doc = self.nlp(text.read())

        nameList = []
        seedList = []
        seedNumber = 0

        print("Found {} seeds".format(seedNumber), end='\r')


        filepath = inputText
        filename = filepath.split('/')[len(filepath.split('/'))-1]
        foutput = f"output/{filename}"

        tuplelist = []
        outputlist=[]
        sentences = list(filter(lambda x : x != '', text.read().split('\n\n')))


        listdoc=[]


        for sentence in sentences:
            doc = self.nlp(sentence)
            for entity in doc.ents:
                tuple = (entity.start_char, entity.end_char, entity.label_)
                tuplelist.append(tuple)
                
                seedName = entity.text.replace("\n", " ")

                match entity.label_:
                    case "1":
                        seed = Seed(quality="q1",
                                    key=str(seedNumber),
                                    name=seedName,
                                    _position_start=entity.start,
                                    _position_end=entity.end
                        )

                    case "2":
                        seed = Seed(quality="q2",
                                    key=str(seedNumber),
                                    name=seedName,
                                    _position_start=entity.start,
                                    _position_end=entity.end
                        )

                    case "3":
                        seed = Seed(quality="q3",
                                    key=str(seedNumber),
                                    name=seedName,
                                    _position_start=entity.start,
                                    _position_end=entity.end
                        )
                    
                    case "4":
                        seed = Seed(quality="q4",
                                    key=str(seedNumber),
                                    name=seedName,
                                    _position_start=entity.start,
                                    _position_end=entity.end
                        )

                    case "5":
                        seed = Seed(quality="q5",
                                    key=str(seedNumber),
                                    name=seedName,
                                    _position_start=entity.start,
                                    _position_end=entity.end
                        )

                    case "6":
                        seed = Seed(quality="q6",
                                    key=str(seedNumber),
                                    name=seedName,
                                    _position_start=entity.start,
                                    _position_end=entity.end
                        )

                    case "7":
                        seed = Seed(quality="q7",
                                    key=str(seedNumber),
                                    name=seedName,
                                    _position_start=entity.start,
                                    _position_end=entity.end
                        )

                    case "8":
                        seed = Seed(quality="q8",
                                    key=str(seedNumber),
                                    name=seedName,
                                    _position_start=entity.start,
                                    _position_end=entity.end
                        )

                    case "9":
                        seed = Seed(quality="q9",
                                    key=str(seedNumber),
                                    name=seedName,
                                    _position_start=entity.start,
                                    _position_end=entity.end
                        )

                    case _:
                        seed = Seed(quality="q0",
                                    key=str(seedNumber),
                                    name=seedName,
                                    _position_start=entity.start,
                                    _position_end=entity.end
                        )
                
                seedList.append(seed)
                seedNumber += 1
                print("Found {} seeds".format(seedNumber), end='\r')

                nameList.append(entity.text)

            listdoc.append(doc)
            outputlist.append((sentence,tuplelist))
            tuplelist=[]

        fulldoc = Doc.from_docs(listdoc)

        with open(foutput, "w", encoding="utf-8") as f:
            f.write(str(outputlist))

        try :#save in training seedmarker
            foutput = f"./SeedMarker/training/extracted/{filename}"
            with open(foutput, "w", encoding="utf-8") as f:
                f.write(str(outputlist))
        except FileNotFoundError:
            exit

        
        print("Found {} seeds".format(seedNumber))


        return (seedList, fulldoc)


        

        





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

    
