from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class CmsConfig(AppConfig):
    name = 'cms'

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'