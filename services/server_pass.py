from dataclasses import dataclass


@dataclass
class ServerPass:
    hostname: str
    username: str
    password: str
    ftpCatDir: str
    serverName: str
