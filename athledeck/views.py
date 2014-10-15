from django.shortcuts import get_object_or_404, render
from . models import Athlete

def index(request):
  athletes = Athlete.objects.all()
  return render(request, 'athletes/index.html', {'athletes': athletes})

def show(request, pk):
  athlete = get_object_or_404(Athlete, pk=pk)
  return render(request, 'athletes/show.html', {'athlete': athlete})