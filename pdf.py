#importing the module
from PyPDF2 import PdfFileReader,PdfFileWriter


def PdfReader(number,pdf,new_pdf):
  #creatign the pdf
  pdftext = "/home/juanfran/Downloads/juanlinkedingresume.pdf"

  with open(pdftext, 'rb') as textpdf:
    #reading the PDF
      reader = PdfFileReader(textpdf)
      page = reader.getPage(number) #take the page the user wants
      with open(new_pdf,"wb") as f:
        writer = PdfFileWriter() #creates the pdf writer
        writer.addPage(page)
        writer.write(f)

  if __name__ == "__main__":
    PdfReader(0)



