#importing the module
from PyPDF2 import PdfFileReader,PdfFileWriter


def PdfReader(number):
  #reading the user input, not sure if is like this
  select = input(number)

  #creatign the pdf
  pdftext = "/home/juanfran/Downloads/juanlinkedingresume.pdf"

  with open(pdftext, 'rb') as textpdf:
    #reading the PDF
      reader = PdfFileReader(textpdf)
    #getting the num of pages of the pdf file
      for page in range(reader.getNumPages()):
        default_page = reader.getPage(0) #getting the first page of the pdf as default page when it gets open
        #not sure this is the right way
        if (select.isdigit()):
          merge_page = default_page.addPage(page + 1 )
          return merge_page




    #checking that we closde the file if not, we do so
  if not textpdf.closed:
      textpdf.close()
      print "closed"




