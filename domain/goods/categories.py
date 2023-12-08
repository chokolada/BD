from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from mydb import db
from mydb.auth.domain.i_dto import IDto


class Categories(IDto, db.Model):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)

    categories_goods = relationship("CategoriesGoods", back_populates="categories")

    def __repr__(self):
        return f"Categories(id={self.id}, name={self.name})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Categories:
        obj = Categories(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
        )
        return obj

    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
        }
