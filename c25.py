#FILE HANDLING
#create, Delete, edit and view

#PARAMETERS
# W-WRITE
# A-APPEND
# X-create file and write
# r-read
# t-text
# b-binary# 
from colorama import Fore,Style,Back

# f=open("demo.txt","rt")    #"rt"=read.text
# print(Fore.RED+Style.BRIGHT+"IT IS USED FOR READ WHOLE LINE"+Style.RESET_ALL+Fore.RESET)           
# print(f.read())  # read() = to read whole line

# f=open("demo.txt","rt")                                         
# print(Fore.GREEN+Style.BRIGHT+"IT IS USED FOR RAED ONLY ONE LNE"+Style.RESET_ALL+Fore.RESET)             
# print(f.readline())  # read() = to read one line
# print(f.readline())


# f=open("demo.txt","w")           # w = write a program
# f.write("IT IS USED FOR RAED ONLY ONE LNE")     # write = write a program


# f=open("demofile.txt","x")
# f.write("This is new file i created using python")


# f=open("demofile1.txt","x")            # it is used for create new file in python programmig
# f=open("demofile2.txt","x")
# f=open("demofile3.txt","x")      
# f=open("demofile4.txt","x")


# import os
# os.remove("demofile4.txt")           # it is used for delete the file


# import os
# os.mkdir("sagar_T new folder")            # it is used for create a new folder 

import os
os.rmdir("sagar_T new folder")           # it is used for delete the folder
