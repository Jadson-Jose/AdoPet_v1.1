from django.shortcuts import render, redirect, get_object_or_404
from shelter.models import Shelter
from .forms import ShelterForm


def shelter_list(request):
    shelters = Shelter.objects.all()
    return render(request, 'shelter_list.html', {'shelters': shelters})


def detail_shelter(request, pk):
    shelter = get_object_or_404(Shelter, pk=pk)
    return render(request, 'detail_shelter.html', {'shelter': shelter})


def create_shelter(request):
    if request == 'POST':
        form = ShelterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shelter_list')
    else:
        form = ShelterForm()
    return render(request, 'create_shelter.html', {'form': form})


def edit_shelter(request, pk):
    shelter = get_object_or_404(Shelter, pk=pk)
    if request.method == 'POST':
        form = ShelterForm(request.POST, request.FILES, instance=shelter)
        if form.is_valid():
            form.save()
            return redirect('shelter_list')
    else:
        form = ShelterForm(instance=shelter)
    return render(request, 'edit_shelter.html', {'form': form, 'shelter': shelter})


def delete_shelter(request, pk):
    shelter = get_object_or_404(Shelter, pk=pk)
    if request.method == 'POST':
        shelter.delete()
        return redirect('shelter_list')
    return render(request, 'delete_shelter.html', {'shelter': shelter})
