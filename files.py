#####
f = open("test.txt")
f = open("test.txt","w")

open file : file_name.open()
write file : .write()
append : .append()
close : .close()
read : .read()
seek : .seek('A')
tell : .tell()

#files operations
f = open("test.txt")
f = open("test.txt",'w')
f = open("img.bmp",'r+b')


r opens a file for reading. (default)
w opens a file for writing.creates a new file.
x opens a file for exclusive creation.If the file already exists the operation fails
a opens a file for appending at the end of
t opens in a text mode.(default)
b opens in a binary mode
+ opens a file for updating(reading and writing)

NB(TEXT MODS -  )
