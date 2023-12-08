from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.user.user import User


class UserDao(GeneralDAO):
    _domain_type = User
