from django.urls import path
from two.views import index, two, three

urlpatterns = [
    path('two_index', index),
    path('two_two', two),
    path('two_three', three)
]