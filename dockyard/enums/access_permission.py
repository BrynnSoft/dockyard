from enum import IntFlag, auto

class AccessPermission(IntFlag):
    Read = auto()
    Write = auto()
    ReadWrite = Read & Write