from sqlalchemy import Uuid, String, ForeignKey, LargeBinary, JSON, SmallInteger, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID

from ..base_model import Base

class RegistryLayer(Base):
    __tablename__ = 'regsitry_layers'

    id: Mapped[UUID] = mapped_column(Uuid, nullable=False, primary_key=True, index=True, unique=True, autoincrement=False)
    manifest_id: Mapped[UUID] = mapped_column(ForeignKey('regsitry_manifests.id'), nullable=False, index=True)
    digest_sha256: Mapped[bytes] = mapped_column(LargeBinary, nullable=False, index=True)

    position: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    size: Mapped[int] = mapped_column(BigInteger, nullable=False)

    storage_provider: Mapped[str] = mapped_column(String(255), nullable=False)
    storage_info: Mapped[dict] = mapped_column(JSON, nullable=False)