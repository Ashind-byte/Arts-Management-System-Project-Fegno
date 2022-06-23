from django.contrib import admin

# Register your models here.
from .models import Event, Registration
from .models import Winner

admin.site.register(Winner)
admin.site.register(Event)
admin.site.register(Registration)
