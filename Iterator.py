def first():
    # looping using items of the list
    one = [1, 2, 3, 4]
    for i in one:
        print(i, end = '')


def second():
    one = [1, 2, 3, 4]
    # looping using range of the list
    for i in range(len(one)):
        print(one[i], end='')

def third():
    one = [1, 2, 3, 4]
    # looping using enumerate method
    # enumerate method provides index as well as the value of the iterable object
    two = tuple(one)
    for index, val in enumerate(two):
        print(index, val)


def fourth():
    # two loop over two or more sequences we can use zip method
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('what is your {0}? It is {1}'.format(q, a))


def fifth():
    # to loop in reverse, first specify the sequence in forward direction
    print('fact of 9 using reverse range')
    fact = 1
    for i in reversed(range(1, 9)):
        fact *= i
    print(fact)


def sixth():
    # printing the sorted values of a given iterable in reverse order
    basket = 'apple', 'orange', 'apple', 'pear', 'orange', 'banana'
    for i in sorted(basket, reverse=True):
        print(i)


def seventh():
    for char in "123":
        print(char)

def workingOfFor():
    '''The for statements calls the iter() on the container object.
        The iter() function returns an iterator object that defines the __next__() method
        This next method accesses the elements of the container one at a time
        When it reaches where there are no elements then it raises a Stopiteration exception
    '''
    string = "1234"
    it = iter(string)
    try:
        def call():
            print(next(it), end = ' ')
            call()
        call()
    except StopIteration:
        exit(0)


workingOfFor()