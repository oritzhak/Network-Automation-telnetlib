# this script connecting to the swithces in telnet, taking the configuration, writing in a files and saving the file. 
import getpass
import telnetlib

user = input('Enter your telnet username: ') #ask username to connect
password = getpass.getpass() # enter password

f = ['192.168.122.72', '192.168.122.82', '192.168.122.83', '192.168.122.84', '192.168.122.85'] 
#ip`s of the devices

for IP in f:
    IP=IP.strip()
    print ('Get running configurations from Switch ' + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST) # connect the device with telnet. (not recommended)
    tn.read_until(b'Username: ') 
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')  
    tn.write(b"terminal length 0\n") 
    tn.write(b"show run\n") #showing the entire configuration of the device
    tn.write(b'exit\n')

    readoutput = tn.read_all() # taking the output
    saveoutput =  open("switch" + HOST, "w") # creating a file 
    saveoutput.write(readoutput.decode('ascii')) # writing the configuration of the device in a file.
    saveoutput.write("\n") 
    saveoutput.close # close the file
