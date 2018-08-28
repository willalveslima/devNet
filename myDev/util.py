#file: util.py

import csv
import json
from pprint import pprint

import sqlite3
import logging
import re
from time import strftime
from time import localtime
from time import sleep
from time import time

from devclass import NetworkDevice
from devclass import NetworkDeviceIOS

logger = logging.getLogger('main.util')

#=====================================================================
def read_devices_lista_CSV(devices_file,user,pw):
	logger.info('util: read_devices_lista_CSV  arquivo: %s', devices_file)
	devices_list = []
	try:
		file = open(devices_file,'r')   # Open the CSV file
		csv_devices = csv.reader(file)  # Create the CSV reader for file
	
		# Iterate through all devices in our CSV file
		for device_info in csv_devices:
			device = NetworkDeviceIOS(device_info[0],device_info[1],user,pw)
			devices_list.append(device)
		logger.info('util: successful read_devices_lista_CSV  arquivo: %s', devices_file)
		return devices_list
	except Exception as err:
			logger.error('util: read_devices_lista_CSV - Erro ao ler arquivo: %s', devices_file)
			print('Ocorreu um Erro: ' +str(err))
			raise Exception('Erro em util.read_devices_lista_CSV')
#=====================================================================       
def filtra_devices_list(devices_list,criterio):
	result_list =[]
	regex_criterio = r"\b(?=\w)" + re.escape(criterio) + r"\b(?!\w)"
	#regex_criterio = "r"+criterio
	for device in devices_list:
		if re.search(regex_criterio, device.name, re.IGNORECASE) is not None:
			result_list.append(device)
	return result_list
#=====================================================================
def read_devices_filtra_CSV(devices_file,criterio,user,pw):
	logger.info('util: read_devices_filtra_CSV  arquivo: %s', devices_file)
	devices_list = []
	regex_criterio = re.compile(r'%s'%criterio, re.IGNORECASE)
	logger.debug('util: read_devices_filtra_CSV regex: %s',regex_criterio)
	try:
		file = open(devices_file,'r')   # Open the CSV file
		csv_devices = csv.reader(file)  # Create the CSV reader for file
	
		# Iterate through all devices in our CSV file
		for device_info in csv_devices:
			if regex_criterio.search(device_info[0]) is not None:
				device = NetworkDeviceIOS(device_info[0],device_info[1],user,pw)
				devices_list.append(device)
		logger.info('util: successful read_devices_filtra_CSV  arquivo: %s', devices_file)
		return devices_list
	except Exception as err:
			logger.error('util: read_devices_filtra_CSV - Erro ao ler arquivo: %s', devices_file)
			print('Ocorreu um Erro: ' +str(err))
			raise Exception('Erro em util.read_devices_filtra_CSV')
#=====================================================================	






