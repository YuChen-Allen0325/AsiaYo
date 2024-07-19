from abc import ABC, abstractmethod
from rest_framework.response import Response


class Principle(ABC):
    @abstractmethod
    def func(self):
        pass


class OrdersNamePrinciple(Principle):
    def __init__(self, name):
        self.name = name

    def func(self):
        capital_index = 0
        capital_list = []
        flag = 1

        if not self.name.replace(" ", "").isalpha():
            return {"msg":"Name contains non-English characters"}

        while flag:   ## 抓取空白後的字母index, 如果字串未含空白則另外處理

            capital_index = self.name.find(" ", capital_index)

            if capital_index == -1:
                flag = 0

            capital_index += 1
            capital_list.append(capital_index)
        
        if len(capital_list) == 1: ## 未含空白 -> 第一個字就一定為大寫
            if not (ord(self.name[0]) >= 65 and ord(self.name[0]) <= 90): 
                return {"msg":"Name is not capitalized"}
        else:
            capital_list.pop()  ## 過濾掉最後一個找不到空白的index

            if not ((ord(self.name[0]) >= 65 and ord(self.name[0]) <= 90) or self.name[0] == " "): 
                return {"msg":"Name is not capitalized"}

            for i in capital_list:
                if not ((ord(self.name[i]) >= 65 and ord(self.name[i]) <= 90) or self.name[i] == " "): 
                    return {"msg":"Name is not capitalized"}
                
        return {}


class OrdersPricePrinciple(Principle):   ##  最後檢查價格
    def __init__(self, price):
        self.price = price
        
    def func(self):
        if int(self.price) > 2000:
            return {"msg":"Price is over 2000"}

        return {}
    

class OrdersCurrencyPrinciple(Principle):
    def __init__(self, currency, price_principle: OrdersPricePrinciple):
        self.currency = currency
        self.price_principle = price_principle

    def func(self):
        
        if self.currency not in ["USD", "TWD"]:
            return {"msg":"Currency format is wrong"}
        
        if self.currency == "USD":
            self.price_principle.price = str(int(self.price_principle.price) * 31)
            self.currency = "TWD"
        
        return {}
    
class OrdersValidation:
    def __init__(self, name_principle: OrdersNamePrinciple, price_principle: OrdersPricePrinciple, currency_principle: OrdersCurrencyPrinciple):
        self.name_principle = name_principle
        self.price_principle = price_principle
        self.currency_principle = currency_principle

        self.name_non_english = False      ## True就是有錯誤
        self.name_not_capitalized = False
        self.currency_format = False
        self.price_over = False
    
    def validate(self):

        valid_name = self.name_principle.func()
        valid_currency = self.currency_principle.func()
        valid_price = self.price_principle.func()

        if valid_name.get('msg') == "Name contains non-English characters":
            self.name_non_english = True
        
        if valid_name.get('msg') == "Name is not capitalized":
            self.name_not_capitalized = True

        if valid_currency.get('msg') == "Currency format is wrong":
            self.currency_format = True

        if valid_price.get('msg') == "Price is over 2000":
            self.price_over = True
        
        return