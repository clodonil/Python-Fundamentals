class Conta:
    def __init__(self,nconta, titular, saldo, limite):
       print("Construindo objeto...")
       self.__nconta = nconta
       self.__titular = titular
       self.__saldo = saldo
       self.__limite = limite


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
    pass