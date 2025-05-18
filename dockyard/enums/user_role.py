from enum import StrEnum

class UserRole(StrEnum):
    Owner = 'owner'
    Admin = 'admin'
    User = 'user'