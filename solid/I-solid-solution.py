# Here your solution

from abc import ABC, abstractmethod

# Creamos interfaces que se necesiten(Interfaces específicas)


class IPaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


class Refunds(ABC):
    @abstractmethod
    def refund(self, amount: float) -> None:
        pass


class Handlerdispute(ABC):
    @abstractmethod
    def handle_dispute(self, dispute_id: str) -> None:
        pass