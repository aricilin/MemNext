#coding: utf-8
import sys
import fitz
#check arg number
if (len(sys.argv) != 3):
    print("utilisation :PDFtoTXT.py PDF nom_output ")
    exit()

f_out=open(sys.argv[2],"w",encoding="utf-8")

 # install using: pip install PyMuPDF


with fitz.open(sys.argv[1]) as doc:
    for page in doc:
        text = page.get_text()
        for i in range(len(text)-1):
            if text[i] == '\n' and text[i+1].islower():
                continue  # skip writing newline character
            f_out.write(text[i])
        if len(text) > 0:
            f_out.write(text[-1])  # write the last character of the page (usually a newline character)


#closing files        
f_out.close()
