'''
- In this program we will create a class and provides the default values of the attributes using the constructor
- in the init method we can see that we have provided the default values for the attributes
- here we also override the __repr__ method of the object class

'''

class demo4:
	def __init__(self,a:int=1,b:int=1)->None:
		self.val=a
		self.incr=b

	
	def increase(self)-> None:
		self.val+=self.incr


	def __repr__(self)->str:
		return  str(self.val)



if __name__ == '__main__':
	ob=demo4()
	print(ob.val,ob.incr)
	ob.increase()
	print(ob.val,ob.incr)
	print(ob)
