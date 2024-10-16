from django.urls import path
from . import views

urlpatterns = [
    path('animals/', views.animal_list, name='animal_list'),
    path('animals/<int:pk>', views.detail_animal, name='detail_animal'),
    path('animals/create_animal/', views.create_animal, name='create_animal'),
    path('animals/<int:pk>/edit_animal/', views.edit_animal, name='edit_animal'),
    path('animals/<int:pk>/delete_animal/', views.delete_animal, name='delete_animal'),
]
