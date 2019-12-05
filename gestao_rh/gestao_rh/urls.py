from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.core.urls'), name='inicio'),
    path('colaboradores/', include('apps.colaboradores.urls'), name='colaboradores'),
    path('admin/', admin.site.urls),
]
