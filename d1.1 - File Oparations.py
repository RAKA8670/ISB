"""
#open a file
#give filename+extaintion
#click enter

fo = open("B:\\Alien Brain\\Python Warm-Up\\exm.txt","a")
fo.write("Again Hallo. Welcome Python to fuck my ass again...\n") 

#Type multiple Lines
lines = ["Apple\n","Banana\n","Coconut\n","Again?"]
fo.writelines(lines)

# moving a file
#create a new folder
import os

os.mkdir("B:\\Alien Brain\\Python Warm-Up\\Test") 

#change the location of a file

import shutil
shutil.move("B:\\Alien Brain\\Python Warm-Up\\exm.txt","B:\\Alien Brain\\Python Warm-Up\\Test\\exm.txt ") """

file_list = ["B:\\Alien Brain\\Python Warm-Up\\handout1_update.docx","B:\\Alien Brain\\Python Warm-Up\\exm.txt"]
for i in file_list:
	print(i)
	print("***************************")
print("FOR Loop End")


