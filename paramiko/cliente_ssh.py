from paramiko import SSHClient
import paramiko

class Cliente_ssh:
	def __init__(self, ip, user='cisco', pw='cisco'):
		self.ip_address = ip
		self.username = user
		self.password = pw
		self.ssh = SSHClient()
		self.ssh.load_system_host_keys()
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		
	def connect(self):
		self.ssh.connect(hostname=self.ip_address,username=self.username,password=self.password)
	def exec_cmd(self,cmd):
		stdin,stdout,stderr = self.ssh.exec_command(cmd)
		if stderr.channel.recv_exit_status() != 0:
			return stderr.read()
		else:
			return stdout.read()
	def close(self):
		self.ssh.close()
		