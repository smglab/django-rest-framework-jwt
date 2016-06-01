from django.apps import apps as django_apps
from rest_framework_jwt.settings import api_settings


def jwt_get_user_model():
    return django_apps.get_model(api_settings.JWT_USER_MODEL)
