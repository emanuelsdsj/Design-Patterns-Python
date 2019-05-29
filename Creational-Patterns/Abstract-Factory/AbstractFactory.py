"""
Abstract Factory:
The Abstract Factory defines a Factory Method per product. Each Factory Method encapsulates the new operator 
and the concrete, platform-specific, product classes. Each "platform" is then modeled with a Factory derived class.

Problem:
If an application is to be portable, it needs to encapsulate platform dependencies. These "platforms" 
might include: windowing system, operating system, database, etc. Too often, this encapsulation is not engineered 
in advance, and lots of #ifdef case statements with options for all currently supported platforms begin to procreate 
like rabbits throughout the code.

*References:
https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_abstract_factory.htm
https://sourcemaking.com/design_patterns/abstract_factory
"""

class Product:
   origin = ""
   component = ""

   def __init__(self, origin, component):
      self.origin = origin
      self.component = component
   
   def getOrigin(self):
      return self.origin
   
   def startComponent(self):
      return self.component

class AtmaXProduct(Product):
   def __init__(self):
      Product.__init__(self, "Atma", "X")

class AtmaYProduct(Product):
   def __init__(self):
      Product.__init__(self, "Atma", "Y")

class AtmaZProduct(Product):
   def __init__(self):
      Product.__init__(self, "Atma", "Z")

class UltimaXProduct(Product):
   def __init__(self):
      Product.__init__(self, "Ultima", "X")

class UltimaYProduct(Product):
   def __init__(self):
      Product.__init__(self, "Ultima", "Y")

class UltimaZProduct(Product):
   def __init__(self):
      Product.__init__(self, "Ultima", "Z")

# Abstract factory class
class IAbstractFactory:
   def getX(self): pass
   def getY(self): pass
   def getZ(self): pass

class AtmaFactory(IAbstractFactory):
   def getX(self):
      return AtmaXProduct()
   def getY(self):
      return AtmaYProduct()
   def getZ(self):
      return AtmaZProduct()

class UltimaFactory(IAbstractFactory):
   def getX(self):
      return UltimaXProduct()
   def getY(self):
      return UltimaYProduct()
   def getZ(self):
      return UltimaZProduct()

if __name__ == "__main__":
   product1 = AtmaFactory()
   product2 = UltimaFactory()

   componentXP1 = product1.getX()
   componentYP1 = product1.getY()
   componentZP1 = product1.getZ()

   componentXP2 = product2.getX()
   componentYP2 = product2.getY()
   componentZP2 = product2.getZ()
   
   print("--- Product 1 ---")
   print("Start component", componentXP1.startComponent(), " from origin", componentXP1.getOrigin())
   print("Start component", componentYP1.startComponent(), " from origin", componentYP1.getOrigin())
   print("Start component", componentZP1.startComponent(), " from origin", componentZP1.getOrigin())

   print("--- Product 2 ---")
   print("Start component", componentXP2.startComponent(), " from origin", componentXP2.getOrigin())
   print("Start component", componentYP2.startComponent(), " from origin", componentYP2.getOrigin())
   print("Start component", componentZP2.startComponent(), " from origin", componentZP2.getOrigin())

"""
OUTPUT:
--- Product 1 ---
Start component X  from origin Atma
Start component Y  from origin Atma
Start component Z  from origin Atma
--- Product 2 ---
Start component X  from origin Ultima
Start component Y  from origin Ultima
Start component Z  from origin Ultima
[Finished in 0.1s]
"""