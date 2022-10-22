
class Conta:
    def __init__(self, numero, titular, saldo):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
    
class Poupanca(Conta):
    def __init__(self, numero, titular, saldo):
        super().__init__(numero, titular, saldo)

class Corrente(Conta):
    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo)
        self._limite=limite