from .utils import clean_file, clean_data, check_loan_status
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from . models import Loan, Service, Blog, File
from django.core.paginator import Paginator
from . forms import LoanPredForm, GraphForm
from django.http import HttpResponse
from django.contrib import messages
import pandas as pd

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
			form.save()

			# data coming from the user requesting for loan
			_ = request.POST.dict()
			user_data = dict(
						Gender=_['gender'], 
						Married=_['married'], 
						Dependents=float(_['dependants']), 
						Education=_['graduate'], 
						Self_Employed=_['self_employed'], 
						ApplicantIncome=float(_['applicant_income']), 
						CoapplicantIncome=float(_['co_applicant_income']), 
						LoanAmount=float(_['loan_amt']), 
						Loan_Amount_Term=float(_['loan_term']),
						Credit_History=_['credit_history'], 
						Property_Area=_['area']
			)

			# creating a dataframe for data to be used in pandas for 
			# data cleaning and encoding
			before_data = pd.DataFrame(user_data, index=[0])
			
			# calling the clean_data function to clean the data transformed 
			# into dataframe and also check for loan eligibility
			loan_status = check_loan_status(clean_data(before_data))

			if loan_status:
				if loan_status['status'] == "Approved":
					return HttpResponse("Congrats! You are Eligible for this loan.\nLoan will be approved")
				else:
					return HttpResponse('Opps! You are not Eligible for this loan.\nLoan will not be approved')
			return HttpResponse("Something went wrong")
		return HttpResponse(f'{form.errors}')

def full_blog_details(request, id=None):
	
	if id is not None:
		try:
			blog = Blog.objects.select_related('loan', 'service').get(id=id)
			blogs = Blog.objects.select_related('loan', 'service').all()[:6]
			services = Service.objects.all()
		except blog.DoesNotExist:
			raise HttpResponse("Page Does Not Exist")
		context = {'blog':blog, 'blogs':blogs, "services":services}
		return render(request, 'main/full_blog_detail.html', context)
	return HttpResponse("Page Not Found")

def service(request, service=None):
	
	if service is not None:
		service = Service.objects.get(name__iexact=service)
		filters = Blog.objects.filter(service=service)

		paginator = Paginator(filters, 5)
		page_number = request.GET.get("page")
		page_obj = paginator.get_page(page_number)
		context = {'service':service, 'page_obj':page_obj}
		
		return render(request, 'main/blog.html', context)
	else: 
		service = Service.objects.all()

	context = {'service':service}
	return render(request, 'main/services.html', context)

@csrf_exempt
def chart(request):

	form = GraphForm()
		
	if request.method == 'POST':
		form = GraphForm(request.POST, request.FILES)
		if form.is_valid():
			labels = form.cleaned_data.get('labels')
			data = form.cleaned_data.get('data')
			indicate = form.cleaned_data.get('indicator')
			file = form.cleaned_data.get('file')

			file = File.objects.create(file=file)

			plot = clean_file(file, labels, data, indicate)
			
			if plot is None:
				messages.error(request, "Column name must match the one on the File")

			form = GraphForm()
			file.delete()
			context = {'form':form, "chart": plot, 'check':True}
			return render(request, 'main/monitoring.html', context)
	return render(request, 'main/monitoring.html', {'form':form})
	