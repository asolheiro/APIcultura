from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, declarative_base

Base = declarative_base()




class BModel(Base):
    """Base model"""
    
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
