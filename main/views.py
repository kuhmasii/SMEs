from django.shortcuts import render, get_object_or_404
from django.http import Http404
from . models import Loan, Service, Blog
from . forms import LoanPredForm
from django.http import HttpResponse
# from.utils import ohevalue, approvereject
# import pandas as pd


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
	form = LoanPredForm()
	loan = get_object_or_404(Loan, id=loan_id)
	blogs = Blog.objects.select_related('loan').filter(loan=loan)
	context = {'loan':loan, 'blogs':blogs, 'form':form }
	return render(request, 'main/detail.html', context)

def loan_predict(request):
	if request.method == "POST":
		form = LoanPredForm(request.POST)
		if form.is_valid():
			Firstname = form.cleaned_data.get('firstname')
			Lastname = form.cleaned_data.get('lastname')
			Dependents = form.cleaned_data.get('Dependents')
			ApplicantIncome = form.cleaned_data.get('ApplicantIncome')
			CoapplicantIncome = form.cleaned_data.get('CoapplicantIncome')
			LoanAmount = form.cleaned_data.get('LoanAmount')
			Loan_Amount_Term  = form.cleaned_data.get('Loan_Amount_Term')
			Credit_History = form.cleaned_data.get('Credit_History')
			Gender  = form.cleaned_data.get('Gender')
			Married  = form.cleaned_data.get('Married')
			Education = form.cleaned_data.get('Education')
			Self_Employed  = form.cleaned_data.get('Self_Employed')
			Property_Area = form.cleaned_data.get('Property_Area')

			# myDict = request.POST.dict()
			# myDict.pop('csrfmiddlewaretoken')
			
			# df=pd.DataFrame(myDict, index=[0])
			# answer=approvereject(ohevalue(df))[0]
			# Xscalers=approvereject(ohevalue(df))[1]
			if ApplicantIncome > LoanAmount:
				return HttpResponse("Congrats! You are Eligible for this loan.\nLoan will be approved")
			elif int(df['LoanAmount'])<10000000:
				return HttpResponse('Invalid: Your Loan Request Exceeds 10 Niara million Limit')
			else:
				return HttpResponse('Opps! You are not Eligible for this loan.\nLoan will not be approved')

			# if answer.lower() == 'approved':
			# 	return HttpResponse("Congrats! You are Eligible for this loan.\nLoan will be approved")
			# elif int(df['LoanAmount'])<10000000:
			# 	return HttpResponse('Invalid: Your Loan Request Exceeds 10 Niara million Limit')
			# else:
			# 	return HttpResponse('Opps! You are not Eligible for this loan.\nLoan will not be approved')


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
	
