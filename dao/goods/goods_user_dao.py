from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.goods.goods_user import GoodsUser


class GoodsUserDao(GeneralDAO):
    _domain_type = GoodsUser
