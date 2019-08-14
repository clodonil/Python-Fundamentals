class Conta:
    def __init__(self,nconta, titular, saldo, limite):
       print("Construindo objeto...")
       self._nconta = nconta
       self._titular = titular
       self._saldo = saldo
       self._limite = limite

    def deposito(self, valor):
       self.__saldo += valor

    def saque(self, valor):
       self.__saldo -= valor

    def extrato(self):
       print("Sr(a) {0} o Saldo eh {1}".format(self.__titular,self.__saldo))

    @property
    def saldo(self):
       return self.__saldo

    @property
    def titular(self):
       return self.__titular

    @property
    def limite(self):
       return self.__limite

    @limite.setter
    def limite(self, limite):
      self.__limite = limite

class Investimento(Conta):
    def __init__(self, nconta,titular, saldo, limite, juros):
      super().__init__(nconta, titular, saldo, limite)
      self.__juros = juros

    def redimento(self):
        self._saldo += (self._saldo * self.__juros)
        return self._saldo