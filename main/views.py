from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'main/index.html')

def about(request):
	return render(request, 'main/about.html')

def enterprise(request):
	return render(request,'main/enterprise.html')

def medium(request):
	return render(request, 'main/medium.html')

def small(request):
	return render(request, 'main/small.html')

def business_plan(request):
	return render(request, 'main/business.html')


def service(request):
	return render(request, 'main/services.html')


def detail_small(request):
	return render(request, 'main/detail.html')

def detail_medium(request):
	return render(request, 'main/detail.html')

def detail_enterprise(request):
	return render(request, 'main/detail.html')


