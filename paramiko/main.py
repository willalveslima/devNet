from cliente_ssh import Cliente_ssh
from getpass import getpass

host = Cliente_ssh('172.29.121.27','f9839345', getpass('Senha: '))
host.connect()
print(host.exec_cmd('get system status'))
