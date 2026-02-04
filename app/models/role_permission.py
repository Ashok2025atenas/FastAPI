from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database import Base


class RoleHasPermission(Base):
    __tablename__ = "role_has_permissions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    role_id = Column(UUID(as_uuid=True), ForeignKey("roles.id"))
    permission_id = Column(UUID(as_uuid=True), ForeignKey("permissions.id"))
