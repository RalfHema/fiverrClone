from sixerrapp import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('gigs/<int:id>/', views.gig_detail, name='gig_detail'),
]
