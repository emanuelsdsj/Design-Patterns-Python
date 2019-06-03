"""
Decorator:
The Decorator attaches additional responsibilities to an object dynamically. The ornaments 
that are added to pine or fir trees are examples of Decorators. Lights, garland, candy canes,
glass ornaments, etc., can be added to a tree to give it a festive look. The ornaments do 
not change the tree itself which is recognizable as a Christmas tree regardless of particular 
ornaments used. As an example of additional functionality, the addition of lights allows one to "light up" 
a Christmas tree.

Problem:
You want to add behavior or state to individual objects at run-time. Inheritance is 
not feasible because it is static and applies to an entire class.

*References:
https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_decorator.htm
https://sourcemaking.com/design_patterns/decorator
"""

import six
from abc import ABCMeta

@six.add_metaclass(ABCMeta)
class Abstract_Coffee(object):

   def get_cost(self):
      pass

   def get_ingredients(self):
      pass
   
   def get_tax(self):
      return 0.1*self.get_cost()

class Concrete_Coffee(Abstract_Coffee):
   
   def get_cost(self):
      return 1.00
   
   def get_ingredients(self):
      return 'coffee'

@six.add_metaclass(ABCMeta)
class Abstract_Coffee_Decorator(Abstract_Coffee):
   
   def __init__(self,decorated_coffee):
      self.decorated_coffee = decorated_coffee
   
   def get_cost(self):
      return self.decorated_coffee.get_cost()
   
   def get_ingredients(self):
      return self.decorated_coffee.get_ingredients()

class Sugar(Abstract_Coffee_Decorator):
   
   def __init__(self,decorated_coffee):
      Abstract_Coffee_Decorator.__init__(self,decorated_coffee)
   
   def get_cost(self):
      return self.decorated_coffee.get_cost()
   
   def get_ingredients(self):
	   return self.decorated_coffee.get_ingredients() + ', sugar'

class Milk(Abstract_Coffee_Decorator):
   
   def __init__(self,decorated_coffee):
      Abstract_Coffee_Decorator.__init__(self,decorated_coffee)
   
   def get_cost(self):
      return self.decorated_coffee.get_cost() + 0.25
   
   def get_ingredients(self):
      return self.decorated_coffee.get_ingredients() + ', milk'

class Vanilla(Abstract_Coffee_Decorator):
   
   def __init__(self,decorated_coffee):
      Abstract_Coffee_Decorator.__init__(self,decorated_coffee)
   
   def get_cost(self):
      return self.decorated_coffee.get_cost() + 0.75
   
   def get_ingredients(self):
      return self.decorated_coffee.get_ingredients() + ', vanilla'

def main():
	myCoffee = Concrete_Coffee()
	print('Ingredients: '+myCoffee.get_ingredients()+
	'; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

	myCoffee = Milk(myCoffee)
	print('Ingredients: '+myCoffee.get_ingredients()+
	'; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

	myCoffee = Vanilla(myCoffee)
	print('Ingredients: '+myCoffee.get_ingredients()+
	'; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

	myCoffee = Sugar(myCoffee)
	print('Ingredients: '+myCoffee.get_ingredients()+
	'; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

	return 0
	
if __name__ == "__main__":
	main()

"""
OUTPUT:
Ingredients: coffee; Cost: 1.0; sales tax = 0.1
Ingredients: coffee, milk; Cost: 1.25; sales tax = 0.125
Ingredients: coffee, milk, vanilla; Cost: 2.0; sales tax = 0.2
Ingredients: coffee, milk, vanilla, sugar; Cost: 2.0; sales tax = 0.2
[Finished in 0.1s]
"""