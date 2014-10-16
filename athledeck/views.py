from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
from .models import Athlete
from .forms import AthleteForm

def index(request):
  athletes = Athlete.objects.order_by('last_name')
  return render(request, 'athletes/index.html', {'athletes': athletes})

def show(request, pk):
  athlete = get_object_or_404(Athlete, pk=pk)
  return render(request, 'athletes/show.html', {'athlete': athlete})

def new(request):
  if request.method == "POST":
    form = AthleteForm(request.POST)
    if form.is_valid():
      athlete = form.save()
      return redirect('athledeck.views.show', pk=athlete.pk)
  else:
    form = AthleteForm()
  return render(request, 'athletes/edit.html', {'form': form})

def edit(request, pk):
  athlete = get_object_or_404(Athlete, pk=pk)
  if request.method == "POST":
    form = AthleteForm(request.POST, instance=athlete)
    if form.is_valid():
      athlete =form.save()
      return redirect('athledeck.views.show', pk=athlete.pk)
  else:
    form = AthleteForm(instance=athlete)
  return render(request, 'athletes/edit.html', {'form': form})

def destroy(request, pk):
  athlete = get_object_or_404(Athlete, pk=pk)
  athlete.delete()
  return redirect('athledeck.views.index')

