from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.user.basket_has_goods import BasketHasGoods


class BasketHasGoodDao(GeneralDAO):
    _domain_type = BasketHasGoods
