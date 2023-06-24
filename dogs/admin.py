from django.contrib import admin

from .models import Dog


class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'gender', 'vaccinated', )


admin.site.register(Dog, DogAdmin)
