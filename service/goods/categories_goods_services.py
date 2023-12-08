from http import HTTPStatus
from flask import abort
from mydb.auth.dao import categories_goods_dao
from mydb.auth.service.general_service import GeneralService


class CategoriesGoodsService(GeneralService):
    _dao = categories_goods_dao
