"""
Observer:
The Observer defines a one-to-many relationship so that when one object changes state, 
the others are notified and updated automatically. Some auctions demonstrate this pattern. 
Each bidder possesses a numbered paddle that is used to indicate a bid. The auctioneer starts the 
bidding, and "observes" when a paddle is raised to accept the bid. The acceptance of the bid changes 
the bid price which is broadcast to all of the bidders in the form of a new bid.

Problem:
A large monolithic design does not scale well as new graphing or monitoring requirements are levied.

*References:
https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_observer.htm
https://sourcemaking.com/design_patterns/observer
"""

import abc

class Subject:
    """
    Know its observers. Any number of Observer objects may observe a
    subject.
    Send a notification to its observers when its state changes.
    """

    def __init__(self):
        self._observers = set()
        self._subject_state = None

    def attach(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self._subject_state)

    @property
    def subject_state(self):
        return self._subject_state

    @subject_state.setter
    def subject_state(self, arg):
        self._subject_state = arg
        self._notify()


class Observer(metaclass=abc.ABCMeta):
    """
    Define an updating interface for objects that should be notified of
    changes in a subject.
    """

    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abc.abstractmethod
    def update(self, arg):
        pass


class ConcreteObserver1(Observer):
    """
    Implement the Observer updating interface to keep its state
    consistent with the subject's.
    Store state that should stay consistent with the subject's.
    """

    def update(self, arg):
        self._observer_state = arg
        print("ConcreteObserver1 - updated")

class ConcreteObserver2(Observer):
    """
    Implement the Observer updating interface to keep its state
    consistent with the subject's.
    Store state that should stay consistent with the subject's.
    """

    def update(self, arg):
        self._observer_state = arg
        print("ConcreteObserver2 - updated")


def main():
    subject = Subject()
    concrete_observer1 = ConcreteObserver1()
    concrete_observer2 = ConcreteObserver2()
    subject.attach(concrete_observer1)
    subject.attach(concrete_observer2)
    subject.subject_state = 123


if __name__ == "__main__":
    main()

"""
OUTPUT:
ConcreteObserver1 - updated
ConcreteObserver2 - updated
[Finished in 0.1s]
"""