"""
Template Method:
A Strategy defines a set of algorithms that can be used interchangeably. Modes of transportation to 
an airport is an example of a Strategy. Several options exist such as driving one's own car, taking a 
taxi, an airport shuttle, a city bus, or a limousine service. For some airports, subways and helicopters 
are also available as a mode of transportation to the airport. Any of these modes of transportation will 
get a traveler to the airport, and they can be used interchangeably. The traveler must chose the Strategy 
based on trade-offs between cost, convenience, and time.

Problem:
One of the dominant strategies of object-oriented design is the "open-closed principle".
Figure demonstrates how this is routinely achieved - encapsulate interface details in a base class, 
and bury implementation details in derived classes. Clients can then couple themselves to an interface, 
and not have to experience the upheaval associated with change: no impact when the number of derived 
classes changes, and no impact when the implementation of a derived class changes.

*References:
https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_template.htm
https://sourcemaking.com/design_patterns/template_method
"""

class MakeMeal:

   def prepare(self): pass
   def cook(self): pass
   def eat(self): pass

   def go(self):
      self.prepare()
      self.cook()
      self.eat()

class MakePizza(MakeMeal):
   def prepare(self):
      print("Prepare Pizza")
   
   def cook(self):
      print("Cook Pizza")
   
   def eat(self):
      print("Eat Pizza")

class MakeTea(MakeMeal):
   def prepare(self):
      print("Prepare Tea")
	
   def cook(self):
      print("Cook Tea")
   
   def eat(self):
      print("Eat Tea")

makePizza = MakePizza()
makePizza.go()

print(25*"+")

makeTea = MakeTea()
makeTea.go()

"""
OUTPUT:
Prepare Pizza
Cook Pizza
Eat Pizza
+++++++++++++++++++++++++
Prepare Tea
Cook Tea
Eat Tea
[Finished in 0.1s]
"""