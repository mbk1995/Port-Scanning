from scapy.all import *
#Author: Meghana Kanaji
syn= 0x12
rst= 0x14
portnumbers=range(0,101)
openport= []
closedport =[]
filteredport =[]


for port in portnumbers:
		source=RandShort()
		conf.verb = 0
		synpacket= sr1(IP(dst = "10.10.111.1")/TCP(sport = source, dport = port , flags= 'S'))
		receivedflags = synpacket.getlayer(TCP).flags
		if receivedflags == syn:
		   openport.append(port)
		   print "port: ", port,": Open"
		elif 	(synpacket.haslayer(ICMP)):
			if (int(synpacket.getlayer(ICMP).type) == 3 and int(synpacket.getlayer(ICMP).code) in [0, 1, 2, 3, 9, 10,13]):
				filteredport.append(port)
				print "port: ",port,": Filtered"
	
		elif receivedflags == rst:
			closedport.append(port)
		send(IP(dst = "10.10.111.1")/TCP(sport= source, dport = port, flags = 'R'))

print "Number of Open ports are" , len(openport)
print "Open ports:", openport
print "Number of closed ports are", len(closedport)
print "Closed ports:", closedport
print "Number of filtered ports are", len(filteredport)
print "Filtered ports:", filteredport

