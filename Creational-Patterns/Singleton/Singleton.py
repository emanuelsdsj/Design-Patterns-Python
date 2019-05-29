"""
Singleton:
The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance. 
It is named after the singleton set, which is defined to be a set containing one element. The office of the 
President of the United States is a Singleton. The United States Constitution specifies the means by which a president 
is elected, limits the term of office, and defines the order of succession. As a result, there can be at most one active 
president at any given time. Regardless of the personal identity of the active president, the title, "The President of the 
United States" is a global point of access that identifies the person in the office.

Problem:
Application needs one, and only one, instance of an object. Additionally, lazy initialization and global access are necessary.

*References:
https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
https://sourcemaking.com/design_patterns/singleton
"""

class Singleton:
   instance = None
   test = "Atma"
   @staticmethod 
   def getInstance():
      """ Static access method. """
      if Singleton.instance == None:
         Singleton()
      return Singleton.instance
   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.instance = self
   def setTest(self, test):
   	self.test = test
   def getTest(self):
   	return self.test

firstInstance = Singleton()
secondInstance = Singleton.getInstance()

firstInstance.setTest("Ultima")
print("SecondInstance - variable test: ", secondInstance.getTest())

print("Trying to create another instance:")
x = Singleton()
"""
OUTPUT:
SecondInstance - variable test: Ultima

Trying to create another instance:
	raise Exception("This class is a singleton!")
"""