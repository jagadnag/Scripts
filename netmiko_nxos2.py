#!/usr/bin/env python
from netmiko import ConnectHandler

# SSH Connection Details
nxos1 = {
    'device_type': 'cisco_nxos',
    'ip': '198.18.134.140',
    'username': 'admin',
    'password': 'C1sco12345',
}

# Establish SSH to device and run config command
net_connect = ConnectHandler(**nxos1)
output = net_connect.send_config_set('logging server 1.1.1.1')
print output