# creating dictionaries
hello = {'Name' : 'Abhishek Mandal', 'Age': 20}
print(hello['Name'])
print(hello['Age'])

print(hello.keys())

hello = dict([(12,1), ('name','abhishek')])
print(hello)

dic = {number : number**2 for number in range(10)}
print(dic)

# when keys are simple strings it is easier to specify pairs using keyword arguments
about = dict(name = 'abhishek', age = 20, profession = 'student')
print(about)


# Looping in dictionaries
for k, v in about.items():
    print(k, v)
