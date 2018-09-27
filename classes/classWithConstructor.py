'''
In the previous program we could see that the attribute values were not initialised, due to which 
it was showing error

here we will use a constructor to initialise the values of the attribute values 
Constructor in python is defined as __init__ (dunder init method) we pass the self keyword along with the values of 
the attributes
'''

class demo3:
	def __init__(self,a:int,b:int)->None:
		self.val=a
		self.incr=b

	def increase(self)-> None:
		self.val+=self.incr

if __name__ == '__main__':
	ob=demo3(10,20)
	print(ob.val,ob.incr)
	ob.increase()
	print(ob.val,ob.incr)
