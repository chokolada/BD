from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .goods.categories_route import categories_bp
    from .goods.categories_goods_route import categories_goods_bp
    from .goods.delivery_route import delivery_bp
    from .goods.description_route import description_bp
    from .goods.goods_route import goods_bp
    from .goods.goods_user_route import goods_user_bp
    from .user.basket_route import basket_bp
    from .user.basket_has_goods_route import basket_has_goods_bp
    from .user.reviews_route import reviews_bp
    from .user.user_route import user_bp

    app.register_blueprint(categories_bp)
    app.register_blueprint(categories_goods_bp)
    app.register_blueprint(delivery_bp)
    app.register_blueprint(description_bp)
    app.register_blueprint(goods_bp)
    app.register_blueprint(goods_user_bp)
    app.register_blueprint(basket_bp)
    app.register_blueprint(basket_has_goods_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(user_bp)

