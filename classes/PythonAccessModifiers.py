if __name__ == '__main__':
    '''
        This program shows pythons implementation of private, protected and public instance members
        
        NO prefix underscore variable = Public member
        
        Single prefix undercore variable = Protected member(though it is just an convention, member is still is public)
        
        Double prefix underscore variable = Private member(can only be accessed by setter methods)
        
    '''


    class Person:

        def __init__(self, firstname='abhishek', lastname='mandal', address='c 67 ganesh nagar'):
            self.__firstname = firstname
            self.__lastname = lastname
            self.__address = address

        def getperson(self):
            return {'firstname': self.__firstname,
                    'lastname': self.__lastname,
                    'address': self.__address

                    }

        def getFirstname(self):
            return self.__firstname

        def getLastname(self):
            return self.__lastname

        def getAddress(self):
            return self.__address


    class Emp(Person):

        def __init__(self, firstname='ezio', lastname='auditore', companyame='assassins', address='Tuscany Italy'):
            super(Emp, self).__init__(firstname, lastname, address)
            self.__companyname = companyame

        def getFirstname(self):
            return super(Emp, self).getFirstname()

        def getLastname(self):
            return super(Emp, self).getLastname()

        def getCompanyname(self):
            return self.__companyname

        def getAddress(self):
            return super(Emp, self).getAddress()

        def getperson(self):
            test = super(Emp, self).getperson()
            test['company name'] = self.__companyname
            return test


    ob = Person('abhishek', 'mandal')
    print(ob.getperson())

    ob = Emp()
    print(ob.getperson())