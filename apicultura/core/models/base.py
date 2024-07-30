from typing import Any
import enum
from sqlalchemy import Column, Integer, func, inspect, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.types import VARCHAR, TypeDecorator

Base = declarative_base()


class BModel(Base):
    """Base model"""

    __abstract__ = True

    id = Column(Integer(), primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )
    deleted_at = Column(DateTime, nullable=True)

    def delete(self):
        self.deleted_at = func.now()

    def dict(self) -> dict[str, Any]:
        return {
            c.key: getattr(self, c.key)
            for c in inspect(self).mapper.column_attrs
        }


class ChoiceType(TypeDecorator):
    impl = VARCHAR

    def __init__(self, enum_class, **kwargs):
        super().__init__(**kwargs)
        self.enum_class = enum_class
        self.choices = {item.value: item for item in enum_class}

    def process_bind_param(self, value, dialect):
        if isinstance(value, enum.Enum):
            return value.value
        if value in self.choices:
            return value
        raise ValueError(
            f"Invalid value '{value}': Allowed values are {list(self.choices.keys())}"
        )

    def process_result_value(self, value, dialect):
        try:
            return self.choices[value]
        except KeyError as exc:
            raise ValueError(
                f"The database contains and unrecognized enum key '{value}'"
            ) from exc
