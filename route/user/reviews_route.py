from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from mydb import db
from mydb.auth.service import reviews_services
from mydb.auth.domain.user.reviews import Reviews

reviews_bp = Blueprint("reviews", __name__, url_prefix="/reviews/")


@reviews_bp.get("")
def get_all_reviews() -> Response:
    reviews = reviews_services.find_all()

    # Convert Review objects to dictionaries
    reviews_data = [review.put_into_dto() for review in reviews]

    return make_response(jsonify(reviews_data), HTTPStatus.OK)



@reviews_bp.get("/<int:reviews_id>")
def get_reviews(reviews_id: int) -> Response:
    return make_response(
        jsonify(reviews_services.find_by_id(reviews_id)), HTTPStatus.OK
    )


@reviews_bp.put("/<int:reviews_id>")
def update_reviews(reviews_id: int) -> Response:
    content = request.get_json()
    reviews = Reviews.create_from_dto(content)
    reviews_services.update(reviews_id, reviews)
    return make_response("Reviews updated", HTTPStatus.OK)


@reviews_bp.patch("/<int:reviews_id>")
def patch_reviews(reviews_id: int) -> Response:
    content = request.get_json()
    reviews_services.patch(reviews_id, content)
    return make_response("Reviews updated", HTTPStatus.OK)


@reviews_bp.delete("/<int:reviews_id>")
def delete_reviews(reviews_id: int) -> Response:
    reviews_services.delete(reviews_id)
    return make_response("Reviews deleted", HTTPStatus.OK)


@reviews_bp.post("")
def create_reviews() -> Response:
    content = request.get_json()
    reviews = Reviews.create_from_dto(content)
    reviews_id = reviews_services.create(reviews)
    return make_response(
        f"Reviews created with ID: {reviews_id}", HTTPStatus.CREATED
    )


@reviews_bp.post("/bulk")
def create_all_reviews() -> Response:
    content = request.get_json()
    reviews = [Reviews.create_from_dto(data) for data in content]
    reviews_services.create_all(reviews)
    return make_response(reviews_services.create_all(reviews), HTTPStatus.CREATED)


@reviews_bp.delete("/all")
def delete_all_reviews() -> Response:
    reviews_services.delete_all()
    return make_response("All Reviewss deleted", HTTPStatus.OK)


@reviews_bp.get("/comments/<int:reviews_id>")
def get_reviews_comments(reviews_id):
    return make_response(
        jsonify(reviews_services.get_comments(reviews_id)), HTTPStatus.OK
    )


@reviews_bp.get("/images/<int:reviews_id>")
def get_reviews_images(reviews_id):
    return make_response(
        jsonify(reviews_services.get_images(reviews_id)), HTTPStatus.OK
    )
