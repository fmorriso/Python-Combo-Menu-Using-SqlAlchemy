from typing import Optional

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from base_table import Base


class User(Base):
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(50), nullable=False)
    fullname = mapped_column(String)
    nickname = mapped_column(String(30))

    # primary_key=True, therefore will be NOT NULL
    # id: Mapped[int] = mapped_column(primary_key=True)

    # not Optional[], therefore will be NOT NULL
    # data: Mapped[str]

    # Optional[], therefore will be NULL
    # additional_info: Mapped[Optional[str]]

    # will be String() NOT NULL, but can be None in Python
    # data: Mapped[Optional[str]] = mapped_column(nullable=False)
