#!/usr/bin/env python
 
from netmiko import ConnectHandler

# Sending multiple lines of config stored in a file 
with open('reset_config') as f:
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
        'username': 'admin',
        'password': 'C1sco12345'
    }
 
    net_connect = ConnectHandler(**nxos_device)
    output = net_connect.send_config_set(commands_list)
    print output