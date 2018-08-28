import logging
import logging.handlers
from devclass import NetworkDeviceIOS
from getpass import getpass
from util import read_devices_lista_CSV
from util import filtra_devices_list
from util import read_devices_filtra_CSV

logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler('main.log',maxBytes=2000000,backupCount=4)
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

logger.addHandler(handler)
print('TesteClass:')

equipamentos = read_devices_filtra_CSV('listaHost.csv','R','user',getpass("Digite a senha: "))
for equipamento in equipamentos:
	print("nome :"+ equipamento.name)
	equipamento.debug_devclass()
	equipamento.connect()
	print(equipamento.busca_mac('192.168.47.185'))
	equipamento.disconnect()

