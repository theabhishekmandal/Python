class Dog:
    tricks = []    # this is a member which can be shared by all the objects

    def __init__(self, name):
        self.name = name

    def add_tricks(self, tricks):
        self.tricks.append(tricks)



d = Dog('sheroo')
e = Dog('muffy')
d.add_tricks('jump')
e.add_tricks('roll over')
print(e.tricks)
