from django.urls import path
from three.views import one, two, three

urlpatterns = [
    path('three_index', one),
    path('three_two', two),
    path('three_three', three)
]