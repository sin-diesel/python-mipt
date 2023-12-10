#!/usr/bin/env python3

from typing import Generator as _Generator
import socket as _socket
from contextlib import contextmanager as _contextmanager

LOOPBACK_HOST = "127.0.0.1"
LOOPBACK_PORT = 5000


class Server:
    def __init__(self, host: str, port: int) -> None:
        self._host = host
        self._port = port
        self._sock = _socket.create_server((host, port), family=_socket.AF_INET)
        self._sock.listen()

    def close(self) -> None:
        self._sock.close()


@_contextmanager
def create_server(host: str = LOOPBACK_HOST, port: int = LOOPBACK_PORT) -> _Generator[Server, None, None]:
    server = Server(host, port)
    try:
        yield server
    finally:
        server.close()
