# Python-for-Network-Automation

This will be a repository for my Python/GNS3 lab. This lab will be maintained using Python 3 Scripts (using Netmiko).

# LAB TOPOLOGY:
2 Cisco 7200 Routers  
1 Cisco 3725 EtherSwitch  
3 PCS  

RouterOne: Cisco 7200  
Loop back 1    - 198.1.1 | Interface f0/0 - 198.1.1.13 | Interface f1/0 - 198.1.1.1 | Interface f2/0 - 198.1.1.9

RouterTwo: Cisco 7200  
Loop back 2    - 2.2.2.2 | Interface f0/0 - 198.1.1.2 | Interface f1/0 - 198.1.1.5

EtherSwitch: Cisco 3725  
Interface f0/0 - Connected to RouterTwo f1/0 | Interface f0/1 - Connected to PC eth0

Python PC: Linux: Interface eth0 - 198.1.1.6

OffsitePC: Interface eth0 - 198.1.1.10

PC1: Interface eth0 - 198.1.1.14

OSPF: RouterOne runs process 1 area 0. Is an ASBR | RouterTwo runs process 2 area 0. Is an ASBR.
