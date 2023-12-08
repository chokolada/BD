from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class CategoriesGoods(IDto, db.Model):
    __tablename__ = "categories_goods"

    goods_id = Column(
        Integer,
        ForeignKey("goods.id"),
        nullable=False,
        primary_key=True,
    )
    categories_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False,
        primary_key=True,
    )

    goods = relationship(
        "Goods",
        primaryjoin="Goods.id == CategoriesGoods.goods_id",
        back_populates="categories_goods",
    )
    categories = relationship(
        "Categories",
        primaryjoin="Categories.id == CategoriesGoods.categories_id",
        back_populates="categories_goods",
    )

    def __repr__(self):
        return f"CategoriesGoods(goods_id={self.goods_id}, categories_id={self.categories_id})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> CategoriesGoods:
        obj = CategoriesGoods(
            goods_id=dto_dict.get("goods_id"),
            categories_id=dto_dict.get("categories_id"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "goods_id": self.goods_id,
            "categories_id": self.categories_id,
        }
