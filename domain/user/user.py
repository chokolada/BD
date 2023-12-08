from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer, DECIMAL
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class User(IDto, db.Model):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(45), nullable=False)
    user_bank = Column(DECIMAL, nullable=False)

    goods_user = relationship("GoodsUser", back_populates="user")
    basket = relationship("Basket", back_populates="user")
    reviews = relationship("Reviews", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, user_name={self.user_name}, user_bank={self.user_bank})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> User:
        obj = User(
            id=dto_dict.get("id"),
            user_name=dto_dict.get("user_name"),
            user_bank=dto_dict.get("user_bank"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "user_name": self.user_name,
            "user_bank": self.user_bank,
        }