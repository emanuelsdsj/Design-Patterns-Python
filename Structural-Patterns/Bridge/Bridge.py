"""
Bridge:
The Bridge pattern decouples an abstraction from its implementation, so that the two can vary independently. 
A household switch controlling lights, ceiling fans, etc. is an example of the Bridge. The purpose of the switch 
is to turn a device on or off. The actual switch can be implemented as a pull chain, simple two position switch, or a 
variety of dimmer switches.

Problem:
"Hardening of the software arteries" has occurred by using subclassing of an abstract base class to provide 
alternative implementations. This locks in compile-time binding between interface and implementation. 
The abstraction and implementation cannot be independently extended or composed.

*References:
https://sourcemaking.com/design_patterns/bridge
https://sourcemaking.com/design_patterns/bridge/python/1
"""

import abc

class Abstraction:
    """
    Define the abstraction's interface.
    Maintain a reference to an object of type Implementor.
    """

    def __init__(self, imp):
        self._imp = imp

    def operation(self):
        return self._imp.operation_imp()


class Implementor(metaclass=abc.ABCMeta):
    """
    Define the interface for implementation classes. This interface
    doesn't have to correspond exactly to Abstraction's interface; in
    fact the two interfaces can be quite different. Typically the
    Implementor interface provides only primitive operations, and
    Abstraction defines higher-level operations based on these
    primitives.
    """

    @abc.abstractmethod
    def operation_imp(self):
        pass


class ConcreteImplementorA(Implementor):
    """
    Implement the Implementor interface and define its concrete
    implementation.
    """

    def operation_imp(self):
        return "Operation A"


class ConcreteImplementorB(Implementor):
    """
    Implement the Implementor interface and define its concrete
    implementation.
    """

    def operation_imp(self):
        return "Operation B"


def main():
    concrete_implementor_a = ConcreteImplementorA()
    concrete_implementor_b = ConcreteImplementorB()
    abstraction = Abstraction(concrete_implementor_a)
    print(abstraction.operation())
    abstraction = Abstraction(concrete_implementor_b)
    print(abstraction.operation())


if __name__ == "__main__":
    main()
"""
OUTPUT:
Operation A
Operation B
[Finished in 0.1s]
"""