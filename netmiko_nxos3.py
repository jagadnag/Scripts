#!/usr/bin/env python
 
from netmiko import ConnectHandler

# Sending multiple lines of config stored in a file 
with open('basic_config') as f:
    commands_to_send = f.read().splitlines()

# SSH Connection details 
nxos1 = {
    'device_type': 'cisco_nxos',
    'ip': '198.18.134.140',
    'username': 'admin',
    'password': 'C1sco12345',
}
 
all_devices = [nxos1]

# Iterate through device list and configure the devices  
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(commands_to_send)
    print output