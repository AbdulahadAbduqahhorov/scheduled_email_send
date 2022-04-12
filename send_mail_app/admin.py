from django.contrib import admin
from send_mail_app.models import SendEmail, RecieverEmail

admin.site.register(SendEmail)
admin.site.register(RecieverEmail)
