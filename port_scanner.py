import socket

def port_scanner(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")
        sock.close()

# Example: Scan localhost common ports
target_ip = "127.0.0.1"
common_ports = [22, 80, 443, 8080]
port_scanner(target_ip, common_ports)
