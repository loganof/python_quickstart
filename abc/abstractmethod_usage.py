"""
abc.abstractclassmethod has been deprecated since version 3.3
reference: https://docs.python.org/3/library/abc.html#abc.abstractclassmethod
"""

from abc import ABC, abstractmethod

class C(ABC):
    @classmethod
    @abstractmethod
    def my_abstract_classmethod(cls, arg):
        ...