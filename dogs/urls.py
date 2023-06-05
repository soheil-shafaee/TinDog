from django.urls import path
from .views import DogListView, DogDetailView

urlpatterns = [
    path('', DogListView.as_view(), name='dogs_list_view'),
    path('<int:pk>', DogDetailView.as_view(), name='dog_detail_view'),
]
