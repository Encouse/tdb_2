from django.apps import AppConfig


class AuthlocConfig(AppConfig):
    name = 'authloc'
    def ready(self):
        from . import signals
