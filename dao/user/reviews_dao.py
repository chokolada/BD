from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.user.reviews import Reviews


class ReviewsDao(GeneralDAO):
    _domain_type = Reviews
