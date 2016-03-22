from django.contrib import admin
from .models import Receta

# Register your models here.
#admin.site.register(Receta)

@admin.register(Receta)
class AdminReceta(admin.ModelAdmin):
	list_display = ('name', 'category', 'description',)
	list_filter = ('name', 'category',)