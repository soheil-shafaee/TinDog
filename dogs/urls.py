from django.urls import path
from .views import DogListView, dog_details_view, DogCreateView, DogUpdateView, DogDeleteView

urlpatterns = [
    path('', DogListView.as_view(), name='dogs_list_view'),
    path('<int:pk>', dog_details_view, name='dogs_detail_view'),
    path('create_your_account/', DogCreateView.as_view(), name='dog_create_view'),
    path('<int:pk>/edit', DogUpdateView.as_view(), name='dog_update_view'),
    path('<int:pk>/delete_dog', DogDeleteView.as_view(), name='dog_delete_view'),
]
