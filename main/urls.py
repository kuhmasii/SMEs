from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
	path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('small/', views.small, name='small'),
    path('enterprise/', views.enterprise, name='enterprise'),
    path('medium/', views.medium, name='medium'),
    path('predict/', views.loan_predict,name='loan_predict'),
    path('loan-detail/<int:loan_id>/', views.loan_detail, name='loan_detail'),
    path('blogs/<int:id>/', views.full_blog_details, name='full_blog_details'),
    path('services/', views.service, name='service'),
    path('services/<str:service>/', views.service, name='service')
]


