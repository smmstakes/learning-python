from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agency: str, account_number: str, bank_balance: float = 0) -> None:
        self._agency = agency
        self._account_number = account_number
        self._bank_balance = bank_balance

    @abstractmethod
    def deposit(self, value: float):
        ...

    @abstractmethod
    def withdraw(self, value: float):
        ...

    @property
    def agency(self) -> str:
        return self._agency
    
    @agency.setter
    def agency(self, new_agency):
       self._agency = new_agency

    @property
    def account_number(self) -> str:
        return self._account_number
    
    @account_number.setter
    def account_number(self, new_account_number):
       self._account_number = new_account_number
    
    @property
    def bank_balance(self) -> float:
        return self._bank_balance
    
    @bank_balance.setter
    def bank_balance(self, new_bank_balance):
       self._bank_balance = new_bank_balance

    def show_bank_balance(self):
        print(f"Saldo atual: R$ {self.bank_balance:.2f}\n")

    def deposit(self, value: float):
        self.bank_balance += value

        print(f"Depósito de R$ {value:.2f} realizado com sucesso!")
        self.show_bank_balance()

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f"({self.agency!r}, {self.account_number!r}, {self.bank_balance!r})"
        return f"{class_name}{attrs}"


class ContaCorrente(Conta):
    def __init__(self, agency: str, account_number: str, bank_balance: float = 0, limit: float = 0) -> None:
        super().__init__(agency, account_number, bank_balance)
        self.__limit = -limit

    def withdraw(self, value: float):
        calc = self.bank_balance - value
        if calc >= self.__limit:
            self.bank_balance = calc

            print(f"Saque de R$ {value:.2f} realizado com sucesso!")
            self.show_bank_balance()
            return
        
        print(f"Impossível sacar! Limite máximo de R$ {self.__limit:.2f} ultrapassado "
              f"em R$ {self.__limit - calc:.2f} \n")
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agency!r}, {self.account_number!r}, '\
            f'{self.bank_balance!r}, {self.__limit!r})'
        return f"{class_name}{attrs}"


class ContaPoupanca(Conta):
    def __init__(self, agency: str, account_number: str, bank_balance: float = 0) -> None:
        super().__init__(agency, account_number, bank_balance)
        self.__limit = 0

    def withdraw(self, value: float):
        calc = self.bank_balance - value
        if calc >= self.__limit:
            self.bank_balance = calc

            print(f"Saque de R$ {value:.2f} realizado com sucesso!")
            self.show_bank_balance()
            return
        
        print(f"Impossível sacar! A conta ficará negativada em "
              f"R$ {self.__limit - calc:.2f} \n")


if __name__ == "__main__":
    cp1 = ContaPoupanca("abc", "0123", 12)
    # print(cp1)
    cp1.deposit(13)
    cp1.withdraw(26)

    print("==="*20, end="\n\n")

    cc1 = ContaCorrente("bcd", "0124", limit=100)
    cc1.deposit(12.24)
    cc1.withdraw(12)
    
