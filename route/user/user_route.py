from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from mydb import db
from mydb.auth.service import user_services
from mydb.auth.domain.user.user import User

user_bp = Blueprint("user", __name__, url_prefix="/user/")


@user_bp.get("")
def get_all_user() -> Response:
    users = user_services.find_all()

    # Convert User objects to dictionaries
    users_data = [user.put_into_dto() for user in users]

    return make_response(jsonify(users_data), HTTPStatus.OK)



@user_bp.get("/<int:user_id>")
def get_user(user_id: int) -> Response:
    return make_response(
        jsonify(user_services.find_by_id(user_id)), HTTPStatus.OK
    )


@user_bp.put("/<int:user_id>")
def update_user(user_id: int) -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    user_services.update(user_id, user)
    return make_response("User updated", HTTPStatus.OK)


@user_bp.patch("/<int:user_id>")
def patch_user(user_id: int) -> Response:
    content = request.get_json()
    user_services.patch(user_id, content)
    return make_response("User updated", HTTPStatus.OK)


@user_bp.delete("/<int:user_id>")
def delete_user(user_id: int) -> Response:
    user_services.delete(user_id)
    return make_response("User deleted", HTTPStatus.OK)


@user_bp.post("")
def create_user() -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    user_id = user_services.create(user)
    return make_response(
        f"User created with ID: {user_id}", HTTPStatus.CREATED
    )


@user_bp.post("/bulk")
def create_all_user() -> Response:
    content = request.get_json()
    user = [User.create_from_dto(data) for data in content]
    user_services.create_all(user)
    return make_response(user_services.create_all(user), HTTPStatus.CREATED)


@user_bp.delete("/all")
def delete_all_user() -> Response:
    user_services.delete_all()
    return make_response("All Users deleted", HTTPStatus.OK)


@user_bp.get("/comments/<int:user_id>")
def get_user_comments(user_id):
    return make_response(
        jsonify(user_services.get_comments(user_id)), HTTPStatus.OK
    )


@user_bp.get("/images/<int:user_id>")
def get_user_images(user_id):
    return make_response(
        jsonify(user_services.get_images(user_id)), HTTPStatus.OK
    )
