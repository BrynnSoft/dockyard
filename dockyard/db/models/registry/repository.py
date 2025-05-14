from sqlalchemy import Uuid, String
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID

from ..base_model import Base

class RegistryRepository(Base):
    __tablename__ = 'regsitry_repositories'

    id: Mapped[UUID] = mapped_column(Uuid, nullable=False, primary_key=True, index=True, unique=True, autoincrement=False)
    name: Mapped[str] = mapped_column(String(256), nullable=False, index=True, unique=True)

    

