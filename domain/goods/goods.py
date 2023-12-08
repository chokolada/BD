from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class Goods(IDto, db.Model):
    __tablename__ = "goods"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(70), nullable=False)
    price = Column(DECIMAL, nullable=False)
    seller_name = Column(String(45))

    goods_user = relationship("GoodsUser", back_populates="goods")
    categories_goods = relationship("CategoriesGoods", back_populates="goods")
    description = relationship("Description", back_populates="goods")
    delivery = relationship("Delivery", back_populates="goods")
    reviews = relationship("Reviews", back_populates="goods")
    basket_has_goods = relationship("BasketHasGoods", back_populates="goods")

    def __repr__(self):
        return (
            f"Goods(id={self.id}, name={self.name}, price={self.price}, "
            f"seller_name={self.seller_name}"
        )

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Goods:
        obj = Goods(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            price=dto_dict.get("price"),
            seller_name=dto_dict.get("seller_name"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "seller_name": self.seller_name,
        }