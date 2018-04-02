from django.apps import AppConfig


class HtConfig(AppConfig):
    name = 'ht'

    def ready(self):
        from .import signals
