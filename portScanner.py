import socket
import subprocess
import sys
from datetime import datetime

subprocess.call("pip install pyfiglet", shell=True)
subprocess.call("clear", shell=True)

import pyfiglet

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

remoteServerIP = input("Entrer l\'IP d\'un serveur à scanner : ")

print("-" * 60)
print("Lancement du scan des ports de la machine " + remoteServerIP)
print("-" * 60)

t1 = datetime.now()

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}:    Ouvert".format(port))
        sock.close()

except KeyboardInterrupt:
    print("Vous avez appuyé sur Ctrl+C.")
    sys.exit()

except socket.error:
    print("Connexion impossible au serveur.")
    sys.exit()

t2 = datetime.now()

total = t2 - t1

print("Scan terminé en : {}".format(str(total)))
