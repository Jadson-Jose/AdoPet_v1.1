from django.urls import path
from . import views

urlpatterns = [
    path('shelters/', views.shelter_list, name='shelter_list'),
    path('shelters/<int:pk>', views.detail_shelter, name='detail_shelter'),
    path('shelters/new_shelter/', views.create_shelter, name='create_shelter'),
    path('shelters/<int:pk>/edit_shelter/', views.edit_shelter, name='edit_shelter'),
    path('shelters/<int:pk>/delete_shelter/', views.delete_shelter, name='delete_shelter'),
]
