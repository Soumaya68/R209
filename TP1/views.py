from django.shortcuts import render, get_object_or_404, redirect
from .models import Voiture
from .forms import VoitureForm

def index(request):
    voitures = Voiture.objects.all()
    return render(request, 'voitures/index.html', {'voitures': voitures})

def detail(request, id):
    voiture = get_object_or_404(Voiture, pk=id)
    return render(request, 'voitures/detail.html', {'voiture': voiture})

def ajouter(request):
    if request.method == "POST":
        form = VoitureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VoitureForm()
    return render(request, 'voitures/form.html', {'form': form, 'action': 'Ajouter'})

def modifier(request, id):
    voiture = get_object_or_404(Voiture, pk=id)
    if request.method == "POST":
        form = VoitureForm(request.POST, instance=voiture)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VoitureForm(instance=voiture)
    return render(request, 'voitures/form.html', {'form': form, 'action': 'Modifier'})

def supprimer(request, id):
    voiture = get_object_or_404(Voiture, pk=id)
    voiture.delete()
    return redirect('index')
