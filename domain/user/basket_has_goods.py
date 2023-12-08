from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class BasketHasGoods(IDto, db.Model):
    __tablename__ = "basket_has_goods"

    basket_id = Column(
        Integer,
        ForeignKey("basket.id"),
        nullable=False,
        primary_key=True,
    )
    goods_id = Column(
        Integer,
        ForeignKey("goods.id"),
        nullable=False,
        primary_key=True,
    )

    goods = relationship(
        "Goods",
        primaryjoin="Goods.id == BasketHasGoods.goods_id",
        back_populates="basket_has_goods",
    )
    basket = relationship(
        "Basket",
        primaryjoin="Basket.id == BasketHasGoods.basket_id",
        back_populates="basket_has_goods",
    )

    def __repr__(self):
        return f"BasketHasGoods(goods_id={self.goods_id}, basket_id={self.basket_id})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> BasketHasGoods:
        obj = BasketHasGoods(
            goods_id=dto_dict.get("goods_id"),
            basket_id=dto_dict.get("basket_id"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "goods_id": self.goods_id,
            "basket_id": self.basket_id,
        }
