'''
This program creates a new file in write mode and to write textual data
if you open the file in write mode then the previous data gets deleted

if you open the file in append mode then the previously written data gets preserved
and does not delete the previous data

if you open the file in 'x' mode and if the file is already present then
it shows error

also we can open the file using with keyword as follows :
with open('hello.txt') as f:
    for i in f:
        print(i)

'''


if __name__ == '__main__':

    # opening file in write mode ,creates a new file if not present
    # truncates all the data if present in the file
    # and places the stream at the begining of file
    a = open("hello.txt", 'w')
    for i in range(5):
        print("hey i am writing in write mode", file=a)
    a.close()

    # opening file in reading mode creates a new file if not present
    # places the stream at the beginning of the file, by default open mode is reading mode
    a = open("hello.txt")
    for i in a:
        print(a)

    # opening file in append mode. can only write data and not read from the file
    # does not truncate the data in the file and places the stream at the end of the file
    a = open("hello.txt", 'a')
    for i in range(5):
        a.write('hey i am writing in append mode \n')
    a.close()

    # opening file in x mode will show error if the file is already present
    # also you cannot read data when using this mode
    # as the file is created new then the file stream is placed at the beginning
    a = open("hello.txt",'x')
    for i in range(5):
        a.write("hey i am writing in x mode ")



    a=open('hello.txt','r+')
    for i in a:
         a.write(i)
    #print(a.read())
    a.close()






