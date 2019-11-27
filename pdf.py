#importing the module
from PyPDF2 import PdfFileReader,PdfFileWriter


def PdfReader(number,pdf):
  #creatign the pdf
  pdftext = "/home/juanfran/Downloads/juanlinkedingresume.pdf"

  #with =  context manager, dont need to close the file
  #when using context manager, ptyhon will do that for us

  with open(pdftext, 'rb') as textpdf:
    #reading the PDF
      reader = PdfFileReader(textpdf)
      page = reader.getPage(number) #take the page the user wants
      with open("new.pdf","wb") as f:
        writer = PdfFileWriter() #creates the pdf writer
        writer.addPage(page)
        writer.write(f)

  if __name__ == "__main__":
    PdfReader(0)


#importing the module
from PyPDF2 import PdfFileReader,PdfFileWriter

def PdfReader(number,pdf,new_pdf):
  #Original pdf to read

  with open(pdf, 'rb') as textpdf: # open the pdf (will close automatically)
      reader = PdfFileReader(textpdf) # create the reader
      page = reader.getPage(number) # grab the page we want
      with open(new._pdf,"wb") as f: # create the new pdf
        writer = PdfFileWriter() # create the pdf writer
        writer.addPage(page) # add the page to the buffer
        writer.write(f) # write the new pdf to the filestream

if __name__ == "__main__": # magic to run the method automatically
    PdfReader(0) # call the code we wrote, get the first page

