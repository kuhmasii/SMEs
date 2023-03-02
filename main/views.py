from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'index.html')

def about(request):
	return render(request, 'about.html')


def enterprise(request):
	return render(request,'enterprise.html')

def medium(request):
	return render(request, 'medium.html')

def small(request):
	return render(request, 'small.html')