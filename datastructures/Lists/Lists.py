if __name__ == '__main__':
    #input = input('Enter anything \n').strip()

    input = '1234'
    print('''Ways to convert to list are''')


    # 1st method
    input = [input]
    print(input)


    # 2nd method
    print('''Converting to list as seperate elements''')
    '''For eg: if input is 'abcd' then list('abcd') will get converted into ['a', 'b', 'c', 'd'] '''


    # 2.1 method
    input = list('1234')
    print(input)


    # 2.2 method
    input = [str(i) for i in '1234']
    print(input)

    ###################################################################################################################

    print('''Converting single string list to separate elements of list of integers''')

    # 1st method
    input = [int(i) for i in '1234']
    print(input)

    # 2nd method
    input = list(map(int, '1234'))
    print(input)


    # Wrong as int object is not iterable
    # input = list(int('1234'))
    # print(input)

    ###################################################################################################################

    print('''Converting list back to string''')

    # 1st method
    # if the list is containing only str elements
    test = "".join(['1234'])
    print(test)

    # Wrong as it converts the square brackets to string also
    #test = list(str(['1234']))
    #print(test)


    # 2nd method
    # if the list items are integers first convert them to str then join
    input = "".join(str(i) for i in [1, 2, 3 , 4])
    print(input)


    # Wrong int not iterable
    # test = "".join(int(i) for i in [1234])

    ###################################################################################################################


    '''List operations'''

    print('''Adding to a list''')

    # 1st method
    hel = [1, 2, 3, 4]
    hel.append(5)
    print(hel)


    # 2nd method
    hel = [1, 2, 3, 4]
    hel[len(hel):] = [5]
    print(hel)


    print('''Extending a list''')

    # 1st method
    hel = [1, 2, 3, 4]
    hel.extend([5, 6, 7])
    print(hel)


    # 2nd method
    hel =  [1, 2, 3, 4]
    hel[len(hel):] = [5, 6, 7]
    print(hel)


    print('''Inserting element at a given position''')

    hel = [1, 2, 3, 4]
    hel.insert(3, 5) # first is index and second is value
    print(hel)


    print('''Removing the value in a list (first occurence)''')

    hel = [1, 2, 3, 4, 2, 2]
    hel.remove(2)
    print(hel)


    print('''Poping an element from given index''')

    hel = [1, 2, 3, 4, 5, 6]
    hel.pop(4)
    print(hel)


    print('''Removes from last if nothing is specified''')

    hel = [1, 2, 3, 4, 5, 6]
    hel.pop()
    print(hel)


    print('''Delete all elements''')

    # 1st method
    hel = [1, 2, 3, 4, 5, 6]
    hel.clear()
    print(hel)


    # 2nd method
    hel = [1, 2, 3, 4, 5, 6]
    hel = []
    print(hel)


    # 3rd method
    hel = [1, 2, 3, 4, 5, 6]
    del hel[:]
    print(hel)


    print('''Returning index of list element''') # throws error if not found
    hel = [1, 2, 3, 4, 5, 6]
    print(hel.index(6))


    print('''Count number of occurences of a given element''')
    hel = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    print(hel.count(4))


    print('''Sorting inplace''')

    # 1st method
    hel = [4, 3, 2, 1]
    hel.sort()
    print(hel)


    # 2nd method
    hel = [4, 3, 2, 1]
    hel = sorted(hel)
    print(hel)


    print('''Reversing the elements''')

    # 1st method
    hel = [1, 2, 3, 4, 5, 6]
    hel.reverse()
    print(hel)


    # 2nd method
    hel = [1, 2, 3, 4, 5, 6]
    hel = hel[::-1]
    print(hel)


    print('''Returning copy of the list''')

    # 1st method
    hel = [1, 2, 3, 4, 5, 6]
    blah = hel.copy()
    print(blah)

    # 2nd method
    hel = [1, 2, 3, 4, 5, 6]
    blah = hel[:]
    print(blah)

    # Wrong as it assigns the reference and doesn't copy
    # print('''Wrong''')
    # hel = [1, 2, 3, 4, 5, 6]
    # blah = hel
    # blah.pop()
    # print(hel)
    # print(blah)


    





