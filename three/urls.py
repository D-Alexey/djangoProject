from django.urls import path
from three.views import index, two, three

urlpatterns = [
    path('three_index', index),
    path('three_two', two),
    path('three_three', three)
]