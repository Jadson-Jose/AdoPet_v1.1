from django.shortcuts import render, get_object_or_404, redirect
from .models import Animal
from .forms import AnimalForms


def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'list.html', {'animals': animals})


def detail_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'detail.html', {'animal': animal})


def create_animal(request):
    if request.method == 'POST':
        form = AnimalForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('animals_list')
    else:
        form = AnimalForms()
    return render(request, 'form.html', {'form': form})


def edit_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        form = AnimalForms(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animal_list', pk=pk)
    else:
        form = AnimalForms(instance=animal)
    return render(request, 'edit_animal.html', {'form': form, 'animal':animal})



def delete_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        animal.delete()
        return redirect('list_animal')
    return render(request, 'confirm_delete.html', {'animal': animal})
