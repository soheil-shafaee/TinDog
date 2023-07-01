from django.contrib import admin

from .models import Dog


class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'sex', 'vaccinated', )


admin.site.register(Dog, DogAdmin)
