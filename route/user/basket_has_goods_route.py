from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from mydb import db
from mydb.auth.service import basket_has_goods_services
from mydb.auth.domain.user.basket_has_goods import BasketHasGoods

basket_has_goods_bp = Blueprint("basket_has_goods", __name__, url_prefix="/basket_has_goods/")


@basket_has_goods_bp.get("")
def get_all_basket_has_goods() -> Response:
    basket_has_goods = basket_has_goods_services.find_all()

    # Convert BasketHasGoods objects to dictionaries
    basket_has_goods_data = [item.put_into_dto() for item in basket_has_goods]

    return make_response(jsonify(basket_has_goods_data), HTTPStatus.OK)



@basket_has_goods_bp.get("/<int:basket_has_goods_id>")
def get_basket_has_goods(basket_has_goods_id: int) -> Response:
    return make_response(
        jsonify(basket_has_goods_services.find_by_id(basket_has_goods_id)), HTTPStatus.OK
    )


@basket_has_goods_bp.put("/<int:basket_has_goods_id>")
def update_basket_has_goods(basket_has_goods_id: int) -> Response:
    content = request.get_json()
    basket_has_goods = BasketHasGoods.create_from_dto(content)
    basket_has_goods_services.update(basket_has_goods_id, basket_has_goods)
    return make_response("BasketHasGoods updated", HTTPStatus.OK)


@basket_has_goods_bp.patch("/<int:basket_has_goods_id>")
def patch_basket_has_goods(basket_has_goods_id: int) -> Response:
    content = request.get_json()
    basket_has_goods_services.patch(basket_has_goods_id, content)
    return make_response("BasketHasGoods updated", HTTPStatus.OK)


@basket_has_goods_bp.delete("/<int:basket_has_goods_id>")
def delete_basket_has_goods(basket_has_goods_id: int) -> Response:
    basket_has_goods_services.delete(basket_has_goods_id)
    return make_response("BasketHasGoods deleted", HTTPStatus.OK)


@basket_has_goods_bp.post("")
def create_basket_has_goods() -> Response:
    content = request.get_json()
    basket_has_goods = BasketHasGoods.create_from_dto(content)
    basket_has_goods_id = basket_has_goods_services.create(basket_has_goods)
    return make_response(
        f"BasketHasGoods created with ID: {basket_has_goods_id}", HTTPStatus.CREATED
    )


@basket_has_goods_bp.post("/bulk")
def create_all_basket_has_goods() -> Response:
    content = request.get_json()
    basket_has_goods = [BasketHasGoods.create_from_dto(data) for data in content]
    basket_has_goods_services.create_all(basket_has_goods)
    return make_response(basket_has_goods_services.create_all(basket_has_goods), HTTPStatus.CREATED)


@basket_has_goods_bp.delete("/all")
def delete_all_basket_has_goods() -> Response:
    basket_has_goods_services.delete_all()
    return make_response("All BasketHasGoodss deleted", HTTPStatus.OK)


@basket_has_goods_bp.get("/comments/<int:basket_has_goods_id>")
def get_basket_has_goods_comments(basket_has_goods_id):
    return make_response(
        jsonify(basket_has_goods_services.get_comments(basket_has_goods_id)), HTTPStatus.OK
    )


@basket_has_goods_bp.get("/images/<int:basket_has_goods_id>")
def get_basket_has_goods_images(basket_has_goods_id):
    return make_response(
        jsonify(basket_has_goods_services.get_images(basket_has_goods_id)), HTTPStatus.OK
    )
