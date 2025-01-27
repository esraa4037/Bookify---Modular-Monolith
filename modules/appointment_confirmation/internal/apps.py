from django.apps import AppConfig
from .confirmation_init import initialize_confirmation_module

class ConfirmationModuleConfig(AppConfig):
    name = 'modules.appointment_confirmation.internal'

    def ready(self):
        """
        Initialize the Confirmation Module when the application starts.
        """
        initialize_confirmation_module()
