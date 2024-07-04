from datetime import datetime
from typing import Any

from sqlalchemy import Integer, func, inspect
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

Base = declarative_base()


class BModel(Base):
    """Base model"""

    __abstract__ = True

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
    deleted_at: Mapped[datetime] = mapped_column(nullable=True)

    
    def delete(self):
        self.deleted_at = func.now()

    def dict(self) -> dict[str, Any]:
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
