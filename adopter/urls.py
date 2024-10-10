from django.urls import path
from . import views

urlpatterns = [
    path('adopters/', views.adopter_list, name='adopter_list'),

]
