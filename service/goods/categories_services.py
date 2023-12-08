from http import HTTPStatus
from flask import abort
from mydb.auth.dao import categories_dao
from mydb.auth.service.general_service import GeneralService


class CategoriesService(GeneralService):
    _dao = categories_dao
