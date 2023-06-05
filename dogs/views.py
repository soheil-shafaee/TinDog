from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Dog


class DogListView(generic.ListView):
    model = Dog
    template_name = 'dogs/dogs_list_view.html'
    context_object_name = 'dogs'


def dog_details_view(request, pk):
    # Dog profile view:
    dog = get_object_or_404(Dog, pk=pk)
    return render(request, 'dogs/dogs_detail_view.html', {
        'dog': dog
    })

