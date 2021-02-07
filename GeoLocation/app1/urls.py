from django.urls import path
from .views import home, export_users_xls

urlpatterns = [
    path('', home, name='home'),
    path('export/', export_users_xls, name='export_user_xls'),
]