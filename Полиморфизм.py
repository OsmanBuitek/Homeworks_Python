from abc import ABC, abstractmethod

# 1. Абстрактный класс PaymentMethod
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount:float):
        """"Абстрактный метод для проведения оплаты"""
        pass

# 2 & 3. Классы конкретных способов оплаты и их логика
class KaspiPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"Оплата через Kaspi на сумму {amount}")

class CardPayment(PaymentMethod):
    def pay(self, amount: float):
        print(f"Оплата картой на сумму {amount}")

class BonusPayment(PaymentMethod):
    def pay(self, amount: float):
        if amount > 5000:
            print("Бонусами нельзя оплатить больше 5000")
        else:
            print(f"Оплата бонусами на сумму {amount}")

class CryptoPaymentMock(PaymentMethod):
    def pay(self, amount: float):
        print(f"Имитация оплаты криптовалютой на сумму {amount}")

# 4. Класс OrderService
class OrderService:
    def process_order(self, amount: float, payment_method: PaymentMethod):
        # Сервис не знает, какой именно класс пришел, но уверен,
        # что у него есть метод pay() благодаря наследованию от PaymentMethod
        payment_method.pay(amount)

# 5. Пример использования
if __name__ == "__main__":
    # Создаем объекты способов оплаты
    kaspi = KaspiPayment()
    card = CardPayment()
    bonus = BonusPayment()
    crypto = CryptoPaymentMock()

    # Создаем объект сервиса
    order_service = OrderService()

    # Проверяем работу системы
    order_service.process_order(3000, kaspi)
    order_service.process_order(7000, card)
    order_service.process_order(6000, bonus)
    order_service.process_order(4000, bonus)
    order_service.process_order(10000, crypto)
    
