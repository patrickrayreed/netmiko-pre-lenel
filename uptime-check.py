
from netmiko import ConnectHandler
import csv

#ENABLE THIS LOGGING IF YOU NEED TO TSHOOT
#import logging
#logging.basicConfig(filename='test.log', level=logging.DEBUG)
#logger = logging.getLogger("netmiko")


username = 'local-tech'

# Defines Function to Return a dictionary to pass parameters to netmiko
def sw_add(switch, username, password):
    return {'device_type': 'cisco_ios',
            'host': switch,
            'username': username,
            'password': password,
            'secret': password,
            'timeout': 5000.0,
            'session_timeout': 10000.0,
            'session_log_file_mode': 'append',
            'session_log': 'switch.txt', }

# Reads CSV columns containing hostname,password data
with open('reload-test-sw1-2.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        switch_list = []
        for row in csv_reader:
            if not row['Password']:
                pass
            else:
                switch_list.append(sw_add(row['Switch'], username, row['Password']))
        switch = (row['Switch'])
        password = (row['Password'])


for X in switch_list:
    net_connect = ConnectHandler(**X)

# Execute show commands.

    output = net_connect.send_command('show ver | i uptime')
    print(output)