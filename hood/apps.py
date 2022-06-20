from django.apps import AppConfig


class HoodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hood'

    # def ready(self):
    #     import users.signals   #noqa
