from typing import Optional
from dataclasses import dataclass

from sqlalchemy import Integer, String, NVARCHAR, Uuid
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import uuid

from base_table import Base


@dataclass
class User(Base):
    __tablename__ = "user"

    id: Mapped[uuid] = mapped_column(Uuid, primary_key=True)
    name: Mapped[str] = mapped_column(NVARCHAR(50), nullable=False)
    fullname: Mapped[str] = mapped_column(NVARCHAR(50), nullable=False)
    nickname: Mapped[Optional[str]] = mapped_column(NVARCHAR(30), nullable=True)

    # primary_key=True, therefore will be NOT NULL
    # id: Mapped[int] = mapped_column(primary_key=True)

    # not Optional[], therefore will be NOT NULL
    # data: Mapped[str]

    # Optional[], therefore will be NULL
    # additional_info: Mapped[Optional[str]]

    # will be String() NOT NULL, but can be None in Python
    # data: Mapped[Optional[str]] = mapped_column(nullable=False)
