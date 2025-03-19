from abc import ABC, abstractmethod


class NotificationSender(ABC):
    def __init__(self):
        self.is_under_maintenance = False

    @abstractmethod
    def send(self, message: str):
        pass


class EmailSender(NotificationSender):
    def send(self, message: str):
        print(f"Sending email with message: {message}")


class SMSSender(NotificationSender):
    def send(self, message: str):
        print(f"Sending SMS with message: {message}")


class PushSender(NotificationSender):
    def send(self, message: str):
        print(f'Sending Push notification with message: {message}.')


class NotificationService:
    UNDER_MAINT_MSG = 'This service is currently under maintenance'

    def __init__(self, sender: "NotificationSender"):
        self.sender = sender

    def notify(self, text: str):
        if not self.sender.is_under_maintenance:
            return self.sender.send(text)
        else:
            print(self.UNDER_MAINT_MSG)


email_sender = EmailSender()
sms_sender = SMSSender()
push_sender = PushSender()

push_sender.is_under_maintenance = True
"""
The status change represents manual toggling done by an admin or a developer 
when they know a system component is under maintenance.
In more complex systems, this would be automated or pulled from an external source.
"""
email_service = NotificationService(email_sender)
sms_service = NotificationService(sms_sender)
push_service = NotificationService(push_sender)

email_service.notify('Hello via email!')
sms_service.notify('Hello via SMS!')
push_service.notify('Hello via Push!')
