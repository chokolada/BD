from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from mydb import db
from mydb.auth.service import description_services
from mydb.auth.domain.goods.description import Description

description_bp = Blueprint("description", __name__, url_prefix="/description/")


@description_bp.get("")
def get_all_description() -> Response:
    descriptions = description_services.find_all()

    # Convert Description objects to dictionaries
    descriptions_data = [description.put_into_dto() for description in descriptions]

    return make_response(jsonify(descriptions_data), HTTPStatus.OK)



@description_bp.get("/<int:description_id>")
def get_description(description_id: int) -> Response:
    return make_response(
        jsonify(description_services.find_by_id(description_id)), HTTPStatus.OK
    )


@description_bp.put("/<int:description_id>")
def update_description(description_id: int) -> Response:
    content = request.get_json()
    description = Description.create_from_dto(content)
    description_services.update(description_id, description)
    return make_response("Description updated", HTTPStatus.OK)


@description_bp.patch("/<int:description_id>")
def patch_description(description_id: int) -> Response:
    content = request.get_json()
    description_services.patch(description_id, content)
    return make_response("Description updated", HTTPStatus.OK)


@description_bp.delete("/<int:description_id>")
def delete_description(description_id: int) -> Response:
    description_services.delete(description_id)
    return make_response("Description deleted", HTTPStatus.OK)


@description_bp.post("")
def create_description() -> Response:
    content = request.get_json()
    description = Description.create_from_dto(content)
    description_id = description_services.create(description)
    return make_response(
        f"Description created with ID: {description_id}", HTTPStatus.CREATED
    )


@description_bp.post("/bulk")
def create_all_description() -> Response:
    content = request.get_json()
    description = [Description.create_from_dto(data) for data in content]
    description_services.create_all(description)
    return make_response(description_services.create_all(description), HTTPStatus.CREATED)


@description_bp.delete("/all")
def delete_all_description() -> Response:
    description_services.delete_all()
    return make_response("All Descriptions deleted", HTTPStatus.OK)


@description_bp.get("/comments/<int:description_id>")
def get_description_comments(description_id):
    return make_response(
        jsonify(description_services.get_comments(description_id)), HTTPStatus.OK
    )


@description_bp.get("/images/<int:description_id>")
def get_description_images(description_id):
    return make_response(
        jsonify(description_services.get_images(description_id)), HTTPStatus.OK
    )
