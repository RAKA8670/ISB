#merge pdf together
from PyPDF2 import PdfFileWriter,PdfFileReader
#open first document
#open second document
#open a new third document and add first doc and second doc one by one

pdf_list = ["B:\\Alien Brain\\Python Warm-Up\\Test\\1.pdf","B:\\Alien Brain\\Python Warm-Up\\Test\\2.pdf"]
write_obj = PdfFileWriter()
for i in pdf_list:
	read_obj = PdfFileReader(i)
	pages = read_obj.getNumPages()
	#print(pages)
	for j in range(pages):
		p = read_obj.getPage(j)
		write_obj.addPage(p)

write_obj.encrypt("RAKA123","SR",True) #For only encrypt the PDF (otherwise each line is same)

pdf_file = open("B:\\Alien Brain\\Python Warm-Up\\Test\\encrypt.pdf","wb")
write_obj.write(pdf_file)

pdf_file.close()
