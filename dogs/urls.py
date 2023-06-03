from django.urls import path
from .views import DogListView

urlpatterns = [
    path('', DogListView.as_view(), name='dogs_list_view')
]
