from sqlalchemy import Uuid, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID

from ..base_model import Base

class RegistryRepository(Base):
    __tablename__ = 'regsitry_repositories'

    __table_args__ = (
        UniqueConstraint('namespace_id', 'name', name='ix_regsitry_repositories_namespace_name'),
    )

    id: Mapped[UUID] = mapped_column(Uuid, nullable=False, primary_key=True, index=True, unique=True, autoincrement=False)
    namespace_id: Mapped[UUID] = mapped_column(ForeignKey('regsitry_namespaces.id'), nullable=False)
    name: Mapped[str] = mapped_column(String(256), nullable=False)

    

