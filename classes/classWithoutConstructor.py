'''
In this program we will create a method inside a class to demonstrate how it works

- first we create a method and pass self to it which shows that it is referring to the current object.
- then to refer to the attributes of the object we use self.attributename
- but if you try to print the values of the attributes then it will show the error because the values 
  have not been initialised 


'''

# In short this code will generate error
class demo2:
	def increase(self):
		self.val+=self.inc

if __name__ == '__main__':
	ob=demo2()
	ob.increase()
	print(ob.val,ob.inc,end=' ')
