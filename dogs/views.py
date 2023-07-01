from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

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


class DogCreateView(generic.CreateView):
    models = Dog
    fields = ['name', 'breed', 'age', 'sex', 'vaccinated', 'children', 'explain', 'location', 'dog_photo']
    template_name = 'dogs/dog_create_view.html'

    def get_queryset(self):
        return Dog.objects.filter()


class DogUpdateView(generic.UpdateView):
    models = Dog
    fields = ['name', 'breed', 'age', 'sex', 'vaccinated', 'children', 'explain', 'location', 'dog_photo']
    template_name = 'dogs/dog_update_view.html'

    def get_queryset(self):
        return Dog.objects.filter()


class DogDeleteView(generic.DeleteView):
    models = Dog
    template_name = 'dogs/dog_delete_view.html'
    success_url = reverse_lazy('dogs_list_view')

    def get_queryset(self):
        return Dog.objects.filter()
