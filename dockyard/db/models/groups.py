from sqlalchemy import Uuid, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID

from .base_model import Base

class Group(Base):
    __tablename__ = 'groups'

    id: Mapped[UUID] = mapped_column(Uuid, nullable=False, primary_key=True, index=True, unique=True, autoincrement=False)
    organization_id: Mapped[UUID] = mapped_column(ForeignKey('organizations.id'), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(256), nullable=False, index=True, unique=True)

    