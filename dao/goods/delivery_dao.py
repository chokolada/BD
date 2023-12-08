from mydb.auth.dao.general_dao import GeneralDAO
from mydb.auth.domain.goods.delivery import Delivery


class DeliveryDao(GeneralDAO):
    _domain_type = Delivery
