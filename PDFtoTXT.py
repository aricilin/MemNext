#coding: utf-8
import PyPDF2
import sys

#check arg number
if (len(sys.argv) != 3):
    print("utilisation :PDFtoTXT.py PDF nom_output ")
    exit()

f_out=open(sys.argv[2],"w",encoding="utf-8")


""" # Open the PDF file in binary mode
with open(sys.argv[1], 'rb') as f:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(f)
    
    num_pages = len(pdf_reader.pages)

    # Loop through all pages and extract text
    for page in range(num_pages):
        pdf_page = pdf_reader.pages[page]
        text = pdf_page.extract_text()
        unicode_text = str(text)
        print(unicode_text) 

 """


 # install using: pip install PyMuPDF
import fitz

with fitz.open(sys.argv[1]) as doc:
     
     for page in doc:
          #append characeter in each page
         f_out.write (page.get_text())

#closing files        
f_out.close()

# f.close()