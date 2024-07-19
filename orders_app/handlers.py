from abc import ABC, abstractmethod

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
    def __init__(self, currency, price):
        self.currency = currency
        self.price = price

    def func(self):
        
        if self.currency not in ["USD", "TWD"]:
            return {"msg":"Currency format is wrong"}
        
        if self.currency == "USD":
            self.price = str(int(self.price) * 31)
            self.currency = "TWD"
        
        return {}