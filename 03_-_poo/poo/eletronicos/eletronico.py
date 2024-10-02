from log import LogPrintMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True
    
    def desligar(self):
        if self._ligado:
            self._ligado = False


class Smartphone(Eletronico):
    def __init__(self, nome):
        super().__init__(nome)
        self._log = LogPrintMixin() # Composição

    def ligar(self):
        super().ligar()
        self._log.log_sucess(f"{self._nome} ligou!")

    def desligar(self):
        super().desligar()
        self._log.log_sucess(f"{self._nome} desligou!")
