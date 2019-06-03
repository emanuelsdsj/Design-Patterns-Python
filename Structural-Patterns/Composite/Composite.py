"""
Composite:
The Composite composes objects into tree structures and lets clients treat individual objects and compositions 
uniformly. Although the example is abstract, arithmetic expressions are Composites. An arithmetic expression 
consists of an operand, an operator (+ - * /), and another operand. The operand can be a number, or another 
arithmetic expression. Thus, 2 + 3 and (2 + 3) + (4 * 6) are both valid expressions.

Problem:
Application needs to manipulate a hierarchical collection of "primitive" and "composite" objects. 
Processing of a primitive object is handled one way, and processing of a composite object is 
handled differently. Having to query the "type" of each object before attempting to process it is not desirable.

*References:
https://sourcemaking.com/design_patterns/composite/python/1
https://sourcemaking.com/design_patterns/composite
"""

import abc


class Component(metaclass=abc.ABCMeta):
    """
    Declare the interface for objects in the composition.
    Implement default behavior for the interface common to all classes,
    as appropriate.
    Declare an interface for accessing and managing its child
    components.
    Define an interface for accessing a component's parent in the
    recursive structure, and implement it if that's appropriate
    (optional).
    """

    @abc.abstractmethod
    def operation(self):
        pass


class Composite(Component):
    """
    Define behavior for components having children.
    Store child components.
    Implement child-related operations in the Component interface.
    """

    def __init__(self):
        self._children = set()

    def operation(self):
    	orderLeaf = ""
    	for child in self._children:
    		orderLeaf += child.operation() + "\n"
    	return orderLeaf

    def add(self, component):
        self._children.add(component)

    def remove(self, component):
        self._children.discard(component)


class Leaf1(Component):
    """
    Represent leaf objects in the composition. A leaf has no children.
    Define behavior for primitive objects in the composition.
    """

    def operation(self):
        return "Leaf 1 - Operation"

class Leaf2(Component):
    """
    Represent leaf objects in the composition. A leaf has no children.
    Define behavior for primitive objects in the composition.
    """

    def operation(self):
        return "Leaf 2 - Operation"

class Leaf3(Component):
    """
    Represent leaf objects in the composition. A leaf has no children.
    Define behavior for primitive objects in the composition.
    """

    def operation(self):
        return "Leaf 3 - Operation"

def main():
    leaf1 = Leaf1()
    leaf2 = Leaf2()
    leaf3 = Leaf3()
    composite = Composite()
    composite.add(leaf1)
    composite.add(leaf2)
    composite.add(leaf3)
    print(composite.operation())

if __name__ == "__main__":
    main()

"""
OUTPUT:
Leaf 2 - Operation
Leaf 3 - Operation
Leaf 1 - Operation

[Finished in 0.1s]
"""