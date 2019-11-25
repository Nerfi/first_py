#importing the module
from PyPDF2 import PdfFileReader


def PdfReader(page):
  #creatign the pdf
  pdftext = "dummy-pdf_2.pdf"

  with open(pdftext, 'rb') as textpdf:
    #reading the PDF
    reader = PdfFileReader(textpdf)
    #getting the num of pages of the pdf file
    for page in range(textpdf.getNumPages()):
        current_page = textpdf.getPage(0) #getting current page






    #checking that we closde the file if not, we do so
    if not textpdf.closed:
      textpdf.close()
      print "closed"





