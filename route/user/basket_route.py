from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from mydb import db
from mydb.auth.service import basket_services
from mydb.auth.domain.user.basket import Basket

basket_bp = Blueprint("basket", __name__, url_prefix="/basket/")


@basket_bp.get("")
def get_all_basket() -> Response:
    baskets = basket_services.find_all()

    # Convert Basket objects to dictionaries
    baskets_data = [basket.put_into_dto() for basket in baskets]

    return make_response(jsonify(baskets_data), HTTPStatus.OK)



@basket_bp.get("/<int:basket_id>")
def get_basket(basket_id: int) -> Response:
    return make_response(
        jsonify(basket_services.find_by_id(basket_id)), HTTPStatus.OK
    )


@basket_bp.put("/<int:basket_id>")
def update_basket(basket_id: int) -> Response:
    content = request.get_json()
    basket = Basket.create_from_dto(content)
    basket_services.update(basket_id, basket)
    return make_response("Basket updated", HTTPStatus.OK)


@basket_bp.patch("/<int:basket_id>")
def patch_basket(basket_id: int) -> Response:
    content = request.get_json()
    basket_services.patch(basket_id, content)
    return make_response("Basket updated", HTTPStatus.OK)


@basket_bp.delete("/<int:basket_id>")
def delete_basket(basket_id: int) -> Response:
    basket_services.delete(basket_id)
    return make_response("Basket deleted", HTTPStatus.OK)


@basket_bp.post("")
def create_basket() -> Response:
    content = request.get_json()
    basket = Basket.create_from_dto(content)
    basket_id = basket_services.create(basket)
    return make_response(
        f"Basket created with ID: {basket_id}", HTTPStatus.CREATED
    )


@basket_bp.post("/bulk")
def create_all_basket() -> Response:
    content = request.get_json()
    basket = [Basket.create_from_dto(data) for data in content]
    basket_services.create_all(basket)
    return make_response(basket_services.create_all(basket), HTTPStatus.CREATED)


@basket_bp.delete("/all")
def delete_all_basket() -> Response:
    basket_services.delete_all()
    return make_response("All Baskets deleted", HTTPStatus.OK)


@basket_bp.get("/comments/<int:basket_id>")
def get_basket_comments(basket_id):
    return make_response(
        jsonify(basket_services.get_comments(basket_id)), HTTPStatus.OK
    )


@basket_bp.get("/images/<int:basket_id>")
def get_basket_images(basket_id):
    return make_response(
        jsonify(basket_services.get_images(basket_id)), HTTPStatus.OK
    )
