import logging.config
from .extend import InputValidationDecorator
from .handlers import OrdersNamePrinciple, OrdersPricePrinciple, OrdersCurrencyPrinciple, OrdersValidation
from rest_framework.views import APIView
from rest_framework.response import Response


log = logging.getLogger(__name__)


class OrdersValidationView(APIView):  ## 繼承APIView 不需檢查Http Method, 這邊POST以外訪問不到

    @InputValidationDecorator().extendfunc
    def post(self, request, payload, *args, **kwargs):
        
        name = payload.get("name")
        price = payload.get("price")
        currency = payload.get("currency")

        name_ins = OrdersNamePrinciple(name)
        price_ins = OrdersPricePrinciple(price)
        currency_ins = OrdersCurrencyPrinciple(currency, price_ins)
        
        orders_validation = OrdersValidation(name_ins, price_ins, currency_ins)
        orders_validation.validate()

        if orders_validation.name_non_english:
            return Response("Name contains non-English characters", status=400)

        if orders_validation.name_not_capitalized:
            return Response("Name is not capitalized", status=400)

        if orders_validation.price_over:
            return Response("Price is over 2000", status=400)

        if orders_validation.currency_format:
            return Response("Currency format is wrong", status=400)

        return Response("Order is valid", status=200)