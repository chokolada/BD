from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class Reviews(IDto, db.Model):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(1000), nullable=False)
    rate = Column(Integer, nullable=False)
    goods_id = Column(Integer, ForeignKey("goods.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    user = relationship("User", back_populates="reviews")
    goods = relationship("Goods", back_populates="reviews")

    def __repr__(self):
        return f"Reviews(id={self.id}, text={self.text}, rate={self.rate}, goods_id={self.goods_id}, user_id={self.user_id})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Reviews:
        obj = Reviews(
            id=dto_dict.get("id"),
            text=dto_dict.get("text"),
            rate=dto_dict.get("rate"),
            goods_id=dto_dict.get("goods_id"),
            user_id=dto_dict.get("user_id"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "text": self.text,
            "rate": self.rate,
            "goods_id": self.goods_id,
            "user_id": self.user_id,
        }
