from django.contrib import admin
from web.models import Pet

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'age')


admin.site.register(Pet, PetAdmin)