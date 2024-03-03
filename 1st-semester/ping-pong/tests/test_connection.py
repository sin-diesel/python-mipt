#!/usr/bin/env python3

from pingpong.server.server import create_server as _create_server

def test_connection() -> None:
    with _create_server() as server:
        pass