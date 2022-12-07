from django.urls import path
from . import views
app_name = 'bookingapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.bookingappView, name='booking'),
    path('addbookingItem/',views.addbookingView), 
    path('deletebookingItem/<int:i>/', views.deletebookingView), 
] 