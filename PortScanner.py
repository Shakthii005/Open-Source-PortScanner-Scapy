from scapy.all import sr1, IP, ICMP, TCP
import time

with open ("dead_hosts.txt", "r") as file:
    alive_hosts = [line.strip() for line in file.readlines()]

ports_to_scan = [22, 80, 443]

scan_results = open("port_scan_results.txt", "w")
print("Starting port scan... ")

for host in alive_hosts:
    print(f"Scanning host: {host}")
    scan_results.write(f"Host: {host}\n")
   
    for port in ports_to_scan:
        packet = IP(dst=host)/TCP(dport=port, flags='S')
        reply = sr1(packet, timeout=1, verbose=0)

        if reply:
            if reply.haslayer(TCP):
                tcp_layer = reply.getlayer(TCP)
                if tcp_layer.flags == 0x12: 
                    print(f"Port {port} is open on {host}")
                    scan_results.write(f"Port {port} is open\n")
                    rst_packet = IP(dst=host)/TCP(dport=port, flags='R')
                    sr1(rst_packet, timeout=1, verbose=0)
                elif tcp_layer.flags == 0x14:  
                    print(f"Port {port} is closed on {host}")
                    scan_results.write(f"Port {port} is closed\n")
            else:
                print(f"Port {port}: No tcp layer is detected")
                scan_results.write(f"Port {port}: No tcp layer is detected Unknown Response\n")
        else:
            print(f"Port {port} is Filtered (no reply)\n")
            scan_results.write(f"Port {port} is Filtered (no reply)\n")
            time.sleep(0.2) 

scan_results.close()
print("\nPort Scan Complete! Results saved in port_scan_results.txt")               
