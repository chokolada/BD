from http import HTTPStatus
from flask import abort
from mydb.auth.dao import delivery_dao
from mydb.auth.service.general_service import GeneralService


class DeliveryService(GeneralService):
    _dao = delivery_dao
