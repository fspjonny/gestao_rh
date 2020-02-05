from django.urls import path
from .views import inicio,saiu

urlpatterns = [
    path('', inicio, name='inicio'),
    path('accounts/', saiu, name='saiu'),
]
