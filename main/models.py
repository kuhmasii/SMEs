from django.db import models

class Loan(models.Model):
	
	LOAN_TYPE = (
		('small','SMALL'),
		('medium','MEDIUM'),
		('enterprise','ENTERPRISE')
	)

	name = models.CharField(max_length=50, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	loan_type = models.CharField(max_length=15, default='small', choices=LOAN_TYPE)
	image = models.ImageField(upload_to='images/', blank=True, null=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return self.name

	@property
	def url(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	
class Service(models.Model):
	name = models.CharField(max_length=100, blank=False, null=False)
	description = models.TextField(blank=True, null=True)
	url = models.URLField(max_length=500, blank=True, null=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return self.name

class Blog(models.Model):
	service = models.ForeignKey(Service, on_delete=models.SET_NULL, related_name='blog_service', blank=True, null=True)
	loan = models.ForeignKey(Loan, on_delete=models.SET_NULL, related_name='blog_loan', blank=True, null=True)
	name = models.CharField(max_length=100, null=True, blank=True)
	text = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to='images/', blank=True, null=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	url = models.URLField(max_length=1000, null=True, blank=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return self.name

	@property
	def url(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

class LoanPred(models.Model):
	
	GENDER_CHOICES = (
		('Male', 'Male'),
		('Female', 'Female')
	)
	MARRIED_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No')
	)
	GRADUATED_CHOICES = (
		('Graduate', 'Graduated'),
		('Not Graduate', 'Not Graduate')
	)
	SELFEMPLOYED_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No')
	)
	PROPERTY_CHOICES = (
		('Rural', 'Rural'),
		('Semiurban', 'Semiurban'),
		('Urban', 'Urban')
	)
	CREDIT_CHOICES = (
		("0", "0"),
		("1", "1")
	)
	
	firstname = models.CharField("Firstname", max_length=15, help_text='Enter Firstname')
	lastname = models.CharField("Lastname", max_length=15, help_text='Enter Lastname')
	dependants = models.IntegerField("Dependants", help_text='Enter Number of Dependents')
	applicant_income = models.IntegerField("Income", help_text='Enter Monthly Gross Income in Dollars')
	co_applicant_income = models.IntegerField("Co-Income", help_text='Enter Monthly Gross Income in Dollars')
	loan_amt = models.IntegerField("Loan Amount", help_text='Requested Loan Amount in Dollars')
	loan_term = models.IntegerField("Loan Term", help_text='Loan Term in Months')
	credit_history = models.CharField("Credit Histroy",max_length=4, choices=CREDIT_CHOICES)
	gender = models.CharField("Gender", max_length=15, choices=GENDER_CHOICES)
	married = models.CharField("Marital Status", max_length=15, choices=MARRIED_CHOICES)
	graduate = models.CharField("Education Status", max_length=15, choices=GRADUATED_CHOICES)
	self_employed = models.CharField("Employment Status", max_length=15, choices=SELFEMPLOYED_CHOICES)
	area = models.CharField("Area Status", max_length=15, choices=PROPERTY_CHOICES)

	def __str__(self):
		return '{}, {}'.format(self.lastname, self.firstname)

class File(models.Model):
	file = models.FileField(upload_to='file')
	created = models.DateTimeField(auto_now_add=True)