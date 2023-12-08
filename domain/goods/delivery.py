from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class Delivery(IDto, db.Model):
    __tablename__ = "delivery"

    id = Column(Integer, primary_key=True, autoincrement=True)
    delivery_company_name = Column(String(1000), nullable=False)
    payment_type = Column(String(20), nullable=False)
    guarantee = Column(Integer)
    deliverycol = Column(String(45))
    goods_id = Column(Integer, ForeignKey("goods.id"), nullable=False)

    goods = relationship("Goods", back_populates="delivery")

    def __repr__(self):
        return (
            f"Delivery(id={self.id}, delivery_company_name={self.delivery_company_name}, "
            f"payment_type={self.payment_type}, guarantee={self.guarantee}, "
            f"deliverycol={self.deliverycol}, goods_id={self.goods_id})"
        )

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Delivery:
        obj = Delivery(
            id=dto_dict.get("id"),
            delivery_company_name=dto_dict.get("delivery_company_name"),
            payment_type=dto_dict.get("payment_type"),
            guarantee=dto_dict.get("guarantee"),
            deliverycol=dto_dict.get("deliverycol"),
            goods_id=dto_dict.get("goods_id"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "delivery_company_name": self.delivery_company_name,
            "payment_type": self.payment_type,
            "guarantee": self.guarantee,
            "deliverycol": self.deliverycol,
            "goods_id": self.goods_id,
        }
