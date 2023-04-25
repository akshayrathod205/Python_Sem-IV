# to read an entire text file
def file_read(fname):
    txt = open(fname)
    print(txt.read())
    
file_read('test.txt')

#---------------------------------------------------------------------------------

#to read a file line by line and store it into a list
def file_read(fname):
    with open(fname) as f:
        #Content_list is the list that contains the read lines.
        content_list = f.readlines()
        print(content_list)
    
file_read('\\test.txt\\')

#---------------------------------------------------------------------------------
# to count the number of lines in a text file
def file_lengthy(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
            return i + 1
print("Number of lines in the file: ",file_lengthy("test.txt"))

#---------------------------------------------------------------------------------
# to copy the contents of a file to another file
from shutil import copyfile
copyfile('test.py', 'abc.py')

#---------------------------------------------------------------------------------

#takes a text file as input and returns the number of words of a given text file
def count_words(filepath):
    with open(filepath) as f:
        data = f.read()
        data.replace(",", " ")
        return len(data.split(" "))
    
print(count_words("words.txt"))

#---------------------------------------------------------------------------------
# to create a file where all letters of English alphabet are listed by specified number of letters on each line.

import string
def letters_file_line(n):
    with open("words1.txt", "w") as f:
        alphabet = string.ascii_uppercase
        letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]
        f.writelines(letters)
        
letters_file_line(3)

#---------------------------------------------------------------------------------
