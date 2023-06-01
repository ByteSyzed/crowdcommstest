from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import RabbitHole, Bunny

admin.site.register(RabbitHole)
admin.site.register(Bunny)

