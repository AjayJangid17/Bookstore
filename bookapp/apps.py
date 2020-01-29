from django.apps import AppConfig
# from . import signals

class BookappConfig(AppConfig):
    name = 'bookapp'


    def ready(self):
        import bookapp.signals


