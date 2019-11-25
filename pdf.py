#importing the module
from PyPDF2 import PdfFileReader,PdfFileWriter


def PdfReader(page):
  #creatign the pdf
    pdftext = "dummy-pdf_2.pdf"

    with open(pdftext, 'rb') as textpdf:
    #reading the PDF
      reader = PdfFileReader(textpdf)
    #getting the num of pages of the pdf file
    for page in range(reader.getNumPages()):
        default_page = reader.getPage(0) #getting the first page of the pdf as default apge when it gets open
        #not sure this is the right way
        if page > 0:
          merge_page = default_page.addPage(page +1 )
          return merge_page




    #checking that we closde the file if not, we do so
    if not textpdf.closed:
      textpdf.close()
      print "closed"





