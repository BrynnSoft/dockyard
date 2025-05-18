from sqlalchemy import Uuid, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID

from ..base_model import Base

class RegistryNamespace(Base):
    __tablename__ = 'regsitry_namespaces'

    id: Mapped[UUID] = mapped_column(Uuid, nullable=False, primary_key=True, index=True, unique=True, autoincrement=False)
    organization_id: Mapped[UUID] = mapped_column(ForeignKey('organizations.id'), nullable=True, index=True)
    private: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default='true')
    name: Mapped[str] = mapped_column(String(256), nullable=False, index=True, unique=True)

    upstream_server: Mapped[str] = mapped_column(String(256), nullable=True)

    

