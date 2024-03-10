from typing import Optional
import uuid

from base_table import Base

from sqlalchemy import NVARCHAR, Uuid, DECIMAL, INTEGER
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class MenuItem(Base):
    __tablename__ = "MenuItem"

    id: Mapped[Optional[uuid]] = mapped_column(Uuid, primary_key=True, init=False)

    category: Mapped[str] = mapped_column(NVARCHAR(20), nullable=False)
    name: Mapped[str] = mapped_column(NVARCHAR(50), nullable=False)
    price: Mapped[float] = mapped_column(DECIMAL(8,2), nullable=False)
    quantity: Mapped[Optional[int]] = mapped_column(INTEGER, nullable=False, default=1)
