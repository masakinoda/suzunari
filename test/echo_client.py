# using: utf-8

import socket

HOST = '127.0.0.1'
PORT = 5959

def main():
    msg = b"test"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.sendall(msg)
    recv = sock.recv(1024)
    print(recv)
    sock.close()

if __name__ == '__main__':
    main()

