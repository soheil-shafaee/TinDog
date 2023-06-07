from django.urls import path
from .views import DogListView, dog_details_view, DogCreateView

urlpatterns = [
    path('', DogListView.as_view(), name='dogs_list_view'),
    path('<int:pk>', dog_details_view, name='dogs_detail_view'),
    path('create_your_account/', DogCreateView.as_view(), name='dog_create_view'),
]
