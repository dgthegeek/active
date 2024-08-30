import socket

# Adresse et port à occuper
HOST = '127.0.0.1'  # Adresse IP locale
PORT = 12345        # Port à occuper

# Création d'un socket UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Listening on UDP {HOST}:{PORT}...")

    while True:
        # Attendre les données du client
        data, addr = s.recvfrom(1024)
        print(f"Received from {addr}: {data}")
        # Optionnel : Répondre au client
        s.sendto(b"Received your message", addr)
