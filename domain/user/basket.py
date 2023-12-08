from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class Basket(IDto, db.Model):
    __tablename__ = "basket"

    id = Column(Integer, primary_key=True, autoincrement=True)
    number_of_items = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    user = relationship("User", back_populates="basket")
    basket_has_goods = relationship("BasketHasGoods", back_populates="basket")

    def __repr__(self):
        return f"Basket(id={self.id}, number_of_items={self.number_of_items}, user_id={self.user_id})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Basket:
        obj = Basket(
            id=dto_dict.get("id"),
            number_of_items=dto_dict.get("number_of_items"),
            user_id=dto_dict.get("user_id"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "number_of_items": self.number_of_items,
            "user_id": self.user_id,
        }
