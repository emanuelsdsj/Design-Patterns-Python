"""
Adapter:
The Adapter pattern allows otherwise incompatible classes to work together by converting the interface 
of one class into an interface expected by the clients.

Problem:
An "off the shelf" component offers compelling functionality that you would like to reuse, but its "view of the world" 
is not compatible with the philosophy and architecture of the system currently being developed.

*References:
https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_adapter.htm
https://sourcemaking.com/design_patterns/adapter
"""

class EuropeanSocketInterface:
	def voltage(self): pass

	def live(self): pass
	def neutral(self): pass
	def earth(self): pass

# Adaptee
class Socket(EuropeanSocketInterface):
	def voltage(self):
		return 230

	def live(self):
		return 1

	def neutral(self):
		return -1

	def earth(self):
		return 0

# Target interface
class USASocketInterface:
   def voltage(self): pass
   def live(self): pass
   def neutral(self): pass

# The Adapter
class Adapter(USASocketInterface):
   __socket = None
   def __init__(self, socket):
      self.__socket = socket
   
   def voltage(self):
      return 110
   
   def live(self):
      return self.__socket.live()
   
   def neutral(self):
      return self.__socket.neutral()

# Client
class ElectricKettle:
	__power = None

	def __init__(self, power):
	   self.__power = power

	def boil(self):
		if self.__power.voltage() > 110:
			print("Kettle on fire!")
		elif self.__power.live() == 1 and self.__power.neutral() == -1:
			print("Coffee time!")
		else:
			print("No power.")

def main():
	# Plug in
	socket = Socket()
	adapter = Adapter(socket)
	kettle = ElectricKettle(adapter)

	# Make coffee
	kettle.boil()

	return 0
	
if __name__ == "__main__":
	main()

"""
OUTPUT:
Coffee time!
[Finished in 0.0s]
"""