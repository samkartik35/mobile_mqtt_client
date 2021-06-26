import socket
import time



local_host="192.168.43.231" # RPi4 IP address
aws_host="15.206.164.57" # Public IP address of EC2 instance on AWS cloud
port=1248

HEADERSIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((aws_host, port))
s.listen(10) 

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    #address="192.168.43.22"
    print(f"Connection from {address} has been established.")

    msg="&,Mumbai,1,000.0,000.0,000.0,000.0,000.0,000.0"
    msg = f"{len(msg):<{HEADERSIZE}}"+msg

    clientsocket.send(bytes(msg,"utf-8"))
    print(msg)
    while True:
        time.sleep(10)
        msg="&,Mumbai,1,000.0,000.0,000.0,000.0,000.0,000.0"
        msg = f"{len(msg):<{HEADERSIZE}}"+msg

        print(msg)

        clientsocket.send(bytes(msg,"utf-8"))
