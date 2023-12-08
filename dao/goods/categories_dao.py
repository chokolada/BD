from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.goods.categories import Categories


class CategoriesDao(GeneralDAO):
    _domain_type = Categories
