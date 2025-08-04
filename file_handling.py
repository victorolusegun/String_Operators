#To open text file without context manager
# 'r' = read a file, 'w' = write to file, 'a' = append to a file,
# 'r+' = read and write to a file
# file = open('file_handling.txt', 'r')
# print(file.name)
# print(file.mode)
# When opening a file like this, you must close it this way:
# file.close()
#Note, if this isn't done, you can end up with leaks that cause you to run over the maximum file descriptors 
#on your system and your apps could throw an error(Corey Schafer)

#Using a context manager. You have access to the file variable outside the function but the file is closed
# READING
# with open('file_handling.txt', 'r') as file:
#.read() prints out the entire contenrs of the file
    # file_contents = file.read()
    # print(file_contents)
#.readline() prints out the first line of the file
    # file_oneline = file.readline()
    # print(file_oneline, end ='')
# #repeating it prints out the next line
    # file_oneline = file.readline()
    # print(file_oneline, end = '')
#the next block of code is a more efficient way to print out the contents of a file
    # for line in file:
    #     print(line, end= '')
#the next block of code is essential to the next 3 after it
    # size_to_read = 50
    # file_content = file.read(size_to_read)
    # print(file_content, end = '')
#.seek() tells the file what position to start printing from
    # file.seek(10)
    # file_content = file.read(size_to_read)
    # print(file_content, end = '')
#.tell() prints out character the .read() is currently at
    # print(file.tell())
#another efficient way of reading files
    # while len(file_content) > 0:
    #     print(file_content, end = '')
    #     file_content = file.read(size_to_read)

# WRITE
# with open('new_file.txt', 'w') as f:
#     f.write('''Artificial Intelligence is transforming the world.
# From healthcare to finance, AI is finding real-world applications.
# Natural Language Processing is a major branch of AI.
# It allows machines to understand and generate human language.
# Are you ready to explore what comes next?''') 

#Reading from one file and writing to another file
with open('file_handling.txt', 'r') as file:
    with open('write_file_handling.txt', 'w') as wf:
        for line in file:
            wf.write(line) 