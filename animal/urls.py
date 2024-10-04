from django.urls import path
from . import views

urlpatterns = [
    path('animals/', views.animal_list, name='animal_list'),
    path('animals/<int:pk>', views.detail_animal, name='detail_animal'),
    path('animals/new/', views.create_animal, name='create_animal'),
    path('animals/<int:pk>/edit/', views.edit_animal, name='edit_animal'),
    path('animals/<int:pk>/delete/', views.delete_animal, name='delete_animal'),
]
