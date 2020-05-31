#!/usr/bin/env python3

def connect(ipaddress, ports):
    print("IP: ", ipaddress)
    print("Port: ", ports)
    #create a local variable, rather than change the value of ipaddress
    ipaddress = '10.10.10.1'
    #change the value of list ports, and use append() to add an element into the list
    ports.append(8080)

if __name__ == '__main__':
    ipaddress = '192.168.1.1'
    ports = [22, 23, 24]
    print("Before connect: ")
    print("IP: ", ipaddress)
    print("Ports: ", ports)
    print("In connect: ")
    connect(ipaddress, ports)
    print("After connect: ")
    print("IP: ", ipaddress)
    print("Ports: ", ports)

