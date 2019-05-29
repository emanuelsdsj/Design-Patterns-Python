"""
Factory Method:
The Factory Method defines an interface for creating objects, but lets subclasses decide which classes 
to instantiate. Injection molding presses demonstrate this pattern. Manufacturers of plastic toys process 
plastic molding powder, and inject the plastic into molds of the desired shapes. 
The class of toy (car, action figure, etc.) is determined by the mold.

Problem:
A framework needs to standardize the architectural model for a range of applications, but allow 
for individual applications to define their own domain objects and provide for their instantiation.

*References:
https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_factory.htm
https://sourcemaking.com/design_patterns/factory_method
"""

class Product1(object):
   construct = ""
   def startComponent(self):
      return self.construct

class Component1(Product1):
   construct = "Atma"

class Component2(Product1):
   construct = "Ultima"

class Component3(Product1):
   construct = "Emerald"

class Product1Factory():
   def create_component(self, typ):
      targetclass = typ.capitalize()
      return globals()[targetclass]()

component_obj = Product1Factory()
component = ["Component1", "Component2", "Component3"]
for b in component:
   print(component_obj.create_component(b).startComponent())

"""
OUTPUT:
Atma
Ultima
Emerald
[Finished in 0.1s]
"""