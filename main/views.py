from django.shortcuts import render, get_object_or_404
from django.http import Http404
from . models import Loan, Service, Blog

def index(request):
	services = Service.objects.all()

	context = {'services':services}
	return render(request, 'main/index.html', context)

def about(request):
	return render(request, 'main/about.html')

def enterprise(request):
	loans = Loan.objects.filter(loan_type__iexact='enterprise')
	blogs = Blog.objects.select_related('loan').filter(loan__loan_type='enterprise')

	context = {'loans':loans, 'loan_type':'Enterprise', 'blogs':blogs}
	return render(request,'main/loan.html', context)

def medium(request):
	loans = Loan.objects.filter(loan_type__iexact='medium')
	blogs = Blog.objects.select_related('loan').filter(loan__loan_type='medium')

	context = {'loans':loans, 'loan_type':'Medium', 'blogs':blogs}
	return render(request, 'main/loan.html', context)

def small(request):
	
	loans = Loan.objects.filter(loan_type='small')
	blogs = Blog.objects.select_related('loan').filter(loan__loan_type='small')

	context = {'loans':loans, 'loan_type':'Small', 'blogs':blogs}
	return render(request, 'main/loan.html', context)

def loan_detail(request, loan_id=None):
	
	if loan_id is not None:
		loan = get_object_or_404(Loan, id=loan_id)
		blogs = Blog.objects.select_related('loan').filter(loan=loan)
		
		context = {'loan':loan, 'blogs':blogs}
		return render(request, 'main/detail.html', context)
	# return http404

def full_blog_details(request, id=None):

	if id is not None:
		try:
			blog = Blog.objects.select_related('loan', 'service').get(id=id)
			blogs = Blog.objects.select_related('loan', 'service').all()[:6]
			services = Service.objects.all()
		except blog.DoesNotExist:
			raise Http404
		context = {'blog':blog, 'blogs':blogs, "services":services}
		return render(request, 'main/full_blog_detail.html', context)
	# return Http404


def service(request, service=None):
	
	if service is not None:
		service = Service.objects.get(name__iexact=service)
		filters = Blog.objects.filter(service=service)
		context = {'service':service, 'filters':filters}
		
		return render(request, 'main/blog.html', context)
	else: 
		service = Service.objects.all()

	context = {'service':service}
	return render(request, 'main/services.html', context)
	
