#!/usr/bin/env python
 
from netmiko import ConnectHandler
from getpass import getpass

# SSH username and password provided by user
username = raw_input('Enter your SSH username: ')
password = getpass()

# Sending multiple lines of config stored in a file 
with open('more_config') as f:
    commands_list = f.read().splitlines()

# Sending device ip's stored in a file 
with open('devices_list') as f:
    devices_list = f.read().splitlines()

# Iterate through device list and configure the devices 
for devices in devices_list:
    print 'Connecting to device ' + devices
    ip_address_of_device = devices
    
    # SSH Connection details
    nxos_device = {
        'device_type': 'cisco_nxos',
        'ip': ip_address_of_device, 
        'username': username,
        'password': password
    }
 
    net_connect = ConnectHandler(**nxos_device)
    output = net_connect.send_config_set(commands_list)
    print output