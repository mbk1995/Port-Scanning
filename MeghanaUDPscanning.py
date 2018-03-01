# Author: Meghana Kanaji
from scapy.all import*
portnumber =  range(0,101)
openport= []
closedport= []
openfiltered=[]
filteredport= []

for port in portnumber:
	conf.verb=0	
	source = RandShort()
	udppacket = sr1(IP(dst = "10.10.111.1")/UDP(sport= source, dport =port),timeout=10)
	if str(type(udppacket))=="<type 'NoneType'>":
		openfiltered.append(port)
		
		print "port: ",port,":Open|Filtered"
	elif (udppacket.haslayer(UDP)):
		openport.append(port)
		print"port: ",port,": Open"	
	elif (udppacket.haslayer(ICMP)):
		if (int(udppacket.getlayer(ICMP).type) == 3 and int(udppacket.getlayer(ICMP).code) in [1, 2, 9, 10,13]):
			filteredport.append(port)
			print "port: ",port,": Filtered"
		elif (int(udppacket.getlayer(ICMP).type) == 3 and int(udppacket.getlayer(ICMP).code) == 3):
			closedport.append(port)


print "Number of open ports are: ", len(openport)
print "Open Ports:", openport
print "Number of open|flitered ports are: ", len(openfiltered)
print "Open|Filtered ports:", openfiltered
print "Number of closed ports are: ", len(closedport)
print "Closed port:", closedport
print "Number of filtered ports are: ", len(filteredport)
print "Filtered ports:", filteredport

