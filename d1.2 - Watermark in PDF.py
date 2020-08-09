#watermark in PDF
from PyPDF2 import PdfFileWriter,PdfFileReader

#read the PDF
#read the Watermark
#create a new pdf
#for each page merge watermark in pages

pdf = PdfFileReader("B:\\Alien Brain\\Python Warm-Up\\Test\\1.pdf")
watermark = PdfFileReader("B:\\Alien Brain\\Python Warm-Up\\Test\\Watermark.pdf")
w_page = watermark.getPage(0) 	#Get the first page from Watermark PDF

new_pdf = PdfFileWriter()

pages = pdf.getNumPages()		#Get Number of Pages in PDF
for i in range(pages):			#Get the pages in a List
	page = pdf.getPage(i)			#Get the indexed page in PDF
	page.mergePage(w_page)
	new_pdf.addPage(page)

pdf_file = open("B:\\Alien Brain\\Python Warm-Up\\Test\\Watermarked PDF.pdf","wb")
new_pdf.write(pdf_file)

pdf_file.close()
