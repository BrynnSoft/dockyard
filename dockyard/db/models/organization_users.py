from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID

from ...enums.user_role import UserRole

from .base_model import Base

class OrganizationUser(Base):
    __tablename__ = 'organization_users'

    organization_id: Mapped[UUID] = mapped_column(ForeignKey('organizations.id'), nullable=False, primary_key=True, index=True, unique=True, autoincrement=False)
    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'), nullable=False, primary_key=True, index=True, unique=True, autoincrement=False)

    role: Mapped[UserRole] = mapped_column(Enum(UserRole), nullable=False)