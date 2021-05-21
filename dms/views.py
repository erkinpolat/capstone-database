from django.shortcuts import render
from django.http import HttpResponse
from .models import Faculty, StudentJunior

# Create your views here.

def home(request):
	return render(request, 'dms/home.html')

def faculty(request):
	faculty=Faculty.objects.all()

	return render(request, 'dms/faculty.html', {'faculty': faculty})


def studentJunior(request):
	students=StudentJunior.objects.all()

	return render(request, 'dms/juniors.html', {'faculty': students})

