from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
	path('', views.index, name='index'),
    path('small/', views.small, name='small'),
    path('enterprise/', views.enterprise, name='enterprise'),
    path('medium/', views.medium, name='medium'),
    path('about/', views.about, name='about'),
    path('business-plans/', views.business_plan, name='business_plan'),
    path('services/', views.service, name='service'),
    path('small-detail/', views.detail_small, name='small_detail'),
    path('medium-detail/',views.detail_medium, name='medium-detail'),
    path('enterprise-detail', views.detail_enterprise, name='enterprise-detail'),

]


