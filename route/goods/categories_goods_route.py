from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from mydb import db
from mydb.auth.service import categories_goods_services
from mydb.auth.domain.goods.categories_goods import CategoriesGoods

categories_goods_bp = Blueprint("categories_goods", __name__, url_prefix="/categories_goods/")


@categories_goods_bp.get("")
def get_all_categories_goods() -> Response:
    categories_goods = categories_goods_services.find_all()

    # Convert CategoriesGoods objects to dictionaries
    categories_goods_data = [category_goods.put_into_dto() for category_goods in categories_goods]

    return make_response(jsonify(categories_goods_data), HTTPStatus.OK)



@categories_goods_bp.get("/<int:categories_goods_id>")
def get_categories_goods(categories_goods_id: int) -> Response:
    return make_response(
        jsonify(categories_goods_services.find_by_id(categories_goods_id)), HTTPStatus.OK
    )


@categories_goods_bp.put("/<int:categories_goods_id>")
def update_categories_goods(categories_goods_id: int) -> Response:
    content = request.get_json()
    categories_goods = CategoriesGoods.create_from_dto(content)
    categories_goods_services.update(categories_goods_id, categories_goods)
    return make_response("CategoriesGoods updated", HTTPStatus.OK)


@categories_goods_bp.patch("/<int:categories_goods_id>")
def patch_categories_goods(categories_goods_id: int) -> Response:
    content = request.get_json()
    categories_goods_services.patch(categories_goods_id, content)
    return make_response("CategoriesGoods updated", HTTPStatus.OK)


@categories_goods_bp.delete("/<int:categories_goods_id>")
def delete_categories_goods(categories_goods_id: int) -> Response:
    categories_goods_services.delete(categories_goods_id)
    return make_response("CategoriesGoods deleted", HTTPStatus.OK)


@categories_goods_bp.post("")
def create_categories_goods() -> Response:
    content = request.get_json()
    categories_goods = CategoriesGoods.create_from_dto(content)
    categories_goods_id = categories_goods_services.create(categories_goods)
    return make_response(
        f"CategoriesGoods created with ID: {categories_goods_id}", HTTPStatus.CREATED
    )


@categories_goods_bp.post("/bulk")
def create_all_categories_goods() -> Response:
    content = request.get_json()
    categories_goods = [CategoriesGoods.create_from_dto(data) for data in content]
    categories_goods_services.create_all(categories_goods)
    return make_response(categories_goods_services.create_all(categories_goods), HTTPStatus.CREATED)


@categories_goods_bp.delete("/all")
def delete_all_categories_goods() -> Response:
    categories_goods_services.delete_all()
    return make_response("All CategoriesGoods deleted", HTTPStatus.OK)


@categories_goods_bp.get("/comments/<int:categories_goods_id>")
def get_categories_goods_comments(categories_goods_id):
    return make_response(
        jsonify(categories_goods_services.get_comments(categories_goods_id)), HTTPStatus.OK
    )


@categories_goods_bp.get("/images/<int:categories_goods_id>")
def get_categories_goods_images(categories_goods_id):
    return make_response(
        jsonify(categories_goods_services.get_images(categories_goods_id)), HTTPStatus.OK
    )
