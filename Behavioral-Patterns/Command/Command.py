"""
Command:
The Command pattern allows requests to be encapsulated as objects, thereby allowing clients to be parametrized 
with different requests. The "check" at a diner is an example of a Command pattern. The waiter or waitress 
takes an order or command from a customer and encapsulates that order by writing it on the check. The order 
is then queued for a short order cook. Note that the pad of "checks" used by each waiter is not dependent on 
the menu, and therefore they can support commands to cook many different items.

Problem:
Need to issue requests to objects without knowing anything about the operation being requested or the receiver 
of the request.,

*References:
https://sourcemaking.com/design_patterns/command/python/1
https://sourcemaking.com/design_patterns/command
"""

import abc

class Invoker:
    """
    Ask the command to carry out the request.
    """

    def __init__(self):
        self._commands = []
        self.pos = 0

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()
    def redo(self):
    	if self.pos == len(self._commands) - 1:
    		self._commands[self.pos].execute()
    	else:
    		self.pos += 1
    		self._commands[self.pos].execute()
    def undo(self):
   		if self.pos == 0:
   			self._commands[self.pos].execute()
   		else:
   			self.pos -= 1
   			self._commands[self.pos].execute()


class Command(metaclass=abc.ABCMeta):
    """
    Declare an interface for executing an operation.
    """

    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    """
    Define a binding between a Receiver object and an action.
    Implement Execute by invoking the corresponding operation(s) on
    Receiver.
    """

    def execute(self):
        self._receiver.action()


class Receiver1:
    """
    Know how to perform the operations associated with carrying out a
    request. Any class may serve as a Receiver.
    """

    def action(self):
        print("Receiver 1 Action")

class Receiver2:
    """
    Know how to perform the operations associated with carrying out a
    request. Any class may serve as a Receiver.
    """

    def action(self):
        print("Receiver 2 Action")

class Receiver3:
    """
    Know how to perform the operations associated with carrying out a
    request. Any class may serve as a Receiver.
    """

    def action(self):
        print("Receiver 3 Action")


def main():
    receiver1 = Receiver1()
    receiver2 = Receiver2()
    receiver3 = Receiver3()
    concrete_command1 = ConcreteCommand(receiver1)
    concrete_command2 = ConcreteCommand(receiver2)
    concrete_command3 = ConcreteCommand(receiver3)

    invoker = Invoker()
    invoker.store_command(concrete_command1)
    invoker.store_command(concrete_command2)
    invoker.store_command(concrete_command3)

    invoker.redo() # 2
    invoker.redo() # 3
    invoker.redo() # 3
    invoker.undo() # 2
    invoker.undo() # 1
    invoker.undo() # 1
    print("ALL COMMANDS: ")
    invoker.execute_commands()


if __name__ == "__main__":
    main()

"""
OUTPUT:
Receiver 2 Action
Receiver 3 Action
Receiver 3 Action
Receiver 2 Action
Receiver 1 Action
Receiver 1 Action
ALL COMMANDS: 
Receiver 1 Action
Receiver 2 Action
Receiver 3 Action
[Finished in 0.1s]
"""