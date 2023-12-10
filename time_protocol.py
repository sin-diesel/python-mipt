#!/usr/bin/env python3

import socket

BUF_SIZE = 4096

def _main() -> None:
    host = "time.nist.gov"
    port = 37
    with socket.socket() as sock:
        sock.connect((host, port))
        sock.sendall(b"Hi")
        data = sock.recv(BUF_SIZE)
        print(data)

if __name__ == "__main__":
    _main()
