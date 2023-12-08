from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class GoodsUser(IDto, db.Model):
    __tablename__ = "goods_user"

    goods_id = Column(
        Integer,
        ForeignKey("goods.id"),
        nullable=False,
        primary_key=True,
    )
    user_id = Column(
        Integer,
        ForeignKey("user.id"),
        nullable=False,
        primary_key=True,
    )

    goods = relationship(
        "Goods",
        primaryjoin="Goods.id == GoodsUser.goods_id",
        back_populates="goods_user",
    )
    user = relationship(
        "User", primaryjoin="User.id == GoodsUser.user_id", back_populates="goods_user"
    )

    def __repr__(self):
        return f"GoodsUser(goods_id={self.goods_id}, user_id={self.user_id})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> GoodsUser:
        obj = GoodsUser(
            goods_id=dto_dict.get("goods_id"),
            user_id=dto_dict.get("user_id"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "goods_id": self.goods_id,
            "user_id": self.user_id,
        }
