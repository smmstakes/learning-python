from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None           # Configura a propriedade 
        self.name = name            # Utiliza o setter

    @property
    @abstractmethod
    def name(self):
        ...

    @name.setter
    def name(self, new_name):
        ...

class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
foo = Foo("Bar")
print(foo.name)
