from enum import Flag, auto

class AuthMode(Flag):
    Public = auto()
    BasicAuth = auto()
    BearerToken = auto()
    Docker = Public | BasicAuth | BearerToken
    Session = auto()

    Any = Docker | Session
    AnyAuth = BasicAuth | BearerToken | Session