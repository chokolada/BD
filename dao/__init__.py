from .goods.categories_dao import CategoriesDao
from .goods.categories_goods_dao import CategoriesGoodsDao
from .goods.delivery_dao import DeliveryDao
from .goods.description_dao import DescriptionDao
from .goods.goods_dao import GoodsDao
from .goods.goods_user_dao import GoodsUserDao
from .user.basket_dao import BasketDao
from .user.basket_has_goods_dao import BasketHasGoodDao
from .user.reviews_dao import ReviewsDao
from .user.user_dao import UserDao

categories_dao = CategoriesDao()
categories_goods_dao = CategoriesGoodsDao()
delivery_dao = DeliveryDao()
description_dao = DescriptionDao()
goods_dao = GoodsDao()
goods_user_dao = GoodsUserDao()
basket_dao = BasketDao()
basket_has_goods_dao = BasketHasGoodDao()
reviews_dao = ReviewsDao()
user_dao = UserDao()
