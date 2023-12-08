from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from mydb import db
from mydb.auth.service import categories_services
from mydb.auth.domain.goods.categories import Categories

categories_bp = Blueprint("categories", __name__, url_prefix="/categories/")


@categories_bp.get("")
def get_all_categories() -> Response:
    categories = categories_services.find_all()

    # Convert Categories objects to dictionaries
    categories_data = [category.put_into_dto() for category in categories]

    return make_response(jsonify(categories_data), HTTPStatus.OK)


@categories_bp.get("/<int:categories_id>")
def get_categories(categories_id: int) -> Response:
    return make_response(
        jsonify(categories_services.find_by_id(categories_id)), HTTPStatus.OK
    )


@categories_bp.put("/<int:categories_id>")
def update_categories(categories_id: int) -> Response:
    content = request.get_json()
    categories = Categories.create_from_dto(content)
    categories_services.update(categories_id, categories)
    return make_response("Categories updated", HTTPStatus.OK)


@categories_bp.patch("/<int:categories_id>")
def patch_categories(categories_id: int) -> Response:
    content = request.get_json()
    categories_services.patch(categories_id, content)
    return make_response("Categories updated", HTTPStatus.OK)


@categories_bp.delete("/<int:categories_id>")
def delete_categories(categories_id: int) -> Response:
    categories_services.delete(categories_id)
    return make_response("Categories deleted", HTTPStatus.OK)


@categories_bp.post("")
def create_categories() -> Response:
    content = request.get_json()
    categories = Categories.create_from_dto(content)
    categories_id = categories_services.create(categories)
    return make_response(
        f"Categories created with ID: {categories_id}", HTTPStatus.CREATED
    )


@categories_bp.post("/bulk")
def create_all_categories() -> Response:
    content = request.get_json()
    categories = [Categories.create_from_dto(data) for data in content]
    categories_services.create_all(categories)
    return make_response(categories_services.create_all(categories), HTTPStatus.CREATED)


@categories_bp.delete("/all")
def delete_all_categories() -> Response:
    categories_services.delete_all()
    return make_response("All Categoriess deleted", HTTPStatus.OK)


@categories_bp.get("/comments/<int:categories_id>")
def get_categories_comments(categories_id):
    return make_response(
        jsonify(categories_services.get_comments(categories_id)), HTTPStatus.OK
    )


@categories_bp.get("/images/<int:categories_id>")
def get_categories_images(categories_id):
    return make_response(
        jsonify(categories_services.get_images(categories_id)), HTTPStatus.OK
    )
