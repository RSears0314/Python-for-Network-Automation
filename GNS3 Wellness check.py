#ssh wellness

import time #To add a more smooth experience
import netmiko #This allows for SSH
from netmiko import ConnectHandler

#Dictionaries for the Devices
cisco_7200_1 = {
    'device_type': 'cisco_ios',
    'host':   '198.1.1.1',
    'username': 'ron',
    'password': 'ron',
}

cisco_7200_2 = {
    'device_type': 'cisco_ios',
    'host':   '198.1.1.5',
    'username': 'ron',
    'password': 'ron',
}

#LIST OF ALL DEVICE IPS that will be pinged in checkping() function
deviceIP = ["198.1.1.14","198.1.1.10","198.1.1.5","198.1.1.9"] 

#Pings all devices to check for connectivity
def checkPing():
    for IP in deviceIP:
        output = net_connect.send_command('ping ' + IP)
        print(output)
        time.sleep(3)

#Verifies ospf neighbors 
def checkOSPF():
    print("\nVerifying osfp configuration\n")
    time.sleep(2)
    output = net_connect.send_command("show running-config | i ospf")
    print(output)
    output = net_connect.send_command("show ip ospf neighbor")
    print(output)
    
#############################################
print("\nChecking RouterOne\n")
net_connect = ConnectHandler(**cisco_7200_1)
checkPing()
checkOSPF()

print("\nChecking RouterTwo\n")
net_connect = ConnectHandler(**cisco_7200_2)
checkPing()
checkOSPF()

time.sleep(1)
print("\nDevice check is finished")
#############################################
