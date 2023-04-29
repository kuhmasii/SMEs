from django.contrib import admin
from . models import Service, LoanPred, Blog, File, Loan

admin.site.register(Service)
admin.site.register(Loan)
admin.site.register(Blog)
admin.site.register(File)
admin.site.register(LoanPred)
