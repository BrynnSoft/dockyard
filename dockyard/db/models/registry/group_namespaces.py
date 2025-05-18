from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID

from ....enums.access_permission import AccessPermission

from ..base_model import Base

class GroupNamespace(Base):
    __tablename__ = 'group_namespaces'

    group_id: Mapped[UUID] = mapped_column(ForeignKey('groups.id'), nullable=False, primary_key=True, index=True, unique=True, autoincrement=False)
    namespace_id: Mapped[UUID] = mapped_column(ForeignKey('regsitry_namespaces.id'), nullable=False, primary_key=True, index=True, unique=True, autoincrement=False)

    permission: Mapped[AccessPermission] = mapped_column(Enum(AccessPermission), nullable=False)