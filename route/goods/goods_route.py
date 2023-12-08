from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from mydb import db
from mydb.auth.service import goods_services
from mydb.auth.domain.goods.goods import Goods

goods_bp = Blueprint("goods", __name__, url_prefix="/goods/")


@goods_bp.get("")
def get_all_goods() -> Response:
    goods = goods_services.find_all()

    # Convert Goods objects to dictionaries
    goods_data = [good.put_into_dto() for good in goods]

    return make_response(jsonify(goods_data), HTTPStatus.OK)



@goods_bp.get("/<int:goods_id>")
def get_goods(goods_id: int) -> Response:
    return make_response(
        jsonify(goods_services.find_by_id(goods_id)), HTTPStatus.OK
    )


@goods_bp.put("/<int:goods_id>")
def update_goods(goods_id: int) -> Response:
    content = request.get_json()
    goods = Goods.create_from_dto(content)
    goods_services.update(goods_id, goods)
    return make_response("Goods updated", HTTPStatus.OK)


@goods_bp.patch("/<int:goods_id>")
def patch_goods(goods_id: int) -> Response:
    content = request.get_json()
    goods_services.patch(goods_id, content)
    return make_response("Goods updated", HTTPStatus.OK)


@goods_bp.delete("/<int:goods_id>")
def delete_goods(goods_id: int) -> Response:
    goods_services.delete(goods_id)
    return make_response("Goods deleted", HTTPStatus.OK)


@goods_bp.post("")
def create_goods() -> Response:
    content = request.get_json()
    goods = Goods.create_from_dto(content)
    goods_id = goods_services.create(goods)
    return make_response(
        f"Goods created with ID: {goods_id}", HTTPStatus.CREATED
    )


@goods_bp.post("/bulk")
def create_all_goods() -> Response:
    content = request.get_json()
    goods = [Goods.create_from_dto(data) for data in content]
    goods_services.create_all(goods)
    return make_response(goods_services.create_all(goods), HTTPStatus.CREATED)


@goods_bp.delete("/all")
def delete_all_goods() -> Response:
    goods_services.delete_all()
    return make_response("All Goodss deleted", HTTPStatus.OK)


@goods_bp.get("/comments/<int:goods_id>")
def get_goods_comments(goods_id):
    return make_response(
        jsonify(goods_services.get_comments(goods_id)), HTTPStatus.OK
    )


@goods_bp.get("/images/<int:goods_id>")
def get_goods_images(goods_id):
    return make_response(
        jsonify(goods_services.get_images(goods_id)), HTTPStatus.OK
    )
