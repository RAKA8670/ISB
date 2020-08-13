from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter, HTMLConverter, XMLConverter
from pdfminer.layout import LAParams
import io

path = "B:\\Alien Brain\\Python Warm-Up\\Test\\2.pdf"
pdf = open(path,'rb')

mem = io.StringIO()
lp = LAParams()
rm = PDFResourceManager()
#cnv = TextConverter(rm,mem,laparams=lp)
#cnv = HTMLConverter(rm,mem,laparams=lp)
cnv = XMLConverter(rm,mem,laparams=lp)
ip = PDFPageInterpreter(rm,cnv)

for i in PDFPage.get_pages(pdf):
	ip.process_page(i)
	text = mem.getvalue()

file = open(path+"Converted.xml",'wb')
file.write(text.encode('utf-8'))

print("DONE")

