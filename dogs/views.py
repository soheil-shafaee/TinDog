from django.shortcuts import render
from django.views import generic

from .models import Dog


class DogListView(generic.ListView):
    model = Dog
    template_name = 'dogs/dogs_list_view.html'
    context_object_name = 'dogs'
