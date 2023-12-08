from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from mydb import db
from mydb.auth.service import delivery_services
from mydb.auth.domain.goods.delivery import Delivery

delivery_bp = Blueprint("delivery", __name__, url_prefix="/delivery/")


@delivery_bp.get("")
def get_all_delivery() -> Response:
    return make_response(jsonify(delivery_services.find_all()), HTTPStatus.OK)


@delivery_bp.get("/<int:delivery_id>")
def get_delivery(delivery_id: int) -> Response:
    return make_response(
        jsonify(delivery_services.find_by_id(delivery_id)), HTTPStatus.OK
    )


@delivery_bp.put("/<int:delivery_id>")
def update_delivery(delivery_id: int) -> Response:
    content = request.get_json()
    delivery = Delivery.create_from_dto(content)
    delivery_services.update(delivery_id, delivery)
    return make_response("Delivery updated", HTTPStatus.OK)


@delivery_bp.patch("/<int:delivery_id>")
def patch_delivery(delivery_id: int) -> Response:
    content = request.get_json()
    delivery_services.patch(delivery_id, content)
    return make_response("Delivery updated", HTTPStatus.OK)


@delivery_bp.delete("/<int:delivery_id>")
def delete_delivery(delivery_id: int) -> Response:
    delivery_services.delete(delivery_id)
    return make_response("Delivery deleted", HTTPStatus.OK)


@delivery_bp.post("")
def create_delivery() -> Response:
    content = request.get_json()
    delivery = Delivery.create_from_dto(content)
    delivery_id = delivery_services.create(delivery)
    return make_response(
        f"Delivery created with ID: {delivery_id}", HTTPStatus.CREATED
    )


@delivery_bp.post("/bulk")
def create_all_delivery() -> Response:
    content = request.get_json()
    delivery = [Delivery.create_from_dto(data) for data in content]
    delivery_services.create_all(delivery)
    return make_response(delivery_services.create_all(delivery), HTTPStatus.CREATED)


@delivery_bp.delete("/all")
def delete_all_delivery() -> Response:
    delivery_services.delete_all()
    return make_response("All Deliverys deleted", HTTPStatus.OK)


@delivery_bp.get("/comments/<int:delivery_id>")
def get_delivery_comments(delivery_id):
    return make_response(
        jsonify(delivery_services.get_comments(delivery_id)), HTTPStatus.OK
    )


@delivery_bp.get("/images/<int:delivery_id>")
def get_delivery_images(delivery_id):
    return make_response(
        jsonify(delivery_services.get_images(delivery_id)), HTTPStatus.OK
    )
