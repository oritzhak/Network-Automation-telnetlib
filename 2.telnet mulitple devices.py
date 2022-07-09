# This script connecting to switches device using telnet and creating vlans

import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ") #ask username to connect
password = getpass.getpass() # enter password

f = ['192.168.122.72', '192.168.122.82', '192.168.122.83', '192.168.122.84', '192.168.122.85']
#ip`s of the devices

for IP in f:
    IP=IP.strip()
    print ("Configuring Switch " + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST) # connect to the device with telnet. (not recommended)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('ascii') + b"\n")
   
   #writing those configurations commands
    tn.write(b"conf t\n") 
    tn.write(b"vlan 2\n")
    tn.write(b"name Python_VLAN_2\n")
    tn.write(b"exit\n")
    tn.write(b"vlan 3\n")
    tn.write(b"name Python_VLAN_3\n")
    tn.write(b"exit\n")
    tn.write(b"vlan 4\n")
    tn.write(b"name Python_VLAN_4\n")
    tn.write(b"exit\n")
    tn.write(b"vlan 5\n")
    tn.write(b"name Python_VLAN_5\n")
    tn.write(b"exit\n")
    tn.write(b"vlan 6\n")
    tn.write(b"name Python_VLAN_6\n")
    tn.write(b"vlan 7\n")
    tn.write(b"name Python_VLAN_7\n")
    tn.write(b"vlan 8\n")
    tn.write(b"name Python_VLAN_8\n")
    tn.write(b"end\n")
    tn.write(b"wr\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii')) 
