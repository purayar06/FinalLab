from django.shortcuts import render
from .models import bookingListItem 
from django.http import HttpResponseRedirect 

from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'index.html')


@login_required(login_url='/login')
def bookingappView(request):
    
    user_email = request.user.email
    all_booking_items = bookingListItem.objects.filter(user=user_email)
    return render(request, 'bookings.html',  {'all_items':all_booking_items})

@login_required(login_url='/login')
def addbookingView(request):
    user_email = request.user.email
    new_item = bookingListItem()
    new_item.user = user_email
    new_item.content = request.POST.get('content')
    new_item.showsdatetime = request.POST.get('showsdatetime')
    new_item.save()
    return HttpResponseRedirect('/booking/') 
    
@login_required(login_url='/login')
def deletebookingView(request, i):
    y = bookingListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/booking/') 