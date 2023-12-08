from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.goods.description import Description


class DescriptionDao(GeneralDAO):
    _domain_type = Description
