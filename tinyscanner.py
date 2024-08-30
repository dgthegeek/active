import socket
import argparse

def scan_port_tcp(host, port):
    """Scans a TCP port to check if it is open."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)  # Timeout to avoid hanging on unresponsive ports
        result = sock.connect_ex((host, port))
        return result == 0  # Return True if the port is open

def scan_port_udp(host, port):
    """Scans a UDP port to check if it is open."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(1)
        try:
            sock.sendto(b"", (host, port))
            sock.recvfrom(1024)
            return True  # If we receive a response, the port is open
        except socket.error:
            return False

def get_service_name(port, protocol):
    """Returns the service name associated with a port and protocol."""
    try:
        return socket.getservbyport(port, protocol)
    except:
        return "Unknown service"

def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("host", help="Host to scan (e.g., 127.0.0.1)")
    parser.add_argument("-p", "--ports", help="Range of ports to scan (e.g., 80, 80-83)", required=True)
    parser.add_argument("-t", "--tcp", help="Use TCP scan", action="store_true")
    parser.add_argument("-u", "--udp", help="Use UDP scan", action="store_true")
    
    args = parser.parse_args()

    host = args.host
    ports = []
    
    # Parsing the port range provided by the user
    if '-' in args.ports:
        start_port, end_port = map(int, args.ports.split('-'))
        ports = range(start_port, end_port + 1)
    else:
        ports = [int(args.ports)]

    for port in ports:
        if args.tcp:
            is_open = scan_port_tcp(host, port)
            protocol = 'tcp'
        elif args.udp:
            is_open = scan_port_udp(host, port)
            protocol = 'udp'
        else:
            print("Please specify either TCP or UDP scan.")
            return

        if is_open:
            service_name = get_service_name(port, protocol)
            print(f"Port {port} is open (Service: {service_name})")
        else:
            print(f"Port {port} is closed")

if __name__ == "__main__":
    main()
