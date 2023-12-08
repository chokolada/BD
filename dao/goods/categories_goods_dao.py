from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.goods.categories_goods import CategoriesGoods


class CategoriesGoodsDao(GeneralDAO):
    _domain_type = CategoriesGoods
