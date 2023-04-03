#Converter
#Cette Program sert a transformer des differents format en txt.
#Supported Formats docx, doc, odt
#il recupere le 'nom_de_fichier' et donne nom_de_fichier.txt
#il faut appeler le fonction pour l'utiliser
#converter(histoire.docx)

import os
import docx2txt
import docx
from odf import text, teletype
from odf.opendocument import load
import subprocess

#my function
def converter(file):
    #toto+.txt
    file_extension = os.path.splitext(file)[1]
    txt_file = os.path.splitext(file)[0] + ".txt"

    if file_extension == ".docx":
        with open(txt_file, "w") as f:
            f.write(docx2txt.process(file))

    elif file_extension == ".odt":
        doc = load(file)
        with open(txt_file, "w") as f:
            for para in doc.getElementsByType(text.P):
                f.write(teletype.extractText(para))
                #si on veut saute de lignes
                #text = teletype.extractText(para) + "\n"
                #f.write(text)

    elif file_extension == ".doc":
        #Antiword is a free software reader for proprietary Microsoft Word documents, and is available for most computer platforms.
        #https://en.wikipedia.org/wiki/Antiword
        cmd = ["antiword", file]
        with open(txt_file, "w") as txt_file:
            #subprocess sert a lancer le program antiword sur cmd
            subprocess.run(cmd, stdout=txt_file)

    else:
        print("Format inconnue")



converter('test.odt')
