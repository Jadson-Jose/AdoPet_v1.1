from django.shortcuts import render, get_object_or_404, redirect
from adoption.models import Adoption
from .forms import AdoptionForm


def adoption_list(request):
    adoption = Adoption.objects.all()
    return render(request, 'adoption_list.html', {'adoption': adoption})


def detail_adoption(request, pk):
    adoption = get_object_or_404(Adoption, pk=pk)
    return render(request, 'detail_adoption.html', {'adoption': adoption})
