# Scripts
CLUS 2018 WISP LAB Scripts


Notes:

interface Ethernet1/1
  description to nx-osv3
  no switchport
  ip address 192.168.1.1/24
  ip ospf network point-to-point
  ip router ospf 1 area 0.0.0.0
  no shutdown

interface Ethernet1/1
  description to nx-osv1
  no switchport
  ip address 192.168.1.3/24
  ip ospf network point-to-point
  ip router ospf 1 area 0.0.0.0
  no shutdown

https://github.com/jagadnag/Scripts

C:\Users\demouser\Desktop\Scripts\

http://ttyplus.com/downloads.html
https://pip.pypa.io/en/stable/installing/
http://cmder.net/
