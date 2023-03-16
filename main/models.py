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

class Service(models.Model):
	name = models.CharField(max_length=100, blank=False, null=False)
	description = models.TextField(blank=True, null=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return self.name


class Blog(models.Model):
	service = models.ForeignKey(Service, on_delete=models.SET_NULL, related_name='blog_service', blank=True, null=True)
	loan = models.ForeignKey(Loan, on_delete=models.SET_NULL, related_name='blog_loan', blank=True, null=True)
	name = models.CharField(max_length=50, null=True, blank=True)
	text = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to='images/', blank=True, null=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return self.name
