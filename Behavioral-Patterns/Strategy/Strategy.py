"""
Strategy:
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
https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_strategy.htm
https://sourcemaking.com/design_patterns/strategy
"""

import types

class Strategy:
   def __init__(self, func = None):
      self.name = 'Strategy Example 0'
      if func is not None:
         self.execute = types.MethodType(func, self)

   def execute(self):
      print(self.name)


def execute_replacement1(self): 
   print(self.name, 'from execute 1')

def execute_replacement2(self):
   print(self.name, 'from execute 2')

if __name__ == '__main__':
   context1 = Strategy()
   context2 = Strategy(execute_replacement1)
   context3 = Strategy(execute_replacement2)
   context1.execute()
   context2.execute()
   context3.execute()

"""
OUTPUT:
Strategy Example 0
Strategy Example 0 from execute 1
Strategy Example 0 from execute 2
[Finished in 0.1s]
"""