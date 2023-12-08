from mydb.auth.controller.general_controller import GeneralController
from mydb.auth.service import categories_services


class CategoriesController(GeneralController):
    _service = categories_services

    def get_category_info(self, id: int):
        return self._service.get_category_info(id)
