from django.shortcuts import render
from . models import Loan, Service, Blog

def index(request):
	services = Service.objects.all()

	context = {'services':services}
	return render(request, 'main/index.html', context)

def about(request):
	return render(request, 'main/about.html')


def enterprise(request):
	loans = Loan.objects.filter(loan_type__iexact='enterprise')
	if loans.exists():
		context = {'loans':loans, 'loan_type':'Enterprise'}
		return render(request,'main/loan.html', context)
	# return a 404 page

def medium(request):
	loans = Loan.objects.filter(loan_type__iexact='medium')
	if loans.exists():
		context = {'loans':loans, 'loan_type':'Medium'}
		return render(request, 'main/loan.html', context)
	# return a 404 page


def small(request):
	loans = Loan.objects.filter(loan_type__iexact='small')

	if loans.exists():
		context = {'loans':loans, 'loan_type':'Small'}
		return render(request, 'main/loan.html', context)
	# return a 404 page


def service(request, service=None):

	if service:
		service = Service.objects.get(name__iexact=service)
		filters = Blog.objects.filter(service=service)
		context = {'service':service, 'filters':filters}
		
		return render(request, 'main/blog.html', context)
	else: 
		service = Service.objects.all()

	context = {'service':service}
	return render(request, 'main/services.html', context)


def detail_small(request):
	return render(request, 'main/detail.html')

def detail_medium(request):
	return render(request, 'main/detail.html')

def detail_enterprise(request):
	return render(request, 'main/detail.html')


