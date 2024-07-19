import logging.config
from .extend import InputValidationDecorator
from .handlers import OrdersNamePrinciple, OrdersPricePrinciple, OrdersCurrencyPrinciple
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
        valid_name = name_ins.func()

        if valid_name.get('msg') == "Name contains non-English characters":
            return Response("Name contains non-English characters", status=400)
        
        if valid_name.get('msg') == "Name is not capitalized":
            return Response("Name is not capitalized", status=400)

        currency_ins = OrdersCurrencyPrinciple(currency, price)
        valid_currency = currency_ins.func()

        if valid_currency.get('msg') == "Currency format is wrong":
            return Response("Currency format is wrong", status=400)

        price_ins = OrdersPricePrinciple(currency_ins.price)   ## 傳入轉換後的price
        valid_price = price_ins.func()

        if valid_price.get('msg') == "Price is over 2000":
            return Response("Price is over 2000", status=400)

        return Response("Order is valid", status=200)