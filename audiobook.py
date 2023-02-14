import pyttsx3
import PyPDF2
book = open('DSA.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(14, pages):
    page = pdfReader.getPage(14)
    text= page.extractText()
    speaker.say(page)
speaker.runAndWait()
