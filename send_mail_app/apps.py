from django.apps import AppConfig


class SendMailAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'send_mail_app'

    def ready(self):
        import send_mail_app.signals
