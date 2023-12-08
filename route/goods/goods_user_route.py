from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from mydb import db
from mydb.auth.service import goods_user_services
from mydb.auth.domain.goods.goods_user import GoodsUser

goods_user_bp = Blueprint("goods_user", __name__, url_prefix="/goods_user/")


@goods_user_bp.get("")
def get_all_goods_user() -> Response:
    goods_users = goods_user_services.find_all()

    # Convert GoodsUser objects to dictionaries
    goods_users_data = [goods_user.put_into_dto() for goods_user in goods_users]

    return make_response(jsonify(goods_users_data), HTTPStatus.OK)



@goods_user_bp.get("/<int:goods_user_id>")
def get_goods_user(goods_user_id: int) -> Response:
    return make_response(
        jsonify(goods_user_services.find_by_id(goods_user_id)), HTTPStatus.OK
    )


@goods_user_bp.put("/<int:goods_user_id>")
def update_goods_user(goods_user_id: int) -> Response:
    content = request.get_json()
    goods_user = GoodsUser.create_from_dto(content)
    goods_user_services.update(goods_user_id, goods_user)
    return make_response("GoodsUser updated", HTTPStatus.OK)


@goods_user_bp.patch("/<int:goods_user_id>")
def patch_goods_user(goods_user_id: int) -> Response:
    content = request.get_json()
    goods_user_services.patch(goods_user_id, content)
    return make_response("GoodsUser updated", HTTPStatus.OK)


@goods_user_bp.delete("/<int:goods_user_id>")
def delete_goods_user(goods_user_id: int) -> Response:
    goods_user_services.delete(goods_user_id)
    return make_response("GoodsUser deleted", HTTPStatus.OK)


@goods_user_bp.post("")
def create_goods_user() -> Response:
    content = request.get_json()
    goods_user = GoodsUser.create_from_dto(content)
    goods_user_id = goods_user_services.create(goods_user)
    return make_response(
        f"GoodsUser created with ID: {goods_user_id}", HTTPStatus.CREATED
    )


@goods_user_bp.post("/bulk")
def create_all_goods_user() -> Response:
    content = request.get_json()
    goods_user = [GoodsUser.create_from_dto(data) for data in content]
    goods_user_services.create_all(goods_user)
    return make_response(goods_user_services.create_all(goods_user), HTTPStatus.CREATED)


@goods_user_bp.delete("/all")
def delete_all_goods_user() -> Response:
    goods_user_services.delete_all()
    return make_response("All GoodsUsers deleted", HTTPStatus.OK)


@goods_user_bp.get("/comments/<int:goods_user_id>")
def get_goods_user_comments(goods_user_id):
    return make_response(
        jsonify(goods_user_services.get_comments(goods_user_id)), HTTPStatus.OK
    )


@goods_user_bp.get("/images/<int:goods_user_id>")
def get_goods_user_images(goods_user_id):
    return make_response(
        jsonify(goods_user_services.get_images(goods_user_id)), HTTPStatus.OK
    )
