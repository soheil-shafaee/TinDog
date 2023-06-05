from django.urls import path
from .views import DogListView, dog_details_view

urlpatterns = [
    path('', DogListView.as_view(), name='dogs_list_view'),
    path('<int:pk>', dog_details_view, name='dogs_detail_view'),
]
