# Writing data into text file

# file=open(r"C:\Users\santo\OneDrive\Desktop\Python\fileHandlingDemo.txt",'w')
# file.write("This is my first statements...\n")
# file.write("This is my second statements...\n")
# file.write("This is my Third statements...\n")
# file.write("This is my Fourth statements...\n")
# file.write("This is my Sixth statements...")
# file.close()
# print("program completed")

#Example 2 reading data from text file
# file=open(r"C:\Users\santo\OneDrive\Desktop\Python\fileHandlingDemo.txt",'r')
# print(file.read())  # read() is to read all file
# #print(file.readline()) # this is for to read 1st line of sentence
# file.close()

#Example 3 : appending data into text file
file=open(r"C:\Users\santo\OneDrive\Desktop\Python\fileHandlingDemo.txt",'a')
file.write("\nThis is my 7th statements...\n")
file.write("This is my 8th statements...")
file.close()
