from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.goods.goods import Goods


class GoodsDao(GeneralDAO):
    _domain_type = Goods
