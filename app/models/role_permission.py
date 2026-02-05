from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class RolePermission(Base):
    __tablename__ = "role_permissions"

    role_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("roles.id"),
        primary_key=True
    )

    permission_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("permissions.id"),
        primary_key=True
    )

    role = relationship(
        "Role",
        back_populates="permissions"
    )

    permission = relationship(
        "Permission",
        back_populates="roles"
    )
