from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered


def auto_register(app_name: str):
    """
    Если у модели есть подкласс Admin
    то этот скрипт автоматически подключает в админку все такие модели из приложения app_name
    """
    for model in apps.get_app_config(app_name).get_models():
        try:
            admin_cls = getattr(model, 'Admin', None)
            if not admin_cls:
                continue
            if hasattr(admin_cls, 'before_register'):
                admin_cls.before_register()
            admin.site.register(model, admin_cls)
        except AlreadyRegistered:
            print('model_admin_already_registered')
