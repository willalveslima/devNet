import logging
from netmiko import ConnectHandler

logger = logging.getLogger('main.devclass')

#log advanced
#---- Class to hold information about a generic network device --------
class NetworkDevice():

    def __init__(self, name, ip, user='cisco', pw='cisco'):
        self.name = name
        self.ip_address = ip
        self.username = user
        self.password = pw

    def connect(self):
        self.session = None

    def get_interfaces(self):
        self.interfaces = '--- Base Device, does not know how to get interfaces ---'

#==== Class to hold information about an IOS network device ========================
class NetworkDeviceIOS(NetworkDevice):

    #---------------------------------------------------------------------------
	def __init__(self, name, ip, user='cisco', pw='cisco', secret=''):
		NetworkDevice.__init__(self, name, ip, user, pw)
		self.secret = secret
		self.device = {
			'device_type': 'cisco_ios',
			'ip': self.ip_address,
			'username': self.username,
			'password': self.password,
			'secret': self.secret,
			'port': 22,
		}		
		self.session = None
		logger.info('devclass: created IOS device: %s %s', name, ip)

#---------------------------------------------------------------------------
	def connect(self):
		try:
			print('--- connecting IOS: telnet: '+self.ip_address+' for: '+self.username)
			self.session = ConnectHandler(**self.device)
			logger.info('devclass: successful login at: %s for user: %s',
                                                        self.ip_address,self.username)
			return self.session
		except Exception as err:
			logger.error('devclass: Erro no login at: %s for user: %s',
                                                        self.ip_address,self.username)
			print('Ocorreu um Erro: ' +str(err))
			raise Exception('Erro em devclass.connect')
			
			
#---------------------------------------------------------------------------
	def disconnect(self):
		if self.esta_connectado():
			print('--- disconnecting IOS: telnet: '+self.ip_address+' for: '+self.username)
			self.session.disconnect() 
			logger.info('devclass: successful logoff at: %s for user: %s',
                                                      self.ip_address,self.username)
		else:
			logger.warn('devclass: --- Erro ao desconectar.')
			print("Não há sessão para desconectar!")
	
#---------------------------------------------------------------------------
	def get_interfaces(self):
		if self.esta_connectado():
			self.interfaces = self.session.send_command("show int status")
			logger.info('devclass: successful get_interfaces at: %s for user: %s',
                                                      self.ip_address,self.username)
			return self.interfaces
		else:
			logger.error('devclass: Erro ao executar devclass.get_interfaces() - Sessão não estabelecida. at: %s for user: %s',
                                                        self.ip_address,self.username)
			raise Exception('Erro ao executar devclass.get_interfaces() - Sessao nao estabelecida.') 
			return "Erro "
#---------------------------------------------------------------------------
	def get_int_connected(self):
		if self.esta_connectado():
			output = self.session.send_command("show int status | i cted")
			logger.info('devclass: successful get_int_connected at: %s for user: %s',
                                                      self.ip_address,self.username)
			return output
		else:
			logger.error('devclass: Erro ao executar devclass.get_int_connected() - Sessão não estabelecida. at: %s for user: %s',
                                                        self.ip_address,self.username)
			raise Exception('Erro ao executar devclass.get_int_connected() - Sessao nao estabelecida.') 
			return "erro"

#---------------------------------------------------------------------------
	def do_wr(self):
		if self.esta_connectado():
			output = self.session.send_command('write memory')
			logger.info('devclass: successful do_wr at: %s for user: %s',
                                                      self.ip_address,self.username)
			return output
		else:
			logger.error('devclass: Erro ao executar devclass.do_wr() - Sessão não estabelecida. at: %s for user: %s',
                                                        self.ip_address,self.username)
			raise Exception('Erro ao executar devclass.do_wr() - Sessao nao estabelecida.') 
#---------------------------------------------------------------------------
	def config_mode(self):
		if self.esta_connectado():
			output = self.session.config_mode()
			logger.info('devclass: successful config_mode() at: %s for user: %s',
                                                      self.ip_address,self.username)
			return output
		else:
			logger.error('devclass: Erro ao executar devclass.config_mode() - Sessão não estabelecida. at: %s for user: %s',
                                                        self.ip_address,self.username)
			raise Exception('Erro ao executar devclass.config_mode() - Sessao nao estabelecida.') 
#---------------------------------------------------------------------------
	def exit_config_mode(self):
		if self.esta_connectado():
			output = self.sessionc.exit_config_mode()
			logger.info('devclass: successful exit_config_mode() at: %s for user: %s',
                                                      self.ip_address,self.username)
			return output
		else:
			logger.error('devclass: Erro ao executar devclass.exit_config_mode() - Sessão não estabelecida. at: %s for user: %s',
                                                        self.ip_address,self.username)
			raise Exception('Erro ao executar devclass.exit_config_mode() - Sessao nao estabelecida.') 
#---------------------------------------------------------------------------
	def check_config_mode(self):
		if self.esta_connectado():
			output = self.session.check_config_mode()
			logger.info('devclass: successful check_config_mode() at: %s for user: %s',
                                                      self.ip_address,self.username)
			return output
		else:
			logger.error('devclass: Erro ao executar devclass.check_config_mode() - Sessão não estabelecida. at: %s for user: %s',
                                                        self.ip_address,self.username)
			raise Exception('Erro ao executar devclass.check_config_mode() - Sessao nao estabelecida.') 
#---------------------------------------------------------------------------
	def enable(self):
		if self.esta_connectado():
			output = self.session.enable()
			logger.info('devclass: successful enable() at: %s for user: %s',
                                                      self.ip_address,self.username)
			return output
		else:
			logger.error('devclass: Erro ao executar devclass.enable() - Sessão não estabelecida. at: %s for user: %s',
                                                        self.ip_address,self.username)
			raise Exception('Erro ao executar devclass.enable() - Sessao nao estabelecida.') 
#---------------------------------------------------------------------------
	def exit_enable_mode(self):
		if self.esta_connectado():
			output = self.session.exit_enable_mode()
			logger.info('devclass: successful exit_enable_mode() at: %s for user: %s',
                                                      self.ip_address,self.username)
			return output
		else:
			logger.error('devclass: Erro ao executar devclass.exit_enable_mode() - Sessão não estabelecida. at: %s for user: %s',
                                                        self.ip_address,self.username)
			raise Exception('Erro ao executar devclass.exit_enable_mode() - Sessao nao estabelecida.') 
#---------------------------------------------------------------------------
	def find_prompt(self):
		if self.esta_connectado():
			output = self.session.find_prompt()
			logger.info('devclass: successful find_prompt() at: %s for user: %s',
                                                      self.ip_address,self.username)
			return output
		else:
			logger.error('devclass: Erro ao executar devclass.find_prompt() - Sessão não estabelecida. at: %s for user: %s',
                                                        self.ip_address,self.username)
			raise Exception('Erro ao executar devclass.find_prompt() - Sessao nao estabelecida.') 
#---------------------------------------------------------------------------
	def send_command(self,arguments):
		if self.esta_connectado():
			output = self.session.send_command(arguments)
			logger.info('devclass: successful send_command() at: %s for user: %s',
                                                      self.ip_address,self.username)
			return output
		else:
			logger.error('devclass: Erro ao executar devclass.send_command() - Sessão não estabelecida. at: %s for user: %s',
                                                        self.ip_address,self.username)
			raise Exception('Erro ao executar devclass.send_command() - Sessao nao estabelecida.')
#---------------------------------------------------------------------------
	def send_config_set(self,arguments_list):
		if self.esta_connectado():
			output = self.session.send_config_set(arguments_list)
			logger.info('devclass: successful send_config_set() at: %s for user: %s',
                                                      self.ip_address,self.username)
			return output
		else:
			logger.error('devclass: Erro ao executar devclass.send_config_set() - Sessão não estabelecida. at: %s for user: %s',
                                                        self.ip_address,self.username)
			raise Exception('Erro ao executar devclass.send_config_set() - Sessao nao estabelecida.')
#---------------------------------------------------------------------------
	def send_config_from_file(self,file):
		if self.esta_connectado():
			output = self.session.send_config_from_file(file)
			logger.info('devclass: successful send_config_from_file() at: %s for user: %s',
                                                      self.ip_address,self.username)
			return output
		else:
			logger.error('devclass: Erro ao executar devclass.send_config_from_file() - Sessão não estabelecida. at: %s for user: %s',
                                                        self.ip_address,self.username)
			raise Exception('Erro ao executar devclass.send_config_from_file() - Sessao nao estabelecida.')
#---------------------------------------------------------------------------			
	def esta_connectado(self):
		if self.session != None:
			return True
		else:
			return False
#---------------------------------------------------------------------------
	def debug_devclass(self):
		filename_log = self.ip_address+'_.log'
		logging.basicConfig(filename=filename_log,format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
		debugClass = logging.getLogger("netmiko")
#---------------------------------------------------------------------------		
	def get_hostname(self):
		if self.esta_connectado():
			output = self.session.send_command("show conf | i hostname")
			logger.info('devclass: successful get_hostname at: %s for user: %s',
                                                      self.ip_address,self.username)
			hostname = (output.split())[1]
			return hostname
		else:
			logger.error('devclass: Erro ao executar devclass.get_hostname() - Sessão não estabelecida. at: %s for user: %s',
                                                        self.ip_address,self.username)
			raise Exception('Erro ao executar devclass.get_hostname() - Sessao nao estabelecida.') 
			return "Erro "
#---------------------------------------------------------------------------	
	def get_nbem(self):
		if self.esta_connectado():
			output = self.session.send_command("show run | i chassis")
			logger.info('devclass: successful get_nbem at: %s for user: %s',
                                                      self.ip_address,self.username)
			output = (output.split())[2]
			return output
		else:
			logger.error('devclass: Erro ao executar devclass.get_nbem() - Sessão não estabelecida. at: %s for user: %s',
                                                        self.ip_address,self.username)
			raise Exception('Erro ao executar devclass.get_nbem() - Sessao nao estabelecida.') 
	#---------------------------------------------------------------------------	
	def get_serial(self):
		if self.esta_connectado():
			output = self.session.send_command("show version | i System [s,S]erial")
			logger.info('devclass: successful get_serial at: %s for user: %s',
                                                      self.ip_address,self.username)
			outputlines = output.splitlines()
			serial =[]
			for line in outputlines:
				serial.append((line.split(": "))[1])
			return serial 
		else:
			logger.error('devclass: Erro ao executar devclass.get_serial() - Sessão não estabelecida. at: %s for user: %s',
                                                        self.ip_address,self.username)
			raise Exception('Erro ao executar devclass.get_serial() - Sessao nao estabelecida.') 
#---------------------------------------------------------------------------	
#retorna o MAC pelo IP 
	def busca_mac(self,end_ip):
		if self.esta_connectado():
			output = self.session.send_command("show arp | i %s"%end_ip)
			logger.info('devclass: successful busca_mac at: %s for user: %s',
                                                      self.ip_address,self.username)
			#output = (output.split())[2]
			return output
		else:
			logger.error('devclass: Erro ao executar devclass.busca_mac() - Sessão não estabelecida. at: %s for user: %s',
                                                        self.ip_address,self.username)
			raise Exception('Erro ao executar devclass.busca_mac() - Sessao nao estabelecida.') 
	#---------------------------------------------------------------------------	