from abc import ABC, abstractmethod

# ----------------------------
# Order Classes
# ----------------------------
class Order(ABC):
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

    @abstractmethod
    def get_order_type(self):
        pass


class RegularOrder(Order):
    def get_order_type(self):
        return "Regular Order"


class DiscountedOrder(Order):
    def get_order_type(self):
        return "Discounted Order"


class PriorityOrder(Order):
    def get_order_type(self):
        return "Priority Order"


# ----------------------------
# Payment Interfaces & Classes
# ----------------------------
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid Rs.{amount} using Credit Card")


class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid Rs.{amount} using UPI")


class WalletPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid Rs.{amount} using Wallet")


# ----------------------------
# Notification Interfaces
# ----------------------------
class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass


class EmailNotification(NotificationService):
    def send_notification(self, message):
        print(f"Email Notification: {message}")


class SMSNotification(NotificationService):
    def send_notification(self, message):
        print(f"SMS Notification: {message}")


class PushNotification(NotificationService):
    def send_notification(self, message):
        print(f"Push Notification: {message}")


# ----------------------------
# Storage Interfaces
# ----------------------------
class StorageService(ABC):
    @abstractmethod
    def save_order(self, order):
        pass


class DatabaseStorage(StorageService):
    def save_order(self, order):
        print(f"Order {order.order_id} saved in Database")


class FileStorage(StorageService):
    def save_order(self, order):
        print(f"Order {order.order_id} saved in File")


# ----------------------------
# Order Service
# ----------------------------
class OrderService:
    def __init__(self, payment_method, notification_service, storage_service):
        self.payment_method = payment_method
        self.notification_service = notification_service
        self.storage_service = storage_service

    def process_order(self, order):
        print(f"\nProcessing {order.get_order_type()}")
        print(f"Order ID: {order.order_id}")
        print(f"Order Amount: Rs.{order.amount}")

        self.payment_method.pay(order.amount)

        self.notification_service.send_notification(
            f"Order {order.order_id} processed successfully"
        )

        self.storage_service.save_order(order)


# ----------------------------
# Main Program
# ----------------------------
if __name__ == "__main__":
    order = PriorityOrder(101, 5000)

    payment = UPIPayment()
    notification = EmailNotification()
    storage = DatabaseStorage()

    service = OrderService(payment, notification, storage)
    service.process_order(order)
