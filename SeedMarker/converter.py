#Converter

import os
import docx2txt
import odf.text
# from odf.opendocument import load
import odf.teletype
import odf.opendocument
import subprocess
import fitz


#my function
def converter(file):
    #toto+.txt
    file_extension = os.path.splitext(file)[1]
    txt_file = os.path.splitext(file)[0] + ".txt"
    foutput = "temp/"+txt_file.split('/')[len(txt_file.split('/'))-1]

    if file_extension == ".txt":
        return file
    elif len(file)==0:
        return 0
    with open(foutput, "w", encoding='utf-8') as f:   
        match file_extension:
            case ".docx":
                f.write(docx2txt.process(file))

            case ".odt":
                doc = odf.opendocument.load(file)
                for para in doc.getElementsByType(odf.text.P):
                    f.write(odf.teletype.extractText(para))
                    #si on veut saute de lignes
                    #text = teletype.extractText(para) + "\n"
                    #f.write(text)


            case ".doc":
                #Antiword is a free software reader for proprietary Microsoft Word documents, and is available for most computer platforms.
                #https://en.wikipedia.org/wiki/Antiword
                cmd = ["antiword", file]
                #subprocess sert a lancer le program antiword sur cmd
                subprocess.run(cmd, stdout=txt_file)
            
            case ".pdf":
                with fitz.open(file) as doc:
                    for page in doc:
                        text = page.get_text()
                        for i in range(len(text)-1):
                            if text[i] == '\n' and text[i+1].islower():
                                continue  # skip writing newline character
                            f.write(text[i])
                        if len(text) > 0:
                            f.write(text[-1])  # write the last character of the page (usually a newline character)
            case _:
                return(-1)
    # print (f"converter : {foutput}")
    return foutput
