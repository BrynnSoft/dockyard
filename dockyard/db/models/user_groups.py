from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID

from ...enums.user_role import UserRole

from .base_model import Base

class UserGroups(Base):
    __tablename__ = 'user_groups'

    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'), nullable=False, primary_key=True, index=True, unique=True, autoincrement=False)
    group_id: Mapped[UUID] = mapped_column(ForeignKey('groups.id'), nullable=False, primary_key=True, index=True, unique=True, autoincrement=False)