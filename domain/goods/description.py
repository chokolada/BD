from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class Description(IDto, db.Model):
    __tablename__ = "description"

    goods_id = Column(
        Integer, ForeignKey("goods.id"), primary_key=True, autoincrement=True
    )
    min_sys_req = Column(String(1000))
    desc_text = Column(String(1000))

    goods = relationship("Goods", back_populates="description")

    def __repr__(self):
        return f"Description(goods_id={self.goods_id}, min_sys_req={self.min_sys_req}, desc_text={self.desc_text})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Description:
        obj = Description(
            goods_id=dto_dict.get("goods_id"),
            min_sys_req=dto_dict.get("min_sys_req"),
            desc_text=dto_dict.get("desc_text"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "goods_id": self.goods_id,
            "min_sys_req": self.min_sys_req,
            "desc_text": self.desc_text,
        }
