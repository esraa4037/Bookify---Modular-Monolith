class NotificationService:
    def send_notification(self, recipient_name: str, message: str):
        """
        Send a notification to the recipient (patient or doctor).
        """
        print(f"Sending notification to {recipient_name}...\n{message}\n")
