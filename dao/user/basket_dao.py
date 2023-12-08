from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.user.basket import Basket


class BasketDao(GeneralDAO):
    _domain_type = Basket
