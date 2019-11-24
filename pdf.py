#importing the module
import PyPDF2

def pdfReader(page):
  #creating an object/open it
  file = open('example.pdf', 'rb')

  #reading the pdf
  pdfReader  = PyPDF2.pdfFileReader(file)

  #getting the pages, the first one 0.
  pageObj = pdfReader.getPage(0)

  #closing the file
  file.close()


  #necesito:
  #abrirb el pdf
  #leerlo ?
  #darle al usuari la pagina que quiere
  # i should split the pages and then send back one by one


#idea 2

def PdfReader(page):
  pdftext = "example.pdf"

  with open(pdftext, 'rb') as textpdf:
    #reading the PDF
    reader = PdfFileReader(textpdf)

    #getting the num of pages of the pdf file
    for page in range(textpdf.getNumPages()):
      current_page = textpdf.getPage() #getting current page







    #checking that we closde the file if not, we do so
    if not textpdf.closed:
      textpdf.close()
      print "closed"




