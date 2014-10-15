from django.shortcuts import render
from . models import Athlete

def index(request):
  athletes = Athlete.objects.all()
  return render(request, 'athletes/index.html', {'athletes': athletes})