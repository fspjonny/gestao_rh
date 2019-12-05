from django.contrib import admin
from .models import RegistroHoraExtra

class FizeramHorasExtras(admin.ModelAdmin):
    list_display = ('colaborador', 'motivo')
    list_filter = ['colaborador',]

admin.site.register(RegistroHoraExtra, FizeramHorasExtras)

