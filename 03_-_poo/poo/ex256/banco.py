from abc import ABC, abstractmethod
from clientes import Cliente
from contas import Conta, ContaCorrente

class Banco():
    def __init__(
            self, 
            agencies: list[str] = None, 
            accounts: list[Conta] = None, 
            clients: list[Cliente] = None
            ) -> None:
    
        self._agencies = agencies or []
        self._accounts = accounts or []
        self._clients = clients or []
    
    def _check_agency(self, client: Cliente):
        if client.account.agency not in self._agencies:
            return False
        return True
    
    def _check_account_number(self, client: Cliente):
        if client.account.account_number not in self._accounts:
            return False
        return True
    
    def _check_client(self, client: Cliente):
        if client not in self._clients:
            return False
        return True

    def authenticate(self, client: Cliente) -> bool:
        if self._check_agency(client) and \
            self._check_account_number(client) and \
            self._check_client(client):
            return True
        
        return False
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f"({self._agencies!r}, {self._accounts!r}, {self._clients!r})"
        return f"{class_name}{attrs}"


if __name__ == "__main__":
    c1 = Cliente("Matheus", 21, ContaCorrente("123", "0123", 0))
    b1 = Banco()

    b1._agencies.extend(["123", "234"])
    b1._accounts.extend(["0123", "0124"])
    b1._clients.extend([c1])

    if b1.authenticate(c1):
        c1.account.deposit(250)
        c1.account.withdraw(290)