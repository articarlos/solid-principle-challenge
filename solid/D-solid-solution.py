# Here your solution
# Implementando "Unica responsabilidad"

class PayPalService:
    @staticmethod
    def pay(amount: float):
        print(f"Paying {amount} using PayPal...")

# separamos la creación del servicio de pago del procesamiento


class PaymentProcessor:
    def __init__(self, pay_service):
        self.pay_service = pay_service

    def process_payment(self, amount: float):
        self.pay_service.pay(amount)