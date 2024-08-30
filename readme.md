# TinyScanner

TinyScanner is a simple port scanner that checks if a port is open or closed. It supports both TCP and UDP scans and can optionally display the service name associated with the port.

## Installation

Ensure you have Python installed on your system. No additional libraries are required.

## Usage

```bash
$ python tinyscanner.py --help
Usage: tinyscanner.py [OPTIONS] [HOST]

Options:
  -p, --ports RANGE       Range of ports to scan (e.g., 80, 80-83)
  -t, --tcp               Use TCP scan
  -u, --udp               Use UDP scan
  --help                  Show this message and exit
```
#Examples
- Scan a single TCP port:
```bash
$ python tinyscanner.py 127.0.0.1 -t -p 80
Port 80 is open (Service: http)

```

- Scan a range of TCP ports:
```bash
$ python tinyscanner.py 127.0.0.1 -t -p 80-83
Port 80 is open (Service: http)
Port 81 is closed
Port 82 is closed
Port 83 is open (Service: http)
```

- Scan a single UDP port:
```bash
$ python tinyscanner.py 127.0.0.1 -u -p 53
Port 53 is open (Service: domain)

```


### Explication du Code

1. **Imports**: On utilise `socket` pour les opérations réseau et `argparse` pour gérer les arguments en ligne de commande.
2. **Fonctions `scan_port_tcp` et `scan_port_udp`**: Elles vérifient si un port TCP ou UDP est ouvert.
3. **Fonction `get_service_name`**: Cette fonction renvoie le nom du service lié à un port, en utilisant le protocole spécifié (TCP ou UDP).
4. **Fonction `main`**: Gère l'interface en ligne de commande, analyse les arguments, et effectue le scan des ports en fonction des options fournies.
5. **README.md**: Explique comment utiliser le programme avec des exemples concrets.

Tu peux utiliser ce code comme point de départ pour ton projet. Si tu as besoin de plus d'aide ou de précisions, n'hésite pas à demander !


# Notes

This tool is for educational purposes only. Ensure you have permission before scanning any network or host.