from functools import wraps
from abc import ABC, abstractmethod
from rest_framework.response import Response


class ExtendDecorator(ABC):   ## 抽象類別
    @abstractmethod
    def extendfunc(func):
        def wrapped_func(*args, **kwargs):
            pass
        return wrapped_func


class InputValidationDecorator(ExtendDecorator):  ## 檢查傳入值是否符合規範
    def __init__(self):
        pass

    def extendfunc(self, func):
        @wraps(func)
        def wrapped_func(self, request, *args, **kwargs):
            
            id = request.data.get("id")
            name = request.data.get("name")
            address = request.data.get("address", {})
            price = request.data.get("price")
            currency = request.data.get("currency")

            city = address.get("city")
            district = address.get("district")
            street = address.get("street")

            if id == None or name == None or address == {} or price == None or currency == None:
                return Response("Required parameters are missing", status=400)

            if type(id).__name__ != 'str':
                return Response("id must be a string", status=400)
            
            if type(name).__name__ != 'str':
                return Response("name must be a string", status=400)
            
            if type(address).__name__ != 'dict':
                return Response("address must be a dict", status=400)
            
            if type(price).__name__ != 'str':
                return Response("price must be a string", status=400)
            else:
                for p in price:
                    if not (ord(p) >= 48 and ord(p) <= 57):
                        return Response("price must be numeric", status=400)
            
            if type(currency).__name__ != 'str':
                return Response("currency must be a string", status=400)
            
            if address.get("city") is None or address.get("district") is None or address.get("street") is None:
                return Response("address must have city, district and street", status=400)
            
            if type(city).__name__ != 'str':
                return Response("city must be a string", status=400)
            
            if type(district).__name__ != 'str':
                return Response("district must be a string", status=400)
            
            if type(street).__name__ != 'str':
                return Response("street must be a string", status=400)

            payload = {
                "id": id,
                "name": name,
                "address": address,
                "price": price,
                "currency": currency
            }

            return func(self, request, payload, *args, **kwargs)
        return wrapped_func
