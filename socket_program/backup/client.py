import socket

local_host="192.168.43.231" # RPi4 IP address
aws_host="15.206.164.57" # Public IP address of EC2 instance on AWS cloud
port=1248

HEADERSIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((aws_host, port))

while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        print(f"full message length: {msglen}")

        full_msg += msg.decode("utf-8")

        print(len(full_msg))


        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ""
