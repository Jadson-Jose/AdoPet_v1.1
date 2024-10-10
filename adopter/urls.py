from django.urls import path
from . import views

urlpatterns = [
    path('adopters/', views.adopter_list, name='adopter_list'),
    path('adopters/<int:pk>', views.detail_adopter, name='detail_adopter'),
    path('adopters/new_adopter/', views.create_adopter, name='create_adopter'),
    path('adopters/<int:pk>/edit_adopter', views.edit_adopter, name='edit_adopter'),
    path('adopters/<int:pk>/delete_adopter', views.delete_adopter, name='delete_adopter')

]
