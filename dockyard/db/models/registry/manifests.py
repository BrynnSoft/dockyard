from sqlalchemy import Uuid, String, ForeignKey, UniqueConstraint, LargeBinary, JSON
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID

from ..base_model import Base

class RegistryManifest(Base):
    __tablename__ = 'regsitry_manifests'

    id: Mapped[UUID] = mapped_column(Uuid, nullable=False, primary_key=True, index=True, unique=True, autoincrement=False)
    repository_id: Mapped[UUID] = mapped_column(ForeignKey('regsitry_repositories.id'), nullable=False, index=True)
    digest_sha256: Mapped[bytes] = mapped_column(LargeBinary, nullable=False, index=True)
    tag_name: Mapped[str] = mapped_column(String(256), nullable=True, index=True)

    architecture: Mapped[str] = mapped_column(String(50), nullable=False)

    signature: Mapped[list[dict]] = mapped_column(JSON, nullable=True)

    

