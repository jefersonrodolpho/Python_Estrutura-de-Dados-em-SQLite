import Classe

conta1 = Classe.Conta('Marcio', 2)
conta1.Depositar(200.00)
print(conta1.getCliente())

conta2 = Classe.Conta('Ana', 3)
conta2.Depositar(200.00)
print(conta2.getCliente())

conta1.Transferencia(conta2, 100)

print(conta1.Saldo())
print(conta2.Saldo())