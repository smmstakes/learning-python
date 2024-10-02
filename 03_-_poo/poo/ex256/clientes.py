from abc import ABC, abstractmethod
import contas

class Pessoa(ABC):
    def __init__(self, name: str , age: int) -> None:
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        self._age = new_age

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f"({self._name!r}, {self._age!r})"
        return f"{class_name}{attrs}"


class Cliente(Pessoa):
    def __init__(self, name: str , age: int, account: contas.Conta | None = None) -> None:
        super().__init__(name, age)
        self.account = account

    
if __name__ == "__main__":
    c1 = Cliente("Matheus", 21)
    # print(c1, c1.account)
    c1.account = contas.ContaCorrente("abc", "0123")
    # print(c1, c1.account)
