from django.shortcuts import render, get_object_or_404, redirect
from adopter.models import Adopter
from .forms import AdopterForm


def adopter_list(request):
    adopters = Adopter.objects.all()
    return render(request, 'adopter_list.html', {'adopters': adopters})


def detail_adopter(request, pk):
    adopter = get_object_or_404(Adopter, pk=pk)
    return render(request, 'detail_adopter.html', {'adopter': adopter})


def create_adopter(request):
    if request.method == 'POST':
        form = AdopterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adopter_list')
        else:
            form = AdopterForm()
        return render(request, 'create_Adopter.html', {'form': form})


def edit_adopter(request, pk):
    adopter = get_object_or_404(Adopter, pk=pk)
    if request.method == 'POST':
        form = AdopterForm(request.POST, request.FILES, instance=adopter)
        if form.is_valid():
            form.sava()
            return redirect('adopter_list')
    else:
        form = AdopterForm(instance=adopter)
    return render(request, 'edit_adopter.html', {'form': form, 'adopter': adopter})


def delete_adopter(request, pk):
    adopter = get_object_or_404(Adopter, pk=pk)
    if request.method == 'POST':
        adopter.delete()
        return redirect('adopter_list')
    return render(request, 'confirm_delete.html', {'adopter': adopter})
